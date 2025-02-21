from contextlib import contextmanager
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@contextmanager
def get_session():
    session = None
    try:
        url = config('url')
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
    finally:
        if session is not None:
            session.close()


