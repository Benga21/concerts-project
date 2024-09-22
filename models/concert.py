from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Concert(Base):
    __tablename__ = 'concerts'

    # Defines the columns of the table here
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)
    date = Column(String, nullable=False)

    # Establishes relationships with Band and Venue classes
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    def introduction(self):
        """
        Returns a string introducing the concert with a message.
        This message includes the city, band name, and hometown.
        """
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def hometown_show(self):
        """
        Returns a message showing if the concert is in the band's hometown.
        If the concert is in the same city as the band's hometown, it confirms it.
        """
        if self.band.hometown == self.venue.city:
            return f"{self.band.hometown} band performing!"  # It's a hometown show
        else:
            return "This is not a hometown show."  # Not a hometown show is shown here