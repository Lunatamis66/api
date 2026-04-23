from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Base, engine, get_db
from app.models import User
from app.schemas import UserOut


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(title="API", lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/db/ping")
async def db_ping(db: AsyncSession = Depends(get_db)):
    """Verifica se a conexão com PostgreSQL/TimescaleDB está ativa."""
    result = await db.execute(text("SELECT 1"))
    row = result.scalar_one()
    version = await db.execute(text("SELECT version()"))
    pg_version = version.scalar_one()
    return {"ok": row == 1, "server_version": pg_version}


@app.get("/users", response_model=list[UserOut])
async def list_users(db: AsyncSession = Depends(get_db)):
    users = await db.execute(select(User).order_by(User.id))
    return users.scalars().all()
