from app.crud import create_urls, get_count_ambassadors_without_link, output_to_csv
from fastapi import FastAPI

from config import settings
from db.base import engine, Base

from app.controller import api_router


# create the app
app = FastAPI(title=settings.PROJECT_NAME)

# bind the database
Base.metadata.create_all(bind=engine)

# add the endpoints to the app
app.include_router(api_router)

# count = get_count_ambassadors_without_link(db)
# print("count of ambassadors without link: ", count)

# urls = create_urls(count)
# output_to_csv(urls)