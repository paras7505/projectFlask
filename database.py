from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


DATABASE_URL = "sqlite:///database.db"


# engine = create_engine('mysql+pymysql://ParasPandey:Pandey75@ParasPandey.mysql.pythonanywhere-services.com/ParasPandey$database')   # engine is created 
engine = create_engine(DATABASE_URL)   # engine is created 
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine) # connection 
session = Session()