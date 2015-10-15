# -*- coding: utf-8 -*-
__author__ = 'Daniel'


from unittest import TestCase, main

from linqpy import List


class Tests(TestCase):

    def test_all(self):
        a = List([1, 2, 3])
        self.assertTrue(a.all(lambda x: x < 5))
        self.assertFalse(a.all(lambda x: x < 2))

    def test_any(self):
        a = List([1, 2, 3])
        self.assertTrue(a.any(lambda x: x > 2))
        self.assertFalse(a.any(lambda x: x > 4))

    def test_new_list(self):
        a = List([1, 2, 3])
        b = a.new_list()
        self.assertNotEqual(id(a), id(b), "New list not returning different obj")


if __name__ == '__main__':
    main()
