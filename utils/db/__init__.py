import logging
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, Session, Query


from .models import Base
from data.config import DB_NAME, DB_USER, DB_PASS, DB_HOST


url = URL.create(
    drivername="mysql+pymysql",
    database=DB_NAME,
    host=DB_HOST,
    username=DB_USER,
    password=DB_PASS,
)
engine = create_engine(url, pool_pre_ping=True, pool_timeout=15)

session = sessionmaker(engine, autoflush=True)

Base.metadata.create_all(engine)


def create_session() -> Session:
    return session()


def add(item):
    s = create_session()

    try:
        if isinstance(item, list):
            s.add_all(item)
        else:
            s.add(item)
        s.commit()
        s.refresh(item)
        return item
    except Exception as e:
        print(e)
        s.rollback()
        return False
    finally:
        s.close()


def delete(query: Query):
    s = create_session()
    query.session = s

    try:
        s.delete(query)
        s.commit()
        return True
    except Exception as e:
        logging.error(e)
        s.rollback()
        return False
    finally:
        s.close()


def updae(query: Query, update):
    s = create_session()
    query.session = s

    try:
        query.update(update)
        s.commit()
        return True
    except Exception as e:
        logging.error(e)
        s.rollback()
        return False
    finally:
        s.close()


def count(query: Query):
    s = create_session()
    query.session = s
    try:
        return query.count()
    except Exception as e:
        logging.error(e)
        s.rollback()
        return False
    finally:
        s.close()


def first(query: Query):
    s = create_session()
    query.session = s
    try:
        return query.first()
    except Exception as e:
        logging.error(e)
        s.rollback()
        return False
    finally:
        s.close()


def all(query: Query):
    s = create_session()
    query.session = s
    try:
        return query.all()
    except Exception as e:
        logging.error(e)
        s.rollback()
        return False
    finally:
        s.close()
