import os
import re
import shutil

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.db_entities import Subject, Recording

database_url = "sqlite:///../database/data/ssvep-db.sqlite"
raw_recordings_folder = r"C:\Users\Hizenberges\Desktop\recordings"
database_recordings_folder = r"../database/data/recordings"

engine = create_engine(database_url)

session_id_to_parameters_regex = r"^(?P<set_id>\d+)_(?P<set_number>\d+)__(?P<frequencies>\w+)_(?P<duration_s>\d+)s$"


def create_subject_and_flush(subject_name: str, session: Session = None) -> Subject:
    subject: Subject = Subject(name=subject_name)
    session.add(subject)
    session.flush()

    subject.anonymized_name = 'subject_' + str(subject.id)
    session.add(subject)
    session.flush()
    return subject


def create_recording_and_flush(session: Session, subject_id: int,
                               set_id: int, set_number: int,
                               parameters: dict, xdf_path: str) -> Recording:
    recording: Recording = Recording(subject_id=subject_id, set_id=set_id,
                                     set_number=set_number, parameters=parameters, xdf_file_path=xdf_path)

    session.add(recording)
    session.flush()

    return recording


def construct_parameters_json_dict(parameters: dict) -> dict:
    result = {'frequencies': parameters['frequencies'],
              'duration_s': parameters['duration_s']}

    return result


def parse_recordings_to_db():
    xdf_files: [tuple] = []

    abs_raw_recordings_folder = os.path.abspath(raw_recordings_folder)
    for root, dirs, files in os.walk(abs_raw_recordings_folder):
        for file in files:
            if file.endswith(".xdf"):
                xdf_files.append((root, file))

    recordings = []
    # Get rid of raw_recordings_folder prefix and get subject_id and recording set, number and parameters
    for file in xdf_files:
        full_file_path = os.path.join(file[0], file[1])
        split_str = file[0][len(abs_raw_recordings_folder + os.sep):].split(os.sep)

        subject_name = split_str[0]
        parameters = re.match(session_id_to_parameters_regex, split_str[1]).groupdict()

        parsed_parameters = {'set_id': int(parameters['set_id']),
                             'set_number': int(parameters['set_number']),
                             'frequencies': parameters['frequencies'].split('_'),
                             'duration_s': float(parameters['duration_s'])}

        recordings.append((subject_name, parsed_parameters, full_file_path))

    # Write everything to DB + files
    with Session(engine) as session, session.begin():
        for recording in recordings:
            subject_name, all_parameters, full_file_path = recording

            subject = Subject.find_subject_by_name(subject_name, session=session)
            if subject is None:
                subject = create_subject_and_flush(subject_name, session)

            parameters = construct_parameters_json_dict(all_parameters)
            recording = Recording.find_recording_by_subject_and_set_and_parameters(
                subject.id, all_parameters['set_id'], all_parameters['set_number'], parameters, session=session)

            if recording is None:
                frequencies_str: str = "_".join(parameters['frequencies'])
                duration_str: str = str(parameters['duration_s']).replace(".", "-")

                new_file_name: str = "{}__{}_{}__{}__{}s.xdf".format(
                    subject.anonymized_name, all_parameters['set_id'], all_parameters['set_number'],
                    frequencies_str, duration_str
                )

                new_file_path = os.path.join(database_recordings_folder, new_file_name)
                create_recording_and_flush(session, subject.id, all_parameters['set_id'],
                                           all_parameters['set_number'], parameters, new_file_name)

                shutil.copy(full_file_path, new_file_path)


if __name__ == '__main__':
    parse_recordings_to_db()
