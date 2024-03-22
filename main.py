from fastapi import FastAPI

from models import LineItemUpdate

app = FastAPI()

@app.post("/line_item")
async def bulk_update(line_item_update: LineItemUpdate):

    if len(line_item_update.lineItems) == 0:
        return {"message": "No line items to update"}
    if len(line_item_update.lineItems) > 1000:
        return {"message": "Too many line items to update"}


    return {"message": "Line items updated"}
