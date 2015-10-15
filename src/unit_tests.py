# -*- coding: utf-8 -*-
__author__ = 'Daniel'


from unittest import TestCase, main

from linqpy import List

a = List([1, 2, 3])

class Tests(TestCase):

    def test_all(self):
        self.assertTrue(a.all(lambda x: x < 5))
        self.assertFalse(a.all(lambda x: x < 2))

    def test_any(self):
        self.assertTrue(a.any())
        self.assertTrue(a.any(lambda x: x > 2))
        self.assertFalse(a.any(lambda x: x > 4))

    def test_element_at(self):
        self.assertEqual(a.element_at(0), 1)

    def test_element_at_or_default(self):
        self.assertEqual(a.element_at_or_default(0), 1)
        self.assertEqual(a.element_at_or_default(4), None)

    def test_first(self):
        self.assertEqual(a.first(), 1)
        self.assertEqual(a.first(lambda x: x == 2), 2)

    def test_first_or_default(self):
        self.assertEqual(a.first_or_default(), 1)
        self.assertEqual(a.first_or_default(lambda x: x == 2), 2)
        self.assertEqual(a.first_or_default(lambda x: x == 5), None)

    def test_new_list(self):
        b = a.new_list()
        self.assertNotEqual(id(a), id(b), "New list not returning different obj")


if __name__ == '__main__':
    main()
