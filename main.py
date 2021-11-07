# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, PriceStrategy
from rental import Rental
from customer import Customer
from .movie_catalog import MovieCatalog


def make_movies():
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("Mulan"),
        catalog.get_movie("No Time To Die"),
        catalog.get_movie("CitizenFour"),
        catalog.get_movie("Son of Saul")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    catalog = Moviecatalog()
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
