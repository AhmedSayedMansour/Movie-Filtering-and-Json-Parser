from django.test import TestCase
from parser_app.parsetojson import CSVParser
import os

class MovieTests(TestCase):

    def test_parse_csv_to_json(self):
        """Test searching for a movie"""
        path = 'Movie-Dataset-Latest (1).csv'

        parser = CSVParser()
        parser.parse_to_json("Movie-Dataset-Latest (1).csv", 'output.json')

        self.assertTrue(os.path.isfile('output.json'))
