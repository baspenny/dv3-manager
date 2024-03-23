from fastapi import FastAPI

from dv3.line_item_models import LineItemUpdate

from custom_logger import get_logger

logger = get_logger()

app = FastAPI()


@app.get("/")
async def test_logs():
    logger.info("test_logs")
    logger.warning("test_logs", extra={"custom": "data"})
    logger.error("test_logs", extra={"custom": "data"})
    logger.exception("test_logs", extra={"custom": "data"}, exc_info="kapot")
    return {"message": "Hello World"}


@app.post("/line_item")
async def bulk_update(line_item_update: LineItemUpdate):
    # logger.info("bulk_update", extra=line_item_update.dict())
    if len(line_item_update.lineItems) == 0:
        return {"message": "No line items to update"}
    if len(line_item_update.lineItems) > 1000:
        return {"message": "Too many line items to update"}

    return {"message": "Line items updated"}
