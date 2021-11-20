from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.sql.sqltypes import Date

Base = declarative_base()

class MedicineDetails(Base):
    __tablename__ = "Medicine Data"
    id = Column( Integer, primary_key=True,autoincrement= True)
    IdNo = Column(Integer)
    CustomerN = Column(String)
    MedicineN = Column(String)
    ManufeDate = Column(Date)
    PuraDate = Column(Date)
    MedicineStock = Column(String)
    ReturnDate = Column(Date)

if __name__ == "__main__":
    engine = create_engine("sqlite:///mydatabase.sqlite3")
    Base.metadata.create_all(engine)