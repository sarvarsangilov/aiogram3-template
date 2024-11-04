import datetime
from typing import List
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Date,
    Boolean,
    ForeignKey,
    TIMESTAMP,
    BigInteger
    
)

from sqlalchemy.orm import declarative_base, declared_attr, relationship, Mapped

Base = declarative_base()


class BaseClass(Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(+5), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(+5),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    class Config:
        from_attributes = True

class User(BaseClass):
    user_id = Column(BigInteger(), primary_key=True,unique=True)
    user_name = Column(Text())
    full_name = Column(Text())
    is_user = Column(Boolean(), default=True)
