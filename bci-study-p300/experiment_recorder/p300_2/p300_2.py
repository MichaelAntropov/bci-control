from src.snap.latentmodule import LatentModule


class Main(LatentModule):
    def __init__(self):
        LatentModule.__init__(self)

        self.a = [(20, 0.2), (20, 0.25), (20, 0.3), (20, 0.4)]
        self.time_between_blocks = 5

    def run(self):

        elements = ("pics\\sq.jpg","pics\\sq2.jpg");
        black = (0, 0, 0, 1)
        self.write('P300 response experiment', 3, align='center', pos=(0, 0), scale=0.12,
                   fg=black)

        whole_time = 0

        for block in self.a:
            whole_time += block[0]

        whole_time += self.time_between_blocks * (len(self.a) - 1)

        task_text = self.write(f'''
                                
                            Welcome to P300 response experiment

                            P300 experiment with different frequencies
                            
                            The experiment will last ~{whole_time}
                                
                            Press space to continue
                                
                            ''', duration=0, block=False, scale=0.09, wordwrap=30, pos=[0, 0.5])

        while True:
            response, _ = self.waitfor_multiple(['space'], send_implicit_markers=False)
            if response == 'space':
                task_text.destroy()
                break

        for block in self.a:
            self.marker("block-start")
            self.write("Block start", duration=3, align='center', pos=(0, 0), scale=0.12, fg=black)
            tries = round(block[0]/block[1])
            for try_index in range(tries):
                self.marker("noise-{}-ms".format(int(block[1]*1000)))
                if try_index % 2 == 0:
                    self.picture(elements[0], duration=block[1], block=True)
                else:
                    self.picture(elements[1], duration=block[1], block=True)
            self.marker("block-end")
            self.write("Block end", duration=3, align='center', pos=(0, 0), scale=0.12, fg=black)
            self.write("Rest. You have {}s".format(self.time_between_blocks), duration=self.time_between_blocks, align='center', pos=(0, 0), scale=0.12, fg=black)
