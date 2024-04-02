from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session

import random

from src.db_entities import Recording, ProcessParameters, ProcessResult

database_url = "sqlite:///../../database/data/ssvep-db.sqlite"
database_recordings_folder = r"../../database/data/recordings"

engine = create_engine(database_url)


def run_process_and_get_results_for_recording(recording: Recording) -> (dict, str, dict):
    recording_parameters: dict = recording.parameters

    result = {"result_1": random.random(),
              "result_2": random.random()}
    notes = f"Some notes. Amount of keys in recording: {len(recording_parameters.keys())}"
    meta = {"meta_key_1": "some_metadata", "key_count": len(recording_parameters.keys())}
    return result, notes, meta


def get_recordings(session: Session) -> list[Recording]:
    stmt = select(Recording).where(
        (Recording.parameters['duration_s'].as_float() == 6.0)
        & (Recording.parameters['frequencies'].as_string() == '["9","16","13"]')
    )

    return list(session.scalars(stmt).all())


def run_example_process():
    with Session(engine) as session, session.begin():

        process_parameters = ProcessParameters.find_proc_params_by_params(parameters, session=session)
        if process_parameters is None:
            process_parameters = ProcessParameters(parameters=parameters)
            session.add(process_parameters)
            session.flush()

        recordings = get_recordings(session)
        for recording in recordings:

            process_result = ProcessResult.find_proc_result_by_params_id_and_recording_id(
                process_parameters.id, recording.id, session=session)
            if process_result is None:
                process_result = ProcessResult()
                process_result.recording_id = recording.id
                process_result.parameters_id = process_parameters.id

            result, notes, meta = run_process_and_get_results_for_recording(recording)

            process_result.results = result
            process_result.notes = notes
            process_result.meta = meta

            session.add(process_result)

        session.flush()


if __name__ == "__main__":
    parameters = {
        "example_parameter_1": "some_value",
        "example_parameter_2": "some_value_2"
    }
    run_example_process()
