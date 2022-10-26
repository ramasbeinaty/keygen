from sqlalchemy.orm import Session
from db import models
from app import schemas

from typing import List

def get_count_ambassadors_without_link_repo(db: Session) -> int:
    count = db.query(models.Ambassadors.id).filter(models.Ambassadors.link.is_(None)).count()
    return count

def get_ambassador_by_link(db: Session, link: str) -> models.Ambassadors:
    return (
        db.query(models.Ambassadors)
        .filter(models.Ambassadors.link == link)
        .first()
    )

def insert_urls(db: Session, links:List[str]):
    ambassadors = db.query(models.Ambassadors).filter(models.Ambassadors.link.is_(None)).all()

    for index, row in enumerate(ambassadors):
        row.link = links[index]

    db.add_all(ambassadors)
    db.commit()

def insert_ambassadors_repo(db: Session, ambassadors_input: List):
    ambassadors = []

    for row in ambassadors_input:
        ambassadors.append(
            models.Ambassadors(
                name=row[0],
                email=row[1],
                link=None,
                points=0,
                is_valid=True,
            )
        )
    
    db.add_all(ambassadors)
    db.commit()