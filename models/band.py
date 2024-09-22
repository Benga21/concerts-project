from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.concert import Concert

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship("Concert", back_populates="band")

    def play_in_venue(self, venue, date, session):
        """
        Schedule a concert for the band at a specific venue on a given date.
        This method creates a concert and adds it to the session.
        """
        concert = Concert(band=self, venue=venue, date=date)
        session.add(concert)  # Adds the concert to the session
        session.commit()  # Saves the changes to the database
        return concert  # Returns the created concert

    def all_introductions(self):
        """
        Generates a list of introduction messages for all concerts the band has performed.
        Each message includes the city of the concert, the band's name, and their hometown.
        """
        introductions = [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self.concerts
        ]
        return introductions
