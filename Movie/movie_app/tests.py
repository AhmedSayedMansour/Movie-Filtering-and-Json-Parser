from django.test import TestCase
from movie_app.MovieFilter import MovieFilter

class MovieTests(TestCase):

    def test_search_for_a_movie(self):
        """Test searching for a movie"""
        path = 'Movie-Dataset-Latest (1).zip'

        filter = MovieFilter(path)

        rows = filter.search(title = None, release_date=None, overview="love", popularity=None, vote_average=8.7, vote_count=None)
        self.assertEqual(rows, [0, 1])

        rows = filter.search(title = None, release_date=None, overview="blood", popularity=None, vote_average=5.0, vote_count=None)
        self.assertEqual(rows, [9169, 9165])

        rows = filter.search(title = 'My Brother Chases Dinosaurs', release_date=None, overview="love", popularity=None, vote_average=7.0, vote_count=None)
        self.assertEqual(rows, [3200])

        rows = filter.search(title = "The Shawshank Redemption", release_date=None, overview="love", popularity=None, vote_average=8.7, vote_count=None)
        self.assertEqual(rows, [1])

        rows = filter.search(title = None, release_date='9/23/1994', overview=None, popularity=None, vote_average=None, vote_count=None)
        self.assertEqual(rows, [1])
