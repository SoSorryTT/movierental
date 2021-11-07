from movie import *
from price_strategy import PriceStrategy
import logging


class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	
	def __init__(self, movie, days_rented): 
		"""
		Initialize a new movie rental object for
		a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented
		self.price_strategy = PriceStrategy.for_movie(self.movie)
		if not isinstance(self.price_strategy, PriceStrategy):
			log = logging.getLogger()
			log.error(f"Movie {self.movie.get_movie_title()} has unrecognized priceStrategy {self.movie}")

	def get_movie_title(self):
		"""Return the title movie."""
		return self.movie.get_title()

	def get_days_rented(self):
		"""Return rented day."""
		return self.days_rented

	def get_price(self):
		"""Calculate the price of each rent."""
		amount = self.price_strategy.price(self.get_days_rented())
		return amount

	def get_rental_point(self):
		"""Calculate the movie rental point."""
		rental_points = self.price_strategy.points(self.get_days_rented())
		return rental_points
