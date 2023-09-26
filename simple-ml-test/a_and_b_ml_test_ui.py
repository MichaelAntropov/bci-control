import os
import threading
import time
from tkinter import messagebox, ttk
from tkinter.constants import END

import customtkinter
import numpy as np
from pylsl import LostError

import bci_config
import bci_lsl
import bci_ml

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    bci_connection = None
    bci_connections = set()
    recording_samples = False
    test_model = None
    modes = ["collect", "train", "test"]
    current_mode = "collect"

    def __init__(self):
        super().__init__()

        # Configure window and layout
        self.title("A&B BCI-ML TEST")
        self.geometry(f"{1100}x{900}")

        # Fix for CTkEntry not losing focus
        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())

        # Set on exit
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.north_frame = customtkinter.CTkFrame(self)
        self.north_frame.grid(row=0, column=0, columnspan=3, sticky="wne", padx=10, pady=10)

        # self.west_frame = customtkinter.CTkFrame(self)
        # self.west_frame.grid(row=1, column=0, sticky="wns", padx=10, pady=10)
        #
        # self.east_frame = customtkinter.CTkFrame(self)
        # self.east_frame.grid(row=1, column=2, sticky="ens", padx=10, pady=10)

        self.center_frame = customtkinter.CTkFrame(self)
        self.center_frame.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        self.south_frame = customtkinter.CTkFrame(self)
        self.south_frame.grid(row=2, column=0, columnspan=3, sticky="wse", padx=10, pady=10)

        # North frame contents
        self.north_frame.grid_columnconfigure(1, weight=1)

        self.is_key_pressed_reg = customtkinter.CTkCheckBox(self.north_frame, text="Register 'A' and 'B' key press")
        self.is_key_pressed_reg.grid(row=0, column=0, padx=10, pady=10, sticky="wn")

        # Center frame contents
        self.center_frame.configure(fg_color="transparent")
        self.center_frame.grid_columnconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(3, weight=1)
        self.center_frame.grid_rowconfigure(0, weight=1)

        self.a_and_b_font = customtkinter.CTkFont(family="Arial")

        self.label_a = customtkinter.CTkLabel(self.center_frame, text="A",
                                              fg_color="white", font=self.a_and_b_font)
        self.label_b = customtkinter.CTkLabel(self.center_frame, text="B",
                                              fg_color="white", font=self.a_and_b_font)

        self.label_a.grid(row=0, column=1, padx=10)
        self.label_b.grid(row=0, column=2, padx=10)

        # # Bind frame size to a_and_b_font size
        self.center_frame.bind("<Configure>", self.resize_a_and_b_font)

        # # Handle A & B keys pressed
        self.bind("<KeyRelease>", self.a_or_b_pressed)

        # South frame contents
        self.south_frame.configure(fg_color="transparent")
        self.south_frame.grid_columnconfigure(0, weight=1)
        self.south_frame.grid_columnconfigure(1, weight=3)

        # # LSL config & settings
        self.tabview_settings = customtkinter.CTkTabview(self.south_frame)
        self.tabview_settings.grid(row=0, column=0, padx=10, sticky="nsew")
        self.lsl_config_tab = self.tabview_settings.add("LSL config")
        self.settings_tab = self.tabview_settings.add("Settings")

        self.lsl_config_tab.columnconfigure(0, weight=1)
        self.settings_tab.columnconfigure(0, weight=1)

        # # # LSL config tab
        self.lsl_settings_frame = customtkinter.CTkScrollableFrame(self.lsl_config_tab, fg_color="transparent")
        self.lsl_settings_frame.grid(row=0, column=0, sticky="nsew")
        self.lsl_settings_frame.grid_columnconfigure(2, weight=1)

        customtkinter.CTkLabel(self.lsl_settings_frame, text="Stream name:") \
            .grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.lsl_stream_name_entry = customtkinter.CTkEntry(self.lsl_settings_frame)
        self.lsl_stream_name_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        self.lsl_connect_button = customtkinter.CTkButton(self.lsl_settings_frame)
        self.lsl_connect_button.configure(text="Connect", command=self.connect_lsl)
        self.lsl_connect_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="we")

        customtkinter.CTkLabel(self.lsl_settings_frame, text="Collect samples\nafter duration(ms):",
                               justify="left").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.collect_samples_after_duration_ms_entry = customtkinter.CTkEntry(self.lsl_settings_frame)
        self.collect_samples_after_duration_ms_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        customtkinter.CTkLabel(self.lsl_settings_frame, text="Sample count:") \
            .grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.sample_count_entry = customtkinter.CTkEntry(self.lsl_settings_frame)
        self.sample_count_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        self.record_samples_checkbox = customtkinter.CTkCheckBox(master=self.lsl_settings_frame,
                                                                 text="Record samples")
        self.record_samples_checkbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # # # Settings tab
        self.settings_frame = customtkinter.CTkScrollableFrame(self.settings_tab, fg_color="transparent")
        self.settings_frame.grid(row=0, column=0, sticky="nsew")

        customtkinter.CTkLabel(self.settings_frame, text="Label flash duration(ms):") \
            .grid(row=0, column=0, padx=5, pady=5)
        self.label_flash_duration_ms_entry = customtkinter.CTkEntry(self.settings_frame)
        self.label_flash_duration_ms_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        # # TabView
        self.tabview = customtkinter.CTkTabview(self.south_frame, command=self.change_mode)
        self.tabview.grid(row=0, column=1, padx=(0, 10), sticky="nsew")

        self.collect_data_tab = self.tabview.add("Collect data")
        self.train_tab = self.tabview.add("Train")
        self.collect_and_test_tab = self.tabview.add("Collect data & test")
        self.test_only_tab = self.tabview.add("Test only")

        # # # Collect data tab
        self.collect_data_tab.grid_columnconfigure(0, weight=1)
        self.collect_data_tab_frame = customtkinter.CTkScrollableFrame(self.collect_data_tab, fg_color="transparent")
        self.collect_data_tab_frame.grid(row=0, column=0, sticky="nsew")
        self.collect_data_tab_frame.grid_columnconfigure(1, weight=1)

        customtkinter.CTkLabel(self.collect_data_tab_frame, text="Data folder 'A' path:") \
            .grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.data_folder_a_entry = customtkinter.CTkEntry(self.collect_data_tab_frame)
        self.data_folder_a_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        customtkinter.CTkLabel(self.collect_data_tab_frame, text="Data folder 'B' path:") \
            .grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.data_folder_b_entry = customtkinter.CTkEntry(self.collect_data_tab_frame)
        self.data_folder_b_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        customtkinter.CTkLabel(self.collect_data_tab_frame, text="Data folder 'NONE' path:") \
            .grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.data_folder_none_entry = customtkinter.CTkEntry(self.collect_data_tab_frame)
        self.data_folder_none_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        # # # Train tab
        self.train_tab.grid_columnconfigure(0, weight=1)
        self.train_tab_frame = customtkinter.CTkScrollableFrame(self.train_tab, fg_color="transparent")
        self.train_tab_frame.grid(row=0, column=0, sticky="nsew")
        self.train_tab_frame.grid_columnconfigure(1, weight=1)

        customtkinter.CTkLabel(self.train_tab_frame, text="Original data folder:") \
            .grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.original_data_folder_entry = customtkinter.CTkEntry(self.train_tab_frame)
        self.original_data_folder_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        customtkinter.CTkLabel(self.train_tab_frame, text="New data folder:") \
            .grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.new_data_folder_entry = customtkinter.CTkEntry(self.train_tab_frame)
        self.new_data_folder_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        self.create_train_and_valid_dirs_button = customtkinter.CTkButton(self.train_tab_frame,
                                                                          text="Create train and validation dirs")
        self.create_train_and_valid_dirs_button.grid(row=2, column=1, padx=5, pady=5, sticky="we")
        self.create_train_and_valid_dirs_button.configure(command=self.create_train_and_validation_dirs)

        customtkinter.CTkLabel(self.train_tab_frame, text="Train data folder:") \
            .grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.train_data_folder_entry = customtkinter.CTkEntry(self.train_tab_frame)
        self.train_data_folder_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        customtkinter.CTkLabel(self.train_tab_frame, text="Validation data folder:") \
            .grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.validation_data_folder_entry = customtkinter.CTkEntry(self.train_tab_frame)
        self.validation_data_folder_entry.grid(row=4, column=1, padx=5, pady=5, sticky="we")

        customtkinter.CTkLabel(self.train_tab_frame, text="Created models folder:") \
            .grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.created_models_folder_entry = customtkinter.CTkEntry(self.train_tab_frame)
        self.created_models_folder_entry.grid(row=5, column=1, padx=5, pady=5, sticky="we")

        self.train_and_evaluate_button = customtkinter.CTkButton(self.train_tab_frame,
                                                                 text="Train and evaluate")
        self.train_and_evaluate_button.grid(row=6, column=1, padx=5, pady=5, sticky="we")
        self.train_and_evaluate_button.configure(command=self.train_model)

        self.train_console = customtkinter.CTkTextbox(self.train_tab_frame)
        self.train_console.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.train_console.insert("0.0", "Train console>\n")
        self.train_console.configure(wrap="none", state="disabled")

        self.clear_train_console_button = customtkinter.CTkButton(self.train_tab_frame,
                                                                  text="Clear console")
        self.clear_train_console_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.clear_train_console_button.configure(command=lambda: clear_console(self.train_console))

        # # # Test only tab

        self.test_only_tab.grid_columnconfigure(0, weight=1)
        self.test_only_tab_frame = customtkinter.CTkScrollableFrame(self.test_only_tab, fg_color="transparent")
        self.test_only_tab_frame.grid(row=0, column=0, sticky="nsew")
        self.test_only_tab_frame.grid_columnconfigure(1, weight=1)

        customtkinter.CTkLabel(self.test_only_tab_frame, text="Path to model:") \
            .grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.model_to_test_entry = customtkinter.CTkEntry(self.test_only_tab_frame)
        self.model_to_test_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        self.load_test_model_button = customtkinter.CTkButton(self.test_only_tab_frame,
                                                              text="Load model")
        self.load_test_model_button.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        self.load_test_model_button.configure(command=self.load_test_model)

        self.test_console = customtkinter.CTkTextbox(self.test_only_tab_frame)
        self.test_console.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.test_console.insert("0.0", "Test only console>\n")
        self.test_console.configure(wrap="none", state="disabled")

        self.clear_test_console_button = customtkinter.CTkButton(self.test_only_tab_frame,
                                                                 text="Clear console")
        self.clear_test_console_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.clear_test_console_button.configure(command=lambda: clear_console(self.test_console))

        # Read config
        self.config_full = bci_config.read_config()
        self.config = self.config_full['config']

        self.label_flash_duration_ms_entry.insert(0, self.config[bci_config.label_flash_duration_ms])

        self.lsl_stream_name_entry.insert(0, self.config[bci_config.lsl_stream_name])
        self.collect_samples_after_duration_ms_entry \
            .insert(0, self.config[bci_config.collect_samples_after_duration_ms])
        self.sample_count_entry.insert(0, self.config[bci_config.sample_count])

        self.data_folder_a_entry.insert(0, self.config[bci_config.collect_data_folder_a])
        self.data_folder_b_entry.insert(0, self.config[bci_config.collect_data_folder_b])
        self.data_folder_none_entry.insert(0, self.config[bci_config.collect_data_folder_none])

        self.original_data_folder_entry.insert(0, self.config[bci_config.train_original_data_folder])
        self.new_data_folder_entry.insert(0, self.config[bci_config.train_new_data_folder])

        self.train_data_folder_entry.insert(0, self.config[bci_config.train_train_data_folder])
        self.validation_data_folder_entry.insert(0, self.config[bci_config.train_validation_data_folder])
        self.created_models_folder_entry.insert(0, self.config[bci_config.train_created_models_folder])
        self.model_to_test_entry.insert(0, self.config[bci_config.test_model_to_test])

    def on_exit(self):
        self.config[bci_config.label_flash_duration_ms] = self.label_flash_duration_ms_entry.get()

        self.config[bci_config.lsl_stream_name] = self.lsl_stream_name_entry.get()
        self.config[bci_config.collect_samples_after_duration_ms] = self.collect_samples_after_duration_ms_entry.get()
        self.config[bci_config.sample_count] = self.sample_count_entry.get()

        self.config[bci_config.collect_data_folder_a] = self.data_folder_a_entry.get()
        self.config[bci_config.collect_data_folder_b] = self.data_folder_b_entry.get()
        self.config[bci_config.collect_data_folder_none] = self.data_folder_none_entry.get()

        self.config[bci_config.train_original_data_folder] = self.original_data_folder_entry.get()
        self.config[bci_config.train_new_data_folder] = self.new_data_folder_entry.get()

        self.config[bci_config.train_train_data_folder] = self.train_data_folder_entry.get()
        self.config[bci_config.train_validation_data_folder] = self.validation_data_folder_entry.get()
        self.config[bci_config.train_created_models_folder] = self.created_models_folder_entry.get()
        self.config[bci_config.test_model_to_test] = self.model_to_test_entry.get()

        bci_config.save_config(self.config)
        self.destroy()

    def resize_a_and_b_font(self, event):
        new_height = round(event.height * 1.2)
        new_width = round(event.width / 2 * 1.4)
        self.a_and_b_font.configure(size=min(new_height, new_width))

    def change_mode(self):
        tab_name = self.tabview.get()
        if tab_name == "Collect data":
            self.current_mode = "collect"
        elif tab_name == "Train":
            self.current_mode = "train"
        elif tab_name == "Test only":
            self.current_mode = "test"
        else:
            self.current_mode = None

    def a_or_b_pressed(self, event):
        if self.is_key_pressed_reg.get() == 0 or self.current_mode is None:
            return

        if self.current_mode == "collect":
            self.a_or_b_pressed_collect_mode(event)
        elif self.current_mode == "test":
            self.a_or_b_pressed_train_mode(event)

    def a_or_b_pressed_collect_mode(self, event):
        if event.keysym == 'a':
            print("A key pressed!")
            self.label_a.configure(fg_color="red", text_color="white")
            self.after(self.label_flash_duration_ms_entry.get(),
                       lambda: self.label_a.configure(fg_color="white", text_color="black"))
            if self.record_samples_checkbox.get():
                self.collect_data(self.data_folder_a_entry.get())
        elif event.keysym == 'b':
            print("B key pressed!")
            self.label_b.configure(fg_color="red", text_color="white")
            self.after(self.label_flash_duration_ms_entry.get(),
                       lambda: self.label_b.configure(fg_color="white", text_color="black"))
            if self.record_samples_checkbox.get():
                self.collect_data(self.data_folder_b_entry.get())
        elif event.keysym == 'space':
            print("SPACE key pressed!")
            if self.record_samples_checkbox.get():
                self.collect_data(self.data_folder_none_entry.get())

    def a_or_b_pressed_train_mode(self, event):
        if event.keysym == 'a':
            print("A key pressed!")
            self.label_a.configure(fg_color="red", text_color="white")
            self.after(self.label_flash_duration_ms_entry.get(),
                       lambda: self.label_a.configure(fg_color="white", text_color="black"))
            if self.record_samples_checkbox.get():
                self.print_to_test_console("A key pressed - ", end="")
                channel_data = self.consume_samples()
                out, confidence = bci_ml.predict(self.test_model, channel_data)
                self.print_to_test_console("predicted ", end="")
                self.print_to_test_console(str(out), end="")
                self.print_to_test_console(" with confidence ", end="")
                self.print_to_test_console(str(confidence))
        elif event.keysym == 'b':
            print("B key pressed!")
            self.label_b.configure(fg_color="red", text_color="white")
            self.after(self.label_flash_duration_ms_entry.get(),
                       lambda: self.label_b.configure(fg_color="white", text_color="black"))
            if self.record_samples_checkbox.get():
                self.print_to_test_console("B key pressed - ", end="")
                channel_data = self.consume_samples()
                out, confidence = bci_ml.predict(self.test_model, channel_data)
                self.print_to_test_console("predicted ", end="")
                self.print_to_test_console(str(out), end="")
                self.print_to_test_console(" with confidence ", end="")
                self.print_to_test_console(str(confidence))
        elif event.keysym == 'space':
            print("SPACE key pressed!")
            if self.record_samples_checkbox.get():
                self.print_to_test_console("SPACE key pressed - ", end="")
                channel_data = self.consume_samples()
                out, confidence = bci_ml.predict(self.test_model, channel_data)
                self.print_to_test_console("predicted ", end="")
                self.print_to_test_console(str(out), end="")
                self.print_to_test_console(" with confidence ", end="")
                self.print_to_test_console(str(confidence))

    def load_test_model(self):
        model_path = self.model_to_test_entry.get()
        self.test_model = bci_ml.load_model(model_path)
        self.load_test_model_button.configure(text="Unload model", command=self.unload_test_model)
        self.print_to_test_console("Loaded model: ", end="")
        self.print_to_test_console(model_path)

    def unload_test_model(self):
        self.load_test_model_button.configure(text="Load model", command=self.load_test_model)
        self.test_model = None
        self.print_to_test_console("Unloaded model")

    def collect_data(self, data_folder):
        try:
            samples_data = self.consume_samples()
            np.save(os.path.join(data_folder,
                                 f"{int(time.time())}.npy"), np.array(samples_data))
        except LostError:
            messagebox.showerror('LSL config', f'Error: Stream "{self.bci_connection.stream_name}" has been '
                                               f'lost!')
            self.disconnect_lsl()
        except AttributeError:
            messagebox.showwarning('LSL config', f'Warning: Stream not connected. Can not record samples!')

    def create_train_and_validation_dirs(self):
        original_data_dir = self.original_data_folder_entry.get()
        result_data_dir = self.new_data_folder_entry.get()

        self.after(0, lambda: bci_ml.create_train_and_validation_dirs(original_data_dir, result_data_dir))

    def train_model(self):
        t = threading.Thread(target=lambda: bci_ml.train_and_evaluate(
            train_data_dir=self.train_data_folder_entry.get(),
            validation_data_dir=self.validation_data_folder_entry.get(),
            created_models_dir=self.created_models_folder_entry.get(),
            print_f=self.print_to_train_console))
        t.start()

    def connect_lsl(self):
        self.lsl_connect_button.configure(state="disabled", text="Connecting...")
        stream_name = self.lsl_stream_name_entry.get()
        if not stream_name:
            messagebox.showwarning('LSL Config', 'Warning: Stream name can not be empty!')
            self.lsl_connect_button.configure(state="normal", text="Connect")
            return

        self.bci_connection = bci_lsl.LslBciConnection(stream_name)
        self.bci_connections.add(self.bci_connection)
        t = threading.Thread(target=self.handle_resolve_stream)
        t.start()
        self.after(0, self.schedule_init_check)

    def handle_resolve_stream(self):
        try:
            self.bci_connection.resolve_stream()
        except IndexError:
            messagebox.showerror('LSL Config', f'Error: Could not find '
                                               f'\"{self.bci_connection.stream_name}\" LSL stream!')
            self.lsl_connect_button.configure(state="normal", text="Connect")
            self.bci_connection = None

    def disconnect_lsl(self):
        self.lsl_connect_button.configure(state="disabled", text="Disconnecting...")
        self.bci_connection.close_stream()
        messagebox.showinfo('LSL Config', f'Info: Disconnected from \"{self.bci_connection.stream_name}\" LSL stream!')
        self.bci_connections.discard(self.bci_connection)
        self.bci_connection = None
        self.lsl_connect_button.configure(state="normal", text="Connect", command=self.connect_lsl)

    def check_init_lsl_connection(self):
        if self.bci_connection.inlet is not None:
            messagebox.showinfo('LSL Config', f'Info: Connected to \"{self.bci_connection.stream_name}\" LSL stream!')
            self.lsl_connect_button.configure(state="normal", text="Disconnect", command=self.disconnect_lsl)
            self.schedule_regular_check(self.bci_connection)
        elif self.bci_connection.resolve_stream_in_process is True:
            self.schedule_init_check()

    def check_regular_lsl_connection(self, bci_connection):
        if bci_connection in self.bci_connections:
            bci_connection: bci_lsl.LslBciConnection
            try:
                bci_connection.get_sample()
                self.schedule_regular_check(bci_connection)
            except LostError:
                messagebox.showerror('LSL Config', f'Error: Stream transmission '
                                                   f'broke off \"{self.bci_connection.stream_name}\"')
                self.disconnect_lsl()

    def schedule_init_check(self):
        self.after(1000, self.check_init_lsl_connection)

    def schedule_regular_check(self, bci_connection):
        self.after(1000, self.check_regular_lsl_connection, bci_connection)

    def consume_samples(self):
        counter = 0
        list_of_samples = []
        while counter < int(self.sample_count_entry.get()):
            sample_list = []
            counter += 1
            for i in range(16):
                sample = self.bci_connection.get_sample()
                sample_list.append(sample[:60])
            list_of_samples.append(sample_list)
        return list_of_samples

    def print_to_console(self, console: customtkinter.CTkTextbox, text="", end="\n"):
        def insert_text():
            console.configure(state="normal")
            console.insert("end", text)
            console.insert("end", end)
            console.configure(state="disabled")

        self.after(0, lambda: insert_text())

    def print_to_train_console(self, text="", end="\n"):
        self.print_to_console(self.train_console, text, end)

    def print_to_test_console(self, text="", end="\n"):
        self.print_to_console(self.test_console, text, end)


def clear_console(console: customtkinter.CTkTextbox):
    console.configure(state="normal")
    console.delete("1.0", END)
    console.configure(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()
