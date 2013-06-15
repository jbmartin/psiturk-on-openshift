import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from config import config

DBNAME = 'psiturk'
# DATABASE = config.get('Database Parameters', 'database_url')
# DATABASE = 'mysql://' + user + ':' + password + '@' + domain + ':' + port + '/' dbname
DATABASE = 'mysql://' + os.environ['OPENSHIFT_MYSQL_DB_USERNAME'] + ':' + os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'] + '@' + os.environ['OPENSHIFT_MYSQL_DB_HOST'] + ':' + os.environ['OPENSHIFT_MYSQL_DB_PORT'] + '/' + DBNAME


engine = create_engine(DATABASE, echo=False)  # connect to db's server
engine.execute("CREATE DATABASE " + DBNAME)  # create db
engine.execute("USE " + DBNAME)  # select new db

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    print "Initalizing db if necessary."
    Base.metadata.create_all(bind=engine)
