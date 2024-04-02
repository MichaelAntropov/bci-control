from typing import List

from sqlalchemy import String, ForeignKey, select
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


class Base(DeclarativeBase):
    pass


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    anonymized_name: Mapped[str] = mapped_column(String(50))

    recordings: Mapped[List["Recording"]] = relationship(primaryjoin="Subject.id == Recording.subject_id")

    def __repr__(self) -> str:
        return f"Subject(id={self.id!r}, name={self.name!r}, anonymized_name={self.anonymized_name!r})"

    @staticmethod
    def find_subject_by_name(subject_name: str, session: Session = None):
        return session.scalars(select(Subject).where(Subject.name == subject_name)).one_or_none()


class Recording(Base):
    __tablename__ = "recordings"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    set_id: Mapped[int]
    set_number: Mapped[int]
    parameters: Mapped[dict] = mapped_column(JSON)
    xdf_file_path: Mapped[str] = mapped_column(String(255))

    subject: Mapped["Subject"] = relationship(back_populates="recordings")

    def __repr__(self) -> str:
        return (f"Recording(id={self.id!r}, subject_id={self.subject_id!r}, set_id={self.set_id!r}, "
                f"set_number={self.set_number!r}, parameters={self.parameters!r}, xdf_file_path={self.xdf_file_path!r})")

    @staticmethod
    def find_recording_by_subject_and_set_and_parameters(subject_id, set_id, set_number,
                                                         parameters, session: Session = None):
        return session.scalars(select(Recording).where(
            (Recording.subject_id == subject_id)
            & (Recording.set_id == set_id)
            & (Recording.set_number == set_number)
            & (Recording.parameters == parameters))).one_or_none()


class ProcessParameters(Base):
    __tablename__ = "process_parameters"

    id: Mapped[int] = mapped_column(primary_key=True)
    parameters: Mapped[dict] = mapped_column(JSON)
    description: Mapped[str] = mapped_column(String(500))
    meta: Mapped[dict] = mapped_column(JSON)

    def __repr__(self) -> str:
        return f"ProcessParameters(id={self.id!r}, parameters={self.parameters!r})"

    @staticmethod
    def find_proc_params_by_params(params: dict, session: Session = None):
        return session.scalars(select(ProcessParameters).where(ProcessParameters.parameters == params)).one_or_none()


class ProcessResult(Base):
    __tablename__ = "process_results"

    id: Mapped[int] = mapped_column(primary_key=True)
    parameters_id: Mapped[int] = mapped_column(ForeignKey("process_parameters.id"))
    recording_id: Mapped[int] = mapped_column(ForeignKey("recordings.id"))
    results: Mapped[dict] = mapped_column(JSON)
    notes: Mapped[str] = mapped_column(String(500))
    meta: Mapped[dict] = mapped_column(JSON)

    def __repr__(self) -> str:
        return (f"ProcessResult(id={self.id!r}, parameters_id={self.parameters_id!r}, "
                f"recording_id={self.recording_id!r}), results={self.results!r}")

    @staticmethod
    def find_proc_result_by_params_id_and_recording_id(params_id: int, recording_id: int, session: Session = None):
        return session.scalars(select(ProcessResult).where(
            (ProcessResult.parameters_id == params_id)
            & (ProcessResult.recording_id == recording_id))).one_or_none()
