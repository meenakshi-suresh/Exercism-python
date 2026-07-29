"""Calculate a person's age on different planets based on a given age in seconds."""
class SpaceAge:
    """Represent an age in seconds and convert it to planetary years."""
    planet_years = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }
    EARTH_YEARS = 60 * 60 * 24 * 365.25

    def __init__(self, seconds):
        """Initialize the object with an age expressed in seconds."""
        self.seconds = seconds


    def age_on(self,planet):
        """Return the age in years on the specified planet."""
        divisor = self.EARTH_YEARS * self.planet_years[planet]
        return round(self.seconds /divisor, 2)


    def on_mercury(self):
        """Return the age in Mercury years."""
        return self.age_on('mercury')


    def on_venus(self):
        """Return the age in Venus years."""
        return self.age_on('venus')


    def on_earth(self):
        """Return the age in Earth years."""
        return self.age_on('earth')


    def on_mars(self):
        """Return the age in Mars years."""
        return self.age_on('mars')

    def on_jupiter(self):
        """Return the age in Jupiter years."""
        return self.age_on('jupiter')


    def on_saturn(self):
        """Return the age in Saturn years."""
        return self.age_on('saturn')


    def on_uranus(self):
        """Return the age in Uranus years."""
        return self.age_on('uranus')


    def on_neptune(self):
        """Return the age in Neptune years."""
        return self.age_on('neptune')
