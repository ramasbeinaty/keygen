import string
import secrets
import csv

from sqlalchemy.orm import Session
from typing import List
from app import schemas

from db import models
from db.repo import get_count_ambassadors_without_link_repo, insert_ambassadors_repo
from . import keygen


def create_urls(number_of_urls: int, db: Session) -> str:
    keys = []

    for i in range(number_of_urls):
        keys.append(keygen.create_unique_random_key(db))
    
    return keys


def create_url(db: Session) -> str:
    return keygen.create_unique_random_key(db)


def get_count_ambassadors_without_link(db:Session) -> int:
    return get_count_ambassadors_without_link_repo(db=db)


def insert_ambassadors(db:Session):

    # read ambassadors from csv file
    with open(file="ambassadors.csv", mode="r") as csv_input:
        ambassadors = []
        reader = csv.reader(csv_input)

        row = next(reader)

        for row in enumerate(reader):
            ambassadors.append(row[1])

    # insert ambassadors into repo
    insert_ambassadors_repo(db=db, ambassadors_input=ambassadors)


def output_to_csv(values: List):
    with open(file='generated_urls.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['link'])

        for value in values:
            writer.writerow(['/'+str(value)+'/'])


    # combing both ambassadors and links csvs
    # with open(file="ambassadors.csv", mode="r") as csv_input:
    #     with open(file="ambassadors_with_urls.csv", mode="w") as csv_output:
    #         writer = csv.writer(csv_output, lineterminator='\n')
    #         reader = csv.reader(csv_input)


    #         all = []
    #         row = next(reader)
    #         all.append(["name", "email", "link"])

    #         for index, row in enumerate(reader):
    #             row.append(values[index])
    #             all.append(row)

    #         writer.writerows(all)
    

    