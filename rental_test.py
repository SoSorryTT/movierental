import unittest
from rental import Rental
from movie import Movie
from price_strategy import PriceStrategy


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("No Time To Die", "2021", ["Adventure"])
		self.regular_movie = Movie("CitizenFour", "1996", ["Action", "Sci-Fi", "Thriller"])
		self.childrens_movie = Movie("The Legend of Sarila", "2013", ["Adventure", "Animation", "Children"])

	def test_movie_attributes(self):
		"""Trivial test to catch refactoring errors or change in API of Movie"""
		self.assertEqual("No Time To Die", self.new_movie.get_title())  # New Movie
		self.assertEqual("2021", self.new_movie.get_year())
		self.assertEqual(PriceStrategy.new_release_price, PriceStrategy.for_movie(self.new_movie))
		self.assertEqual(True, self.new_movie.is_genre("Adventure"))
		self.assertEqual("CitizenFour", self.regular_movie.get_title())  # Regular Movie
		self.assertEqual("1996", self.regular_movie.get_year())
		self.assertEqual(PriceStrategy.regular_price, PriceStrategy.for_movie(self.regular_movie))
		self.assertEqual(True, self.regular_movie.is_genre("Sci-Fi"))
		self.assertEqual("The Legend of Sarila", self.childrens_movie.get_title())  # Children Movie
		self.assertEqual("2013", self.childrens_movie.get_year())
		self.assertEqual(PriceStrategy.childrens_price, PriceStrategy.for_movie(self.childrens_movie))
		self.assertEqual(True, self.childrens_movie.is_genre("Children"))

	def test_rental_price(self):
		"""Test rental price."""
		rental = Rental(self.new_movie, 1)  # Test for movie
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 8)
		self.assertEqual(rental.get_price(), 24)
		rental = Rental(self.regular_movie, 1)  # Test for regular
		self.assertEqual(rental.get_price(), 2)
		rental = Rental(self.regular_movie, 8)
		self.assertEqual(rental.get_price(), 11)
		rental = Rental(self.childrens_movie, 1)  # Test for child
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 8)
		self.assertEqual(rental.get_price(), 9)

	def test_rental_points(self):
		"""Test for the retal point."""
		rental = Rental(self.new_movie, 1)  # For new movie
		self.assertEqual(rental.get_rental_point(), 1)
		rental = Rental(self.new_movie, 8)
		self.assertEqual(rental.get_rental_point(), 8)
		rental = Rental(self.regular_movie, 1)  # for regular
		self.assertEqual(rental.get_rental_point(), 1)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_rental_point(), 1)
		rental = Rental(self.childrens_movie, 2)  # for children
		self.assertEqual(rental.get_rental_point(), 1)
		rental = Rental(self.childrens_movie, 10)
		self.assertEqual(rental.get_rental_point(), 1)
