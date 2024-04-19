import logging
import random
import requests
import numpy as np
from src.snap.latentmodule import LatentModule
from src.snap.vsync import wait_vblank

logger = logging.getLogger(__name__)


class Settings:

    def __init__(self):
        self.sub_title = '[SUB_TITLE]'
        self.general_instructions = '[GENERAL_INSTRUCTIONS]'

        self.continue_key = 'space'
        self.startup_delay = 3
        self.end_delay = 3

        self.frequencies_to_test = [8, 9, 13, 14, 15, 16]

        self.randomize_freq_for_each_box = False
        self.randomize_test_trials = True
        self.randomize_trials = True

        self.number_of_test_trials = 0
        self.number_of_trials = 2

        self.trial_duration = 5
        self.trial_tite_duration = 2
        self.start_trial_duration = 0
        self.end_trial_duration = 2

        self.rest_each_n_trials = 3
        self.rest_duration = 5

        self.boxes_settings = {'top_left':{'size':(0.2, 0.2),'center':(-1.4, 0.6)},
                               'top_middle':{'size':(0.2, 0.2),'center':(0.0, 0.6)},
                               'top_right':{'size':(0.2, 0.2),'center':(1.4, 0.6)},
                               'bottom_left':{'size':(0.2, 0.2),'center':(-1.4, -0.6)},
                               'bottom_middle':{'size':(0.2, 0.2),'center':(0.0, -0.6)},
                               'bottom_right':{'size':(0.2, 0.2),'center':(1.4, -0.6)}
                               }

        self.check_box_on = True
        self.check_box_size = (0.05, 0.05)
        self.check_box_center = (-1.725, -0.95)

        self.transparent = (0, 0, 0, 0)
        self.red = (1, 0, 0, 1)
        self.bg_color = (0.5, 0.5, 0.5, 1)
        self.white = (1, 1, 1, 1)
        self.black = (0, 0, 0, 1)

        self.color_map = {'white': (1, 1, 1, 1),
                          'black': (0, 0, 0, 1),
                          'grey': (0.4, 0.4, 0.4, 1),
                          'green': (0, 1, 0, 1),
                          'red': (1, 0, 0, 1),
                          'blue': (0, 0, 1, 1),
                          'bg': (0.5, 0.5, 0.5, 1)}

        # target frame rate -- be sure to verify this against screen
        self.framerate = 60.0
        # on some screens can cause frame rate to drop!
        self.turn_on_wait_v_blank = False

        self.online_ssvep_url = "http://localhost:5000"

        if (len(self.frequencies_to_test) != len(self.boxes_settings)):
            raise Exception("Amount of requencies have to equal amount of boxes")

        if (self.number_of_trials == 0):
            raise Exception("Number of trial can not be 0")
        

class Main(LatentModule):

    def __init__(self):
        LatentModule.__init__(self)
        Settings.__init__(self)

    def generate_sequence(self, f, phi, refresh_rate, duration_s):
        # arrange from - 1 / refresh_rate to avoid first 0.5 that
        # would be generated if started from 0
        time_array = np.arange(1 / refresh_rate, duration_s, 1 / refresh_rate) # time array
        seq_array = 0.5 * (1 + np.sign(np.sin(2 * np.pi * f * time_array + phi))) # sequence of 0s and 1s
        return seq_array

    def get_box(self, box_center, box_size):
        """Creates a transparent box and returns its reference"""
        xpos, ypos = box_center
        width, height = box_size
        box_dims = (xpos - width, xpos + width, ypos - height, ypos + height)
        return self.rectangle(box_dims, duration=0, block=False, color=self.transparent)
    
    def show_red_rectangle(self, rect_center, rect_size):
        """Creates a red rectangle that should show which box to look at"""
        xpos, ypos = rect_center
        width, height = rect_size
        rect_dims = (xpos - width, xpos + width, ypos - height, ypos + height)
        return self.frame(rect_dims, (0.02, 0.02), duration=1.5, block=True, color=self.red)
    
    def show_target_rectangle(self, frequencies: list):

        for box in self.boxes:
            if self.target_freq == box['freq']:
                width, height = box['size']
                self.show_red_rectangle(box['center'], (width + 0.05, height + 0.05))


    def setup_boxes_for_trial(self, boxes_settings: dict, frequencies_for_boxes: list):
        """Initialize box"""

        self.boxes = []
        
        for key, box_setting in boxes_settings.items():
            box = {}
            freq = frequencies_for_boxes[list(boxes_settings).index(key)]
            box['box'] = self.get_box(box_setting['center'], box_setting['size'])
            box['size'] = box_setting['size']
            box['center'] = box_setting['center']
            box['freq'] = freq
            box['seq_array'] = self.generate_sequence(freq, 0, self.framerate, self.trial_duration)
            box['frame_counter'] = 0

            self.boxes.append(box)

        if self.check_box_on:
            self.check_box = self.get_box(self.check_box_center, self.check_box_size)


    def replicate_for_check_box(self, color):
        if self.check_box_on and self.check_box is not None:
            self.check_box.set_color(color)


    def destroy_box(self):
        """Destroys current box in the engine"""
        for box in self.boxes:
            if box is not None:
                if box['box'] is not None:
                    box['box'].destroy()

        if self.check_box_on and self.check_box is not None:
            self.check_box.destroy()

    def setup(self):
        """Initialize the start of the task"""
        # initialize some counters
        # frame counter
        self.framenum = 0
        # time stamp of the last dropped frame
        self.last_frame_drop = None
        # Array of trials
        self.all_test_trials = self.frequencies_to_test * self.number_of_test_trials
        self.all_trials = self.frequencies_to_test * self.number_of_trials

        if self.randomize_test_trials:
            random.shuffle(self.all_test_trials)
        
        if self.randomize_trials:
            random.shuffle(self.all_trials)
        

    def now(self):
        """Get current time in seconds."""
        return self.framenum / self.framerate

    def on_tick(self, dt, block_active=False):
        """Executes on every tick (which should be every frame, depends on refrashrate of monitor)
        when called with block_active=True it updates box"""

        # track the current frame number
        delta_frames = int(round(dt / (1.0 / self.framerate)))

        # get current time, depending on method
        now = self.now()

        # insert dummy frames for each dropped frame since the last
        # update (these will have a lagged time stamp, but this can be corrected
        # post-hoc by linearizing the time stamps)
        if delta_frames > 1:
            num_dropped = delta_frames - 1
            time_since_drop = now - self.last_frame_drop if self.last_frame_drop is not None else 0
            self.last_frame_drop = now
            logger.info('missed %i frames after frame %i (%.1f ms since last drop)' % (
                num_dropped, self.framenum, 1000 * time_since_drop))

        self.framenum = self.framenum + delta_frames

        if block_active:
            for box_dict in self.boxes:
                box = box_dict['box']
                freq = box_dict['freq']
                seq_array = box_dict['seq_array']
                frame_counter = box_dict['frame_counter']

                if frame_counter < len(seq_array):
                    if seq_array[frame_counter] == 1.0:
                        box.set_color(self.color_map['white'])
                        if (self.target_freq == freq):
                            self.replicate_for_check_box(self.color_map['white'])
                    else:
                        box.set_color(self.color_map['black'])
                        if (self.target_freq == freq):
                            self.replicate_for_check_box(self.color_map['black'])

                    box_dict['frame_counter'] = frame_counter + 1


        # wait for a vertical blank period
        if self.turn_on_wait_v_blank:
            wait_vblank()

    def run(self):
        """Main loop of the experiment"""

        base.win.setClearColor(self.bg_color)

        self.setup()

        self.write(f'''
                   SSVEP:
                   {self.sub_title}
                   ''', duration=self.startup_delay, block=True, align='center', pos=(0, 0), scale=0.12)

        self.marker('instructions-shown')

        self.write(f'''
                   Instructions:

                   {self.general_instructions}

                   Each trial takes {self.trial_duration}s with
                   total of {self.number_of_trials * len(self.frequencies_to_test)} trials

                   Please press {self.continue_key} to continue
                   ''',
                   duration=[0, self.continue_key],
                   block=True,
                   align='center',
                   scale=0.09,
                   wordwrap=30,
                   pos=[0, 0.4])
        

        logger.info(f"XDF File Path on SSVEP SERVER: {requests.get('http://localhost:5000/api/xdf-file').content}")
        
        # TEST TRIALS START ///////////////////////////
        if self.number_of_test_trials > 0:

            self.write(f'''
                        Test trials starting...
                        ''', duration=self.trial_tite_duration, block=True, align='center', pos=(0, 0), scale=0.12)

            self.marker('test-trials-start')

            for trial_idx, frequency in enumerate(self.all_test_trials):

                if self.rest_each_n_trials != 0 and trial_idx > 0 and trial_idx % self.rest_each_n_trials == 0:
                    for i in range(self.rest_duration):
                        self.write(f'''
                                    Rest. Test trial start in {self.rest_duration - i}s...
                                    ''', duration=1, block=True, align='center', pos=(0, 0), scale=0.12)
                
                # show title
                self.marker('trial-title-show')
                self.write(f'Test trial {trial_idx + 1} - {frequency}Hz', duration=self.trial_tite_duration, block=True, align='center',
                        pos=(0, 0), scale=0.12)
        
                for i in range(self.start_trial_duration):
                    self.write(f'''
                                Test trial start in {self.start_trial_duration - i}s...
                                ''', duration=1, block=True, align='center', pos=(0, 0), scale=0.12)

                # setup boxes for this trial
                self.target_freq = frequency

                if self.randomize_freq_for_each_box:
                    freq_to_shuffle = list(self.frequencies_to_test)
                    random.shuffle(freq_to_shuffle)
                    frequencies = freq_to_shuffle
                else:
                    frequencies = list(self.frequencies_to_test)
                
                self.setup_boxes_for_trial(self.boxes_settings, frequencies)
                self.show_target_rectangle(frequencies)

                self.marker(f'test-trial-start-{frequency}-hz')

                self.sleep(self.trial_duration, cur_tick=lambda dt: self.on_tick(dt, block_active=True))

                self.marker(f'test-trial-end-{frequency}-hz')

                self.destroy_box()

            self.marker('test-trials-end')

            self.write("Process calibration trials...", duration=0.1, block=True, align='center', pos=(0, 0), scale=0.12)
            result = requests.post('http://localhost:5000/api/process/calibration-trials')

            if result.status_code == 200:
                self.write("Calibration trials processed successfully", duration=2, block=True, align='center', pos=(0, 0), scale=0.12)
            else:
                self.write("Processing of calibration trials failed, exiting...", duration=2, block=True, align='center', pos=(0, 0), scale=0.12)
                return

        # TRIALS START /////////////////////////////////
        self.write(f'''
                    Trials starting...
                    ''', duration=self.trial_tite_duration, block=True, align='center', pos=(0, 0), scale=0.12)

        self.marker('trials-start')

        for trial_idx, frequency in enumerate(self.all_trials):

            if self.rest_each_n_trials != 0 and trial_idx > 0 and trial_idx % self.rest_each_n_trials == 0:
                for i in range(self.rest_duration):
                    self.write(f'''
                                Rest. Trial start in {self.rest_duration - i}s...
                                ''', duration=1, block=True, align='center', pos=(0, 0), scale=0.12)
            # show title
            self.marker('trial-title-show')
            self.write(f'Trial {trial_idx + 1} - {frequency}Hz', duration=self.trial_tite_duration, block=True, align='center',
                       pos=(0, 0), scale=0.12)
       
            for i in range(self.start_trial_duration):
                self.write(f'''
                            Trial start in {self.start_trial_duration - i}s...
                            ''', duration=1, block=True, align='center', pos=(0, 0), scale=0.12)

            # setup boxes for this trial
            self.target_freq = frequency

            if self.randomize_freq_for_each_box:
                freq_to_shuffle = list(self.frequencies_to_test)
                random.shuffle(freq_to_shuffle)
                frequencies = freq_to_shuffle
            else:
                frequencies = list(self.frequencies_to_test)
            
            self.setup_boxes_for_trial(self.boxes_settings, frequencies)
            self.show_target_rectangle(frequencies)

            self.marker(f'trial-start-{frequency}-hz-{trial_idx}')

            self.sleep(self.trial_duration, cur_tick=lambda dt: self.on_tick(dt, block_active=True))

            self.destroy_box()

            self.marker(f'trial-end-{frequency}-hz-{trial_idx}')

            self.write(f'''Process trial...''', duration=0.1, block=True, align='center', scale=0.09, wordwrap=30, pos=[0, 0.4])

            process_trial_request = {'markers': [f'trial-start-{frequency}-hz-{trial_idx}', f'trial-end-{frequency}-hz-{trial_idx}'], 'targetFrequency': frequency}
            result = requests.post('http://localhost:5000/api/process/process-trial', json=process_trial_request)

            if result.status_code != 200:
                self.write("Processing of trial failed, exiting...", duration=2, block=True, align='center', pos=(0, 0), scale=0.12)
                return
            
            data = result.json()
            is_correct = data['isCorrectMix']
            guessed_frequency = data['guessedFrequencyMix']

            if is_correct == 1:
                self.write(f'''Correct - {guessed_frequency}hz
                           
                            Press {self.continue_key} to continue''', fg=self.color_map['green'], duration=[0, self.continue_key], block=True, align='center', scale=0.09, wordwrap=30, pos=[0, 0.4])
            else:
                self.write(f'''Incorrect - {guessed_frequency}hz
                           
                           Press {self.continue_key} to continue''', fg=self.color_map['red'], duration=[0, self.continue_key], block=True, align='center', scale=0.09, wordwrap=30, pos=[0, 0.4])

        self.marker('trials-end')

        self.write('Finished', duration=self.end_delay, align='center', pos=(0, 0), scale=0.1)
