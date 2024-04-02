create table if not exists subjects
(
    id integer not null primary key autoincrement,
    name varchar(50) not null constraint subjects_unique_1 unique,
    anonymized_name varchar(50)
);

create table if not exists recordings
(
    id integer not null primary key autoincrement,
    subject_id integer not null,
    set_id integer not null,
    set_number integer not null,
    parameters json not null,
    xdf_file_path varchar(255),
    constraint recordings_unique_1 unique (subject_id, set_id, set_number, parameters)
);

create table if not exists process_parameters
(
    id integer not null primary key autoincrement,
    parameters json not null,
    description varchar(500),
    meta json,
    constraint process_parameters_unique_1 unique (parameters)
);

create table if not exists process_results
(
    id integer not null primary key autoincrement,
    parameters_id integer not null,
    recording_id integer not null,
    results json not null,
    notes varchar(500),
    meta json,
    constraint process_results_unique_1 unique (parameters_id, recording_id)
);
