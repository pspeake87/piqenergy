from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, Session, Relationship, SQLModel, create_engine, select
from typing import Annotated, Optional
import uuid
from datetime import datetime
from pydantic import BaseModel
import simulator

class FormData(BaseModel):
    num_scenarios: int
    scenario_type: str
    start: str
    end: str
    
class Simulation(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    num_scenarios: int
    data_points: list["DataPoint"] = Relationship(back_populates="simulation")

class DataPoint(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    scenario: int
    dt: datetime
    created_at: datetime = Field(default_factory=datetime.now)
    power_MW: float
    simulation_id: uuid.UUID = Field(foreign_key="simulation.id")
    simulation: Simulation = Relationship(back_populates="data_points")

sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/simulations")
def read_studies(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Simulation]:
    simulations = session.exec(select(Simulation).offset(offset).limit(limit)).all()
    return simulations

@app.get("/simulations/{simulation_id}")
def read_simulation(simulation_id: uuid.UUID, session: SessionDep) -> list[DataPoint]:
    data_points = session.exec(select(DataPoint).where(DataPoint.simulation_id == simulation_id)).all()
    if not data_points:
        raise HTTPException(status_code=404, detail="Simulation not found")
    return data_points

@app.post("/simulations")
async def create_simulation(data: FormData, session: SessionDep) -> Simulation:
    results = simulator.run_simulation(data.num_scenarios, data.scenario_type, datetime.fromisoformat(data.start), datetime.fromisoformat(data.end))

    simulation = Simulation(num_scenarios=data.num_scenarios)
    session.add(simulation)
    session.commit()
    session.refresh(simulation)

    for result in results:
        data_point = DataPoint(scenario=result["scenario"], dt=result["datetime"], power_MW=result["power_MW"], simulation_id=simulation.id)
        session.add(data_point)
    session.commit()

    return simulation