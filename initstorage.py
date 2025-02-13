


from sqlalchemy import create_engine , Column , Integer, String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker,mapped_column,Mapped,relationships
from decouple import config

url=config("url")

engine = create_engine(url)

Base = declarative_base()

class UserS(Base):
    __tablename__ = "userdata"

    uid: Mapped[int] = mapped_column(primary_key=True)
    answer_uid: Mapped[int] = mapped_column(ForeignKey("answerdata.user_id"))
    name: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    userl: Mapped["AnswerS"] = relationship(back_populates="answerl1")

class QuestionS(Base):
    __tablename__ = "questiondata"

    qid: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("answerdata.question_id"))
    question: Mapped[str]
    options: Mapped[str]
    checks: Mapped[str]
    questionl: Mapped["AnswerS"] = relationship(back_populates="answerl2")

class AnswerS(Base):
    __tablename__ = "answerdata"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(primary_key=True)
    answer: Mapped[str]
    weight: Mapped[int]
    answerl1: Mapped[list["UserS"]] = relationship(back_populates="userl")
    answerl2: Mapped[list["QuestionS"]] = relationship(back_populates="questionl")



Base.metadata.create_all(engine)



