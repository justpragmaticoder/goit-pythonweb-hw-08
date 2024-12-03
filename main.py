import logging
from fastapi import FastAPI

from src.api import contacts, utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(utils.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting FastAPI application...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
