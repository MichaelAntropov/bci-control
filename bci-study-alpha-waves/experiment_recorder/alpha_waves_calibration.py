"""
Simple Alpha Waves calibration task. Data recorded with markers
placed when subject is asked to close/open their eyes.

Later this session can be studied and a range of Alpha Wave for
particular subject calculated.

(c) Michael Antropov
"""

import inspect
import logging
import random
from src.snap.latentmodule import LatentModule

logger = logging.getLogger(__name__)


class Main(LatentModule):
    def __init__(self):
        LatentModule.__init__(self)

        self.continue_key = 'space'
        self.startup_delay = 3
        self.transition_sound = 'default_bing.wav'
        self.open_eyes_sound = 'open.mp3'
        self.close_eyes_sound = 'close.mp3'
        self.open_phase_duration_time_frame = (10, 15)
        self.close_phase_duration_time_frame = (10, 15)
        self.phase_count = 10

    def run(self):

        # Calculate session duration and phases based on phase duration time frame and count
        min_open_duration, max_open_duration = self.open_phase_duration_time_frame
        min_close_duration, max_close_duration = self.close_phase_duration_time_frame
        eyes_open = True
        phases = []
        total_duration = 0
        for i in range(self.phase_count):
            phase_duration = 0
            if eyes_open:
                phase_duration = random.randint(min_open_duration, max_open_duration)
                phases.append(('open', phase_duration))
            else:
                phase_duration = random.randint(min_close_duration, max_close_duration)
                phases.append(('close', phase_duration))
            total_duration += phase_duration
            eyes_open = not eyes_open

        base.win.setClearColor((0.5, 0.5, 0.5, 1))

        self.write('Alpha Waves Calibration', duration=self.startup_delay, align='center', pos=(0, 0), scale=0.12,
                   fg=(0, 0, 0, 1))

        self.sound(self.transition_sound, block=False, volume=1)

        task_text = self.write(inspect.cleandoc(f"""\
                Instructions: 
    
                During calibration process we will 
                record EEG data.
                
                Please, start with sitting in a relaxed position 
                with your eyes opened. During the test you will be
                asked to open/close your eyes.
                
                You may blink, when your eyes open. Data collecting 
                process will take %i seconds.
                
                Press %s to start the session...
                
                """) % (total_duration, self.continue_key), duration=0, block=False, scale=0.09, wordwrap=30,
                               pos=[0, 0.5])

        while True:
            response, time = self.waitfor_multiple([self.continue_key], send_implicit_markers=False)
            if response == self.continue_key:
                task_text.destroy()
                break

        self.sound(self.transition_sound, block=False, volume=1)
        self.marker('calibration-start')

        for phase in phases:
            action, duration = phase
            self.sound(self.open_eyes_sound if action is 'open' else self.close_eyes_sound, block=False, volume=1)
            self.marker('calibration-' + action)
            self.write(action, duration=duration)

        self.sound(self.transition_sound, block=False, volume=1)
        self.marker('calibration-end')

        self.write('Finished.', duration=3, align='center', pos=(0, 0), scale=0.1, fg=(0, 0, 0, 1))
