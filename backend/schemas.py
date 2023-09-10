from pydantic import BaseModel


class CreateJobRequest(BaseModel):
    title: str
    description: str


class FinalShipsModel(BaseModel):
    ship: int
    id_request: int
    ledocol: int
    date_begin: str
    date_end: str
    point_begin: str
    point_end: str
    is_ledocol: bool


class RequestsModel(BaseModel):
    name: str
    imo: int
    led_class: str
    speed: int
    date_begin: str
    date_end: str
    point_begin: str
    point_end: str
    is_ledocol: bool



class ShipModel(BaseModel):
    name: str
    route_from_city: str
    route_from_port: str
    route_from_coordinates_n: float
    route_from_coordinates_e: float
    route_from_time: str
    route_to_city: str
    route_to_port: str
    route_to_coordinates_n: float
    route_to_coordinates_e: float
    route_to_time: str
    history_1_n: float
    history_1_e: float
    history_2_n: float
    history_2_e: float
    history_3_n: float
    history_3_e: float
    size_length: int
    size_width: int
    directiondegree: int
    speed: float
    status: str
    coordinates_n: float
    coordinates_e: float


