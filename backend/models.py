from sqlalchemy import Integer, String, Float, Boolean
from sqlalchemy.sql.schema import Column
from database import Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)


class Requests(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    imo = Column(Integer)
    led_class = Column(String(255))
    speed = Column(Integer)
    date_begin = Column(String(255))
    date_end = Column(String(255))
    point_begin = Column(String(255))
    point_end = Column(String(255))
    is_ledocol = Column(Boolean)


class FinalShips(Base):
    __tablename__ = 'final_ships'

    id = Column(Integer, primary_key=True)
    ship = Column(Integer)
    id_request = Column(Integer)
    ledocol = Column(Integer)
    date_begin = Column(String(255))
    date_end = Column(String(255))
    point_begin = Column(String(255))
    point_end = Column(String(255))
    is_ledocol = Column(Boolean)


class Ship(Base):
    __tablename__ = 'ships'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    route_from_city = Column(String(255))
    route_from_port = Column(String(255))
    route_from_coordinates_n = Column(Float)
    route_from_coordinates_e = Column(Float)
    route_from_time = Column(String(255))
    route_to_city = Column(String(255))
    route_to_port = Column(String(255))
    route_to_coordinates_n = Column(Float)
    route_to_coordinates_e = Column(Float)
    route_to_time = Column(String(255))
    history_1_n = Column(Float)
    history_1_e = Column(Float)
    history_2_n = Column(Float)
    history_2_e = Column(Float)
    history_3_n = Column(Float)
    history_3_e = Column(Float)
    size_length = Column(Integer)
    size_width = Column(Integer)
    directiondegree = Column(Integer)
    speed = Column(Float)
    status = Column(String(255))
    coordinates_n = Column(Float)
    coordinates_e = Column(Float)
