from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import *
from database import get_db
from models import *
import uvicorn


app = FastAPI()

@app.post("/ship/insert")
def create(details: ShipModel, db: Session = Depends(get_db)):
    to_create = Ship(
        name=details.name,
        route_from_city=details.route_from_city,
    route_from_port=details.route_from_port,
    route_from_coordinates_n=details.route_from_coordinates_n,
    route_from_coordinates_e=details.route_from_coordinates_e,
    route_from_time=details.route_from_time,
    route_to_city=details.route_to_city,
    route_to_port=details.route_to_city,
    route_to_coordinates_n=details.route_to_coordinates_n,
    route_to_coordinates_e=details.route_to_coordinates_e,
    route_to_time=details.route_to_time,
    history_1_n=details.history_1_n,
    history_1_e=details.history_1_e,
    history_2_n=details.history_2_n,
    history_2_e=details.history_2_e,
    history_3_n=details.history_3_n,
    history_3_e=details.history_3_e,
    size_length=details.size_length,
    size_width=details.size_width,
    directiondegree=details.directiondegree,
    speed=details.speed,
    status=details.status,
    coordinates_n=details.coordinates_n,
    coordinates_e=details.coordinates_e
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }

@app.get("/ships/")
def get_ships(db: Session = Depends(get_db)):
    return db.query(Ship).all()

@app.get("/ships/get/by/id")
def get_ship_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Ship).filter(Ship.id == id).first()

@app.delete("/ships/delete")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Ship).filter(Ship.id == id).delete()
    db.commit()
    return { "success": True }

@app.get("/table/")
def get_table(db: Session = Depends(get_db)):
    return db.query(FinalShips).all()

@app.post("/table/new/trek")
def post_table(details: FinalShipsModel, db: Session = Depends(get_db)):
    to_create = FinalShips(
        ship=details.ship,
        id_request=details.id_request,
        ledocol=details.ledocol,
        date_begin=details.date_begin,
        date_end=details.date_end,
        point_begin=details.point_begin,
        point_end=details.point_end,
        is_ledocol=details.is_ledocol
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True
    }

@app.get("/requests/")
def get_table(db: Session = Depends(get_db)):
    return db.query(Requests).all()

@app.post("/requests/new/")
def post_table(details: RequestsModel, db: Session = Depends(get_db)):
    to_create = Requests(
        name=details.name,
    imo=details.imo,
    led_class=details.led_class,
    speed=details.speed,
    date_begin=details.date_begin,
    date_end=details.date_end,
    point_begin=details.point_begin,
    point_end=details.point_end,
    is_ledocol=details.is_ledocol
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8000)