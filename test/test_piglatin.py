import unittest
from piglatin import PigLatin
from error import *


class TestPigLatin(unittest.TestCase):

    def test_hello_world(self):
        obj = PigLatin("hello world")
        self.assertEqual(obj.get_phrase(),"hello world")

    def test_empty_phrase(self):
        obj = PigLatin("")
        self.assertEqual(obj.translate(),"nil")

    def test_vowels_and_consonant(self):
        obj = PigLatin("any")
        self.assertEqual(obj.translate(), "anynay")
        obj = PigLatin("apple")
        self.assertEqual(obj.translate(), "appleyay")
        obj = PigLatin("ask")
        self.assertEqual(obj.translate(), "askay")
        obj = PigLatin("apple")
        self.assertFalse(obj.translate()=="apple")
        self.assertNotEqual(obj.translate(), "ask")

    def test_word_starting_with_consonant(self):
        obj = PigLatin("hello")
        self.assertEqual(obj.translate(), "ellohay")

    def test_word_starting_with_consonants(self):
        obj = PigLatin("known")
        self.assertEqual(obj.translate(), "ownknay")

    def test_str_with_more_words(self):
        obj = PigLatin("hello world")
        self.assertEqual(obj.translate(), "ellohay orldway")
        obj = PigLatin("well-being")
        self.assertEqual(obj.translate(), "ellway-eingbay")
        obj = PigLatin("hello world!")
        self.assertEqual(obj.translate(), "ellohay orldway!")

    def test_error(self):
        obj = PigLatin("hello world!")
        self.assertRaises(PigLatinError, obj.translate)

    def test_word_starting_with_consonant(self):
        obj = PigLatin("hello")
        self.assertEqual(obj.translate(), "ellohay")



    def test_something(self):
        pass




