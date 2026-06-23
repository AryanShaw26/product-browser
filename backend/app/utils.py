import base64
import json

def encode_cursor(updated_at, product_id):
    data = {
        "updated_at": updated_at.isoformat(),
        "id": product_id
    }

    return base64.b64encode(
        json.dumps(data).encode()
    ).decode()

def decode_cursor(cursor):
    return json.loads(
        base64.b64decode(cursor).decode()
    )