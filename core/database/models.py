#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database.base import Base

SHORT_STRING = 30
LONG_STRING  = 200


class Queue(Base):
    __tablename__ = 'queue'

    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    name = Column(String(LONG_STRING), nullable=False)


class Schedule(Base):
    __tablename__ = 'schedule'

    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)


class Worklog(Base):
    __tablename__ = 'worklog'

    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    """
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    """