"""PostgreSQL + SQLAlchemy: guardar y recuperar tasaciones."""
import os
from datetime import datetime, timezone
from sqlalchemy import create_engine, Integer, String, DateTime, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////tmp/carvalue_demo.db")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

class Base(DeclarativeBase):
    pass

class Tasacion(Base):
    __tablename__ = "tasaciones"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    creada_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    manufacturer: Mapped[str] = mapped_column(String(70))
    year: Mapped[int] = mapped_column(Integer)
    odometer: Mapped[int] = mapped_column(Integer)
    fuel: Mapped[str] = mapped_column(String(30))
    type: Mapped[str] = mapped_column(String(50))
    transmission: Mapped[str] = mapped_column(String(30))
    condition: Mapped[str] = mapped_column(String(30))
    justificacion: Mapped[str] = mapped_column(String(400))
    price_prediction: Mapped[float] = mapped_column(Float)
    vision_source: Mapped[str] = mapped_column(String(20))


def crear_tablas():
    Base.metadata.create_all(engine)


def guardar_tasacion(registro: dict) -> int:
    """TODO A5: persistir una tasación y devolver su id."""
    # TODO A5: Session(engine), add(), commit(), refresh() y devuelve id
    raise NotImplementedError("Completa guardar_tasacion")


def obtener_ultimas_tasaciones(limite: int = 10):
    """TODO A6: SELECT de últimas tasaciones (descendente)."""
    # TODO A6: select(Tasacion).order_by(...).limit(limite)
    raise NotImplementedError("Completa obtener_ultimas_tasaciones")
