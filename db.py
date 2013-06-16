import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from config import config

DBNAME = 'psiturk'
# DATABASE = config.get('Database Parameters', 'database_url')
# DATABASE = 'mysql://' + user + ':' + password + '@' + domain + ':' + port + '/' dbname
DATABASE = 'postgresql://' + os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'] + ':' + os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'] + '@' + os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'] + ':' + os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'] + '/'


engine = create_engine(DATABASE, echo=False)  # connect to db's server
conn = engine.connect()
conn.execute("commit")
try:
    conn.execute('SELECT 1')
    conn.execute("CREATE DATABASE " + DBNAME)  # create db
except:
    pass

# conn.execute("USE " + DBNAME)  # select new db

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    print "Initalizing db if necessary."
    Base.metadata.create_all(bind=engine)
