class Config:
    DB_URL = f"postgresql+asyncpg://postgres:567234@postgres:5432/rest_app"
    ALEMBIC_DB_URL = f"postgresql+asyncpg://postgres:567234@localhost:5432/rest_app"


config = Config
