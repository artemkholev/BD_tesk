from sqlalchemy import create_engine, Column, Integer, Float, DateTime, String, select, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

def SQLAlchemyActions(query):
  engine = create_engine('postgresql://name:password@localhost:5432/name_bd', echo=True)
  Base = declarative_base()
  class TaxiYellow(Base):
    __tablename__ = 'taxi_yellow' 
    vendorid = Column(Integer, primary_key=True)
    tpep_pickup_datetime = Column(DateTime)
    tpep_dropoff_datetime = Column(DateTime)
    passenger_count = Column(Integer)
    trip_distance = Column(Float)
    ratecodeid = Column(Integer)
    store_and_fwd_flag = Column(String(10))
    pulocationid = Column(String(1000))
    dolocationid = Column(String(1000))
    payment_type = Column(Integer)
    fare_amount = Column(Float)
    extra = Column(Float)
    mta_tax = Column(Float)
    tip_amount = Column(Float)
    tolls_amount = Column(Float)
    improvement_surcharge = Column(Float)
    total_amount = Column(Float)
    congestion_surcharge = Column(Float)
    airport_fee = Column(Float)
  

  # Base.metadata.create_all(engine)
  Session = sessionmaker(bind=engine)
  session = Session()

  if (query == 1):
    answer = session.query(TaxiYellow.vendorid, func.count(TaxiYellow.vendorid)).group_by(TaxiYellow.vendorid).all()
    print(answer)
  elif (query == 2):
    answer = session.query(TaxiYellow.passenger_count, func.avg(TaxiYellow.total_amount)).group_by(TaxiYellow.passenger_count).all()
    print(answer)
  elif (query == 3):
    answer = session.query(TaxiYellow.passenger_count, func.extract('year', TaxiYellow.tpep_pickup_datetime), func.count(TaxiYellow.passenger_count)).group_by(TaxiYellow.passenger_count, func.extract('year', TaxiYellow.tpep_pickup_datetime)).all()
    print(answer)
  elif (query == 4):
    answer = session.query(TaxiYellow.passenger_count, func.extract('year', TaxiYellow.tpep_pickup_datetime), func.round(TaxiYellow.trip_distance), func.count(TaxiYellow.passenger_count)).group_by(TaxiYellow.passenger_count, func.extract('year', TaxiYellow.tpep_pickup_datetime), func.round(TaxiYellow.trip_distance)).order_by(func.extract('year', TaxiYellow.tpep_pickup_datetime), func.count(TaxiYellow.passenger_count).desc()).all()
    # print(answer)
    for elem in answer: 
      print (elem)
  session.close()
  try:
    with engine.connect() as conn:
        print(" Successfully Connected to the database")
  except Exception as ex:
      print(" Sorry Could not connect to the database")