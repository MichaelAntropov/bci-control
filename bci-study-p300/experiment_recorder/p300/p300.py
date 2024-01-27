import random
import csv
from src.snap.latentmodule import LatentModule


class Main(LatentModule):
    def __init__(self):
        LatentModule.__init__(self)

        self.main_key = 'space'
        self.startup_delay = 3
        self.tries = 10
        self.min_rand = 4
        self.max_rand = 6
        self.time_of_rect = 0.25
        self.time_of_oddball = 0.5
        self.is_red = True
        self.blocks = 10
        self.time_between_blocks = 5
        self.csv_path = "your path"

    def run(self):

        # Setup
        transition_sound = 'default_bing.wav'
        black = (0, 0, 0, 1)
        gray = (0.5, 0.5, 0.5, 1)
        oddball_pic = "pics\\psq.jpg" if self.is_red else "pics\\gsq.jpg"
        elements = {
            "noise_square_rot_0": {"type": "noise_square", "pic_path": "pics\\sq.jpg", "time": self.time_of_rect},
            "noise_square_rot_90": {"type": "noise_square", "pic_path": "pics\\sq2.jpg", "time": self.time_of_rect},
            "oddball_square": {"type": "oddball", "pic_path": oddball_pic, "time": self.time_of_oddball},
            "block_start": {"type": "block_start", "time": self.startup_delay},
            "block_end": {"type": "block_end", "time": self.startup_delay},
            "pause": {"type": "pause", "time": self.time_between_blocks}}

        base.win.setClearColor(gray)

        all_frames = []

        def generate_noises_array() -> list:
            result_noises_array = []
            noises_amount = round(random.randint(self.min_rand, self.max_rand) / self.time_of_rect)
            for noise_index in range(noises_amount):
                if noise_index % 2 == 0:
                    result_noises_array.append(elements["noise_square_rot_0"])
                else:
                    result_noises_array.append(elements["noise_square_rot_90"])
            return result_noises_array

        for block_index in range(self.blocks):
            all_frames.append(elements["block_start"])

            for try_index in range(self.tries):
                all_frames.extend(generate_noises_array())
                all_frames.append(elements["oddball_square"])

            all_frames.extend(generate_noises_array())
            all_frames.append(elements["block_end"])
            if block_index != self.blocks - 1:
                all_frames.append(elements["pause"])

        whole_time = 0.0

        for frame in all_frames:
            whole_time += frame["time"]

        csvfile = open(self.csv_path, 'w', newline='')
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['reaction time', 'block'])

        self.write('P300 response experiment', duration=self.startup_delay, align='center', pos=(0, 0), scale=0.12,
                   fg=black)

        self.sound(transition_sound, block=False, volume=1)

        task_text = self.write(f'''
                                
                            Welcome to P300 response experiment

                            In this experiment you'll stare at monitor and you'll see some noises
                            from {self.min_rand} to {self.max_rand} seconds, then you'll see red square.

                            You should press {self.main_key} as fast as possible and count every time you see square. 
                            Try not to clip your eyes during block.

                            There will be {self.blocks} blocks, each has {self.tries} tries.

                            Experiment will last {round(whole_time)} seconds
                                
                            Press space to continue
                                
                            ''', duration=0, block=False, scale=0.09, wordwrap=30, pos=[0, 0.7])

        while True:
            response, _ = self.waitfor_multiple(['space'], send_implicit_markers=False)
            if response == 'space':
                task_text.destroy()
                break
            self.sound(transition_sound, block=False, volume=1)

        watcher = None
        counter = 0
        # block_counter = 0

        avg_total = []
        avg_block = []
        block_counter = 1

        for frame in all_frames:
            if frame["type"] == "noise_square":
                self.marker("noise")
                if self.main_key is not None:
                    counter -= 1
                    if counter == 0 and watcher is not None:
                        watcher_result = self.watchfor_multiple_end(watcher)
                        if len(watcher_result[self.main_key]) > 0:
                            response_time = watcher_result[self.main_key][0]
                            avg_total.append(response_time)
                            csvwriter.writerow([response_time, block_counter])
                            avg_block.append(response_time)
                self.picture(frame["pic_path"], frame["time"], block=True)
            elif frame["type"] == "oddball":
                self.marker("oddball")
                if self.main_key is not None:
                    watcher = self.watchfor_multiple_begin([self.main_key])
                    counter = 3
                self.picture(frame["pic_path"], frame["time"], block=True)
            elif frame["type"] == "block_start":
                self.marker("block_start")
                avg_block = []
                block_counter += 1
                self.write("Block start", duration=frame["time"], align='center', pos=(0, 0), scale=0.12, fg=black)
            elif frame["type"] == "block_end":
                self.marker("block_end")
                if self.main_key is None:
                    self.write("Block end", duration=frame["time"], align='center', pos=(0, 0), scale=0.12,
                               fg=black)
                else:
                    self.write("Block end. Average response time {}s".format(round(sum(avg_block) / len(avg_block), 3)),
                               duration=frame["time"], align='center', pos=(0, 0), scale=0.12, fg=black)
            elif frame["type"] == "pause":
                self.write("Rest. Next block will start in {} seconds".format(frame["time"]), duration=frame["time"],
                           align='center', pos=(0, 0), scale=0.12, fg=black)
        if self.main_key is None:
            self.write("Finished", duration=self.startup_delay,
                       align='center', pos=(0, 0), scale=0.12, fg=black)
        else:
            self.write("Finished. Average response time {}s".format(round(sum(avg_total) / len(avg_total), 3)),
                       duration=self.startup_delay, align='center', pos=(0, 0), scale=0.12, fg=black)
        csvfile.close()
