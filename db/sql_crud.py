import sqlalchemy as sa
from sqlalchemy.sql import select, text

def add_pagination(query, offset, limit):
    # Increases the limit parameter to 5000
    return query.offset(offset).limit(5000)