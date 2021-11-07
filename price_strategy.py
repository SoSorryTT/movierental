from enum import Enum
from datetime import date


class PriceStrategy(Enum):
    """An enumeration for different kinds of movies and their behavior."""
    regular_price = {"price": lambda days: 2 if days <= 2 else 2 + (1.5 * (days - 2)),
                    "frp": lambda days: 1}
    new_release_price = {"price": lambda days: 3.0 * days,
                    "frp": lambda days: days}
    childrens_price = {"price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days - 3)),
                    "frp": lambda days: 1}

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        pricing = self.value["price"]   # the enum member's price formula
        return pricing(days)

    def points(self, days: int):
        """Return the rental points for a given number of days."""
        point = self.value["frp"]   # the enum member's point formula
        return point(days)

    @classmethod
    def for_movie(cls, movie):
        """Return price code that match that movie."""
        if movie.get_year() == str(date.today().year):
            return cls.new_release_price
        elif movie.is_genre("Children"):
            return cls.childrens_price
        else:
            return cls.regular_price