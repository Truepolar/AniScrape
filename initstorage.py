from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, mapped_column, Mapped, DeclarativeBase
from decouple import config

url = config("url")

engine = create_engine(url, echo=True)


class Base(DeclarativeBase):
    pass


class UserData(Base):
    __tablename__ = "userdata"

    uid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    password: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    userl: Mapped["AnswerData"] = relationship(back_populates="answerl1")


class QuestionData(Base):
    __tablename__ = "questiondata"

    qid: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str]
    options: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)
    questionl: Mapped["AnswerData"] = relationship(back_populates="answerl2")


class AnswerData(Base):
    __tablename__ = "answerdata"
    aid: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('userdata.uid'))
    question_id: Mapped[int] = mapped_column(ForeignKey('questiondata.qid'))
    answer: Mapped[str]
    weight: Mapped[int] = mapped_column(nullable=True)
    answerl1: Mapped[list["UserData"]] = relationship(back_populates="userl")
    answerl2: Mapped[list["QuestionData"]] = relationship(back_populates="questionl")

Base.metadata.create_all(engine)
