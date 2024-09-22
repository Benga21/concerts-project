import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.band import Band
from models.venue import Venue
from models.concert import Concert

class TestVenue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)  
        cls.Session = sessionmaker(bind=cls.engine)  

    def setUp(self):
        # Creates a new session for each test
        self.session = self.Session()
        
        # Creates test data for bands and venue
        self.band = Band(name="BTS", hometown="Seoul")
        self.rockers = Band(name="Blackpink", hometown="Seoul")
        self.venue = Venue(title="Olympium Stadium", city="Seoul")

        # Adds bands and venue to the session
        self.session.add(self.band)
        self.session.add(self.rockers)
        self.session.add(self.venue)
        self.session.commit()  

    def tearDown(self):
        self.session.rollback()
        self.session.close()  

    def test_concert_on(self):
        # this Schedule a concert for the band at the venue
        self.band.play_in_venue(self.venue, "2024-09-21", self.session)
        
        #  this Checks if the concert is scheduled on that date
        concert = self.venue.concert_on("2024-09-21")
        self.assertIsNotNone(concert)  
        self.assertEqual(concert.date, "2024-09-21")  

    def test_most_frequent_band(self):
        for _ in range(5):
            self.rockers.play_in_venue(self.venue, "2024-09-21", self.session)
        self.band.play_in_venue(self.venue, "2024-09-22", self.session)
        self.session.commit()  

        # Checks which band has performed the most at the venue
        frequent_band = self.venue.most_frequent_band()
        self.assertEqual(frequent_band.name, "Blackpink")  

    @classmethod
    def tearDownClass(cls):
        # Dispose of the engine after all tests are done
        cls.engine.dispose()

if __name__ == '__main__':
    unittest.main()  # Run the tests