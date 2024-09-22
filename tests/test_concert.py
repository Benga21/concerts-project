import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.concert import Concert
from models.band import Band  
from models.venue import Venue  
class TestConcert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)  
        cls.Session = sessionmaker(bind=cls.engine) 

    def setUp(self):
        # Create a new session for each test
        self.session = self.Session()
        
        # Create test data for a band and a venue
        self.band = Band(name="BTS", hometown="Seoul")
        self.venue = Venue(title="Olympic Stadium", city="Seoul")
        
        # Add the band and venue to the session
        self.session.add(self.band)
        self.session.add(self.venue)
        self.session.commit()  
        
        # Create a concert for the band at the venue
        self.concert = Concert(band_id=self.band.id, venue_id=self.venue.id, date="2024-09-21")
        self.session.add(self.concert)
        self.session.commit()  

    def tearDown(self):
        self.session.close()

    def test_hometown_show(self):
        # Check if the concert is a hometown show here
        self.assertTrue(self.concert.hometown_show())  

    def test_introduction(self):
        expected_intro = "Hello Seoul!!!!! We are BTS and we're from Seoul"
        self.assertEqual(self.concert.introduction(), expected_intro)  # Verifys the introduction message

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()

if __name__ == '__main__':
    unittest.main()  # Run the test here