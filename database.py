from datetime import datetime
from numpy import string_
from numpy.lib.type_check import imag
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Date

Base = declarative_base()

class MedicineDetails(Base):
    __tablename__ = "Medicine Data"
    id    = Column( Integer, primary_key=True,autoincrement= True )
    IdNo  = Column(Integer)
    CustomerN = Column(String)
    MedicineN = Column(String)
    ManufeDate = Column(Date)
    PuraDate = Column(Date)
    MedicineStock = Column(String)
    ReturnDate = Column(Date)

class UserDeatails(Base):
    __tablename__ = "User Details"
    id = Column(Integer, primary_key=True, autoincrement= True)
    Names = column(String)
    Username = Column(String)
    Email_id = Column(String)
    Password = Column(String)
   

if __name__ == "__main__":
    engine = create_engine("sqlite:///mydatabase.sqlite3")
    Base.metadata.create_all(engine)