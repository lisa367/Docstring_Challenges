from unittest import TestCase, main

from main import add, divide


class TestCalculatrice(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(5, 10), 15)

    def test_with_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")

    def test_add_with_two_booleans(self):
        self.assertEqual(add(True, False), 1)
        self.assertEqual(add(True, True), 2)
        self.assertEqual(add(False, False), 0)

    def test_add_with_two_none(self):
        with self.assertRaises(TypeError):
            add(None, None)

    def test_divide_two_numbers(self):
        self.assertEqual(divide(10, 2), 5)


# main()

# python -m unittest tests.py --verbose
# python -m unittest

# python3 -m venv .env
# source .env/bin/activate
# pip install coverage
# coverage run -m unittest tests
# coverage html
