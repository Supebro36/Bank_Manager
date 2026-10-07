import uuid
from .accounts import Account
from .transactions import Transaction

def generate_id():
    parts=str(uuid.uuid4()).split("-")
    return f"{parts[0]}**{parts[1]}{parts[2]}"

_all_ = ["Account","Transaction","generate_id"]