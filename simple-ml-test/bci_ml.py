import shutil
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv1D, MaxPooling1D, BatchNormalization
import os
import random
import time

CASES = ["a", "b", "none"]
reshape = (-1, 16, 60)


def create_train_and_validation_dirs(original_data_dir, result_data_dir,
                                     training_dir="training_data", validation_dir="validation_data"):
    files = []
    for case in CASES:
        action_dir = os.path.join(original_data_dir, case)
        for root, _, files in os.walk(action_dir):
            np.random.shuffle(files)
        split_index = int(len(files) * 0.7)
        training = files[:split_index]
        validation = files[split_index:]

        os.makedirs(os.path.join(result_data_dir, training_dir, case), exist_ok=True)
        os.makedirs(os.path.join(result_data_dir, validation_dir, case), exist_ok=True)

        for training_file in training:
            shutil.copyfile(os.path.join(original_data_dir, case, training_file),
                            os.path.join(result_data_dir, training_dir, case, training_file))
        for validation_file in validation:
            shutil.copyfile(os.path.join(original_data_dir, case, validation_file),
                            os.path.join(result_data_dir, validation_dir, case, validation_file))


def create_data(starting_dir, print_f=None):
    if print_f is None:
        print_f = print
    training_data = {}
    for case in CASES:
        if case not in training_data:
            training_data[case] = []

        data_dir = os.path.join(starting_dir, case)
        for item in os.listdir(data_dir):
            data = np.load(os.path.join(data_dir, item))
            for item_data in data:
                training_data[case].append(item_data)

    lengths = [len(training_data[case]) for case in CASES]
    print_f(str(lengths))

    for case in CASES:
        np.random.shuffle(training_data[case])
        training_data[case] = training_data[case][:min(lengths)]

    lengths = [len(training_data[case]) for case in CASES]
    print_f(str(lengths))
    # creating X, y
    combined_data = []
    for case in CASES:
        for data in training_data[case]:
            if case == "a":
                combined_data.append([data, [1, 0, 0]])

            elif case == "b":
                combined_data.append([data, [0, 0, 1]])

            elif case == "none":
                combined_data.append([data, [0, 1, 0]])

    np.random.shuffle(combined_data)
    print_f("Length:", end="")
    print_f(str(len(combined_data)))
    return combined_data


def train_and_evaluate(train_data_dir, validation_data_dir, created_models_dir, print_f=None):
    if print_f is None:
        print_f = print
    print_f("Creating training data...")
    traindata = create_data(starting_dir=train_data_dir, print_f=print_f)
    train_x = []
    train_y = []
    for X, y in traindata:
        train_x.append(X)
        train_y.append(y)

    print_f("Creating testing data...")
    testdata = create_data(starting_dir=validation_data_dir, print_f=print_f)
    test_x = []
    test_y = []
    for X, y in testdata:
        test_x.append(X)
        test_y.append(y)

    print_f(len(train_x))
    print_f(len(test_x))

    print_f(np.array(train_x).shape)
    print_f(np.array(test_x).shape)
    train_x = np.array(train_x).reshape(reshape)
    test_x = np.array(test_x).reshape(reshape)

    train_y = np.array(train_y)
    test_y = np.array(test_y)

    model = Sequential()

    model.add(Conv1D(64, (3), input_shape=train_x.shape[1:]))
    model.add(Activation('relu'))

    model.add(Conv1D(64, (2)))
    model.add(Activation('relu'))
    model.add(MaxPooling1D(pool_size=(2)))

    model.add(Conv1D(64, (2)))
    model.add(Activation('relu'))
    model.add(MaxPooling1D(pool_size=(2)))

    model.add(Flatten())

    model.add(Dense(512))

    model.add(Dense(3))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    epochs = 10
    batch_size = 32
    for epoch in range(epochs):
        model.fit(train_x, train_y, batch_size=batch_size, epochs=1, validation_data=(test_x, test_y))
        score = model.evaluate(test_x, test_y, batch_size=batch_size)
        model_name = f"{round(score[1] * 100, 2)}-acc-64x3-batch-norm-{epoch}epoch-{int(time.time())}-loss-{round(score[0], 2)}.model"
        model.save(os.path.join(created_models_dir, model_name))
        print_f("Model saved:", end="")
        print_f(model_name)

    print_f("Process finished!")


def load_model(model_name):
    model = tf.keras.models.load_model(model_name)
    model.predict(np.zeros((32, 16, 60)).reshape(reshape))
    return model


def predict(model, channel_data):
    network_input = np.array(channel_data).reshape(reshape)
    out = model.predict(network_input)[0]
    return np.argmax(out), out[np.argmax(out)]
