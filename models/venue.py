from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Venue(Base):
    __tablename__ = 'venues'  

    # Define the columns of the table
    id = Column(Integer, primary_key=True)  
    title = Column(String, nullable=False)   
    city = Column(String, nullable=False)     

    # Establishes a relationship with the Concert class
    concerts = relationship("Concert", back_populates="venue")

    def concert_on(self, date):
        """Return the concert at this venue on the given date."""
        # Look for a concert on the specified date
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        """Return the band that has performed most frequently at this venue."""
        from collections import Counter  
        # Count how many times each band has performed at this venue here
        band_counts = Counter([concert.band for concert in self.concerts])
        # Return the band with the highest count, or None if no concerts exist is happening here
        return band_counts.most_common(1)[0][0] if band_counts else None