import string
import secrets
from sqlalchemy.orm import Session

from db import repo

def create_random_key(length: int = 5) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_random_key(db: Session) -> str:
    key = create_random_key()
    while repo.get_ambassador_by_link(db, key):
        key = create_random_key()
    return key