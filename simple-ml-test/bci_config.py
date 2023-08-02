# General settings
import configparser
import os

label_flash_duration_ms = "label_flash_duration_ms"

# LSL config
lsl_stream_name = "lsl_stream_name"
collect_samples_after_duration_ms = "collect_samples_after_duration_ms"
sample_count = "sample_count"

# Collect data tab config
collect_data_folder_a = "collect_data_folder_a"
collect_data_folder_b = "collect_data_folder_b"
collect_data_folder_none = "collect_data_folder_none"

# Train tab config
train_data_folder_a = "train_data_folder_a"
train_data_folder_b = "train_data_folder_b"

# Train tab config
train_original_data_folder = "train_original_data_folder"
train_new_data_folder = "train_new_data_folder"

train_train_data_folder = "train_train_data_folder"
train_validation_data_folder = "train_validation_data_folder"
train_created_models_folder = "train_created_models_folder"

# Test only tab config
test_model_to_test = "test_model_to_test"


def get_ini_name_or_default():
    env_var = os.getenv('SIMPLE_ML_TEST_SETUP_INI')
    if env_var is None or len(env_var) == 0:
        return 'setup.ini'
    else:
        return env_var


def read_config():
    config_parser = configparser.ConfigParser()
    config_parser.read(get_ini_name_or_default())
    return {s: dict(config_parser.items(s)) for s in config_parser.sections()}


def save_config(config_dict):
    config_parser = configparser.ConfigParser()
    config_parser.add_section("config")
    for key in config_dict:
        config_parser.set("config", key, config_dict[key])
    with open(get_ini_name_or_default(), 'w') as configfile:
        config_parser.write(configfile)
