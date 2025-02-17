from sqlalchemy import create_engine , Column , Integer, String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker,mapped_column,Mapped,DeclarativeBase,Session
from decouple import config

class Ustore():
    url = config("url")

    engine = create_engine(url, echo=True)

    with Session(engine) as session:
        UserS  = (
            name = "",
            password = "",
            age = "",
            gender = "",
        )

