import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.band import Band
from models.venue import Venue
from models.concert import Concert
from models.base import Base  
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

class TestBand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)

    def setUp(self):
        self.session = Session()
        self.band = Band(name="BTS", hometown="Seoul")
        self.venue = Venue(title="Olympium Stadium", city="Seoul")

        self.session.add(self.band)
        self.session.add(self.venue)
        self.session.commit()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_play_in_venue(self):
        self.band.play_in_venue(self.venue, "2024-09-21", self.session)
        concert = self.session.query(Concert).filter_by(band_id=self.band.id).first()
        self.assertIsNotNone(concert)
        self.assertEqual(concert.date, "2024-09-21")

    def test_all_introductions(self):
        self.band.play_in_venue(self.venue, "2024-09-21", self.session)
        introductions = self.band.all_introductions()
        self.assertEqual(len(introductions), 1)
        self.assertIn("Hello Seoul!!!!! We are BTS and we're from Seoul", introductions)  

if __name__ == '__main__':
    unittest.main()
