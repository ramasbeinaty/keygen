from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.crud import create_urls, get_count_ambassadors_without_link, insert_ambassadors, output_to_csv
from db.base import get_db
from db.repo import insert_urls

api_router = APIRouter()

@api_router.get('/links')
def generate_links(db: Session=Depends(get_db)):
    count = get_count_ambassadors_without_link(db=db)
    print("INFO: number of ambassadors without link: ", count)

    urls = create_urls(number_of_urls=count, db=db)
    print("INFO: urls created - ", urls)

    output_to_csv(urls)
    insert_urls(db=db, links=urls)

@api_router.get('/amb')
def populate_ambassadors(db: Session=Depends(get_db)):
    insert_ambassadors(db=db)

@api_router.get('/all')
def populate_ambassadors_links(db: Session=Depends(get_db)):
    insert_ambassadors(db=db)
    generate_links(db=db)
