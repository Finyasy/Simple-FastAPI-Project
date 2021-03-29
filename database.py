from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# database URI
SQLALCHEMY_DATABASE_URI = "sqlite:///article_app.db"

#echo-shortcut to setup SQLAlchemy logging/python standard logging
#create_engine an instance of engine that represents the core interface to the database
#connect_args is needed only for SQLite

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#To start talking to our database, the ORM's handle to the database is the Session

Base = declarative_base()

#Using the Declarative system, we can create classes that include directives to describe the actual database table they will map to A class using Declarative at a minimum needs a __tablename__ attribute and atleast one Column