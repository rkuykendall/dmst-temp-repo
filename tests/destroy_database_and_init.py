#!/usr/bin/env python

from iris.article import Article, Base, engine
from iris.iris import iris

def destroy_db():
    """
    Destroy all data and tables in db, specified in the config.py file.
    """
    Base.metadata.drop_all(engine)

def create_db():
    """
    Create the database in db, specified in the config.py file.
    """
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    destroy_db()
    create_db()