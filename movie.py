class Movie:
	"""
	A movie available for rent.
	"""
	
	def __init__(self, title, year, genre: list):
		# Initialize a new movie. 
		self.__title = title
		self.__year = year
		self.__genre = genre

	def is_genre(self, same_genre):
		"""Return True if the genre of the movie was in movie genre."""
		return same_genre in self.__genre
	
	def get_title(self):
		"""Return movie title."""
		return self.__title

	def get_year(self):
		"""Return movie year."""
		return self.__year
	
	def __str__(self):
		return self.__title
