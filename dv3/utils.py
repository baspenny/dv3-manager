from googleapiclient.discovery import Resource
from models import LineItemUpdate


def update_line_item_status(service: Resource, advertiser_id: str, line_item_id: str, new_status):
    """
    Update the status of a DV360 line item.

    Args:
        service: The authenticated DV360 service object.
        advertiser_id: The ID of the advertiser that owns the line item.
        line_item_id: The ID of the line item to update.
        new_status: The new status for the line item ("ACTIVE" | "PAUSED" | "ENTITY_STATUS_DRAFT").

    Returns:
        The response from the DV360 API.
    """
    # Prepare the update body with the new status
    update_body = {
        "entityStatus": new_status
    }

    # Execute the PATCH request to update the line item
    request = service.advertisers().lineItems().patch(
        advertiserId=advertiser_id,
        lineItemId=line_item_id,
        updateMask="entityStatus",
        body=update_body
    )
    response = request.execute()

    return response


def update_line_items_status(service: Resource, advertiser_id: str, line_item_ids: LineItemUpdate, new_status):
    """
    Update the status of multiple DV360 line items.

    Args:
        service: The authenticated DV360 service object.
        advertiser_id: The ID of the advertiser that owns the line items.
        line_item_ids: A list of line item IDs to update.
        new_status: The new status for the line items ("ACTIVE" | "PAUSED" | "ENTITY_STATUS_DRAFT").
    Returns:
        The response from the DV360 API.
    """
    # print(LineItemUpdate.lineItems[0].entityStatus)
    pass
