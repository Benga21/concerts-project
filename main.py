from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.band import Band
from models.venue import Venue
from models.concert import Concert
from datetime import date

#  database engine
engine = create_engine('sqlite:///concerts.db')

# Seting up the database tables
Base.metadata.drop_all(engine)  
Base.metadata.create_all(engine)  

# Creates a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

#  list of bands is here
bands = [
    Band(name="BTS", hometown="Seoul"),
    Band(name="Blackpink", hometown="Seoul"),
    Band(name="EXO", hometown="Seoul"),
    Band(name="Stray Kids", hometown="Seoul"),
    Band(name="TWICE", hometown="Seoul"),
    Band(name="Red Velvet", hometown="Seoul"),
]

#  list of venues is here
venues = [
    Venue(title="Olympic Stadium", city="Seoul"),
    Venue(title="Jamsil Arena", city="Seoul"),
    Venue(title="Gocheok Sky Dome", city="Seoul"),
    Venue(title="Busan Asiad Main Stadium", city="Busan"),
    Venue(title="Daegu Stadium", city="Daegu"),
    Venue(title="Incheon Munhak Stadium", city="Incheon"),
]

# Add bands and venues to the session
session.add_all(bands)
session.add_all(venues)

# Commit the changes to the database
session.commit()

# Schedule concerts for each band at specific venues is done in this section
concert_dates = [
    (bands[0], venues[0], date(2024, 9, 21)),  
    (bands[1], venues[1], date(2024, 10, 1)),  
    (bands[2], venues[2], date(2024, 11, 15)), 
    (bands[3], venues[3], date(2024, 10, 25)), 
    (bands[4], venues[4], date(2024, 11, 5)),  
    (bands[5], venues[5], date(2024, 11, 15)), 
]

# Create concerts and add them to the session
for band, venue, concert_date in concert_dates:
    concert = band.play_in_venue(venue, concert_date, session)
    session.add(concert)

# Commit the concert changes to the database
session.commit()

# Query and print all concerts
all_concerts = session.query(Concert).all()

# Printing details for each concert is done here
for concert in all_concerts:
    print(concert.introduction())  #  here it Prints  the concert introduction
    print(concert.hometown_show())  #  here it prints if it is a hometown show

# here is where to Close the session
session.close()