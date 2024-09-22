from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.band import Band  
from models.venue import Venue  
from models.concert import Concert  

#  this is the Database setup
engine = create_engine('sqlite:///concerts.db')  
Session = sessionmaker(bind=engine)
session = Session()

#  this is Querying all the bands
bands = session.query(Band).all()
print("Bands:")
for band in bands:
    print(f"ID: {band.id}, Name: {band.name}, Hometown: {band.hometown}")

#  this is Querying all  thevenues
venues = session.query(Venue).all()
print("\nVenues:")
for venue in venues:
    print(f"ID: {venue.id}, Title: {venue.title}, City: {venue.city}")

#  this is Querying all the  concerts
concerts = session.query(Concert).all()
print("\nConcerts:")
for concert in concerts:
    print(f"ID: {concert.id}, Band ID: {concert.band_id}, Venue ID: {concert.venue_id}, Date: {concert.date}")

session.close()
