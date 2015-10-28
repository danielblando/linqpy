# -*- coding: utf-8 -*-
__author__ = 'Daniel'


import os, sys
sys.path.insert(0, os.path.abspath(__file__+"/../../src"))

from unittest import TestCase, main
from linqpy.list import List

a = List([1, 2, 3])
b = List()
c = List([1])
d = List([{"id": 1, "name": "bla"}, {"id": 1, "name": "ble"}])


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

    def test_last(self):
        self.assertEqual(a.last(), 3)
        self.assertRaises(IndexError, b.last)
        self.assertEqual(a.last(lambda x: x == 2), 2)
        self.assertRaises(IndexError, a.last, lambda x: x > 5)
        self.assertEqual(d.last(lambda x: x["id"] == 1)["name"], "ble")

    def test_last_or_default(self):
        self.assertEqual(a.last_or_default(), 3)
        self.assertEqual(b.last_or_default(), None)
        self.assertEqual(a.last_or_default(lambda x: x == 2), 2)
        self.assertEqual(a.last_or_default(lambda x: x > 5), None)
        self.assertEqual(d.last(lambda x: x["id"] == 1)["name"], "ble")

    def test_new_list(self):
        __new_list = a.new_list()
        self.assertNotEqual(id(a), id(__new_list), "New list not returning different obj")

    def test_single(self):
        self.assertRaises(Exception, a.single)
        self.assertRaises(Exception, b.single)
        self.assertEqual(c.single(), 1)
        self.assertEqual(a.single(lambda x: x == 3), 3)
        self.assertRaises(Exception, d.single, lambda x: x["id"] == 1)

    def test_single_or_default(self):
        self.assertEqual(a.single_or_default(), None)
        self.assertEqual(b.single_or_default(), None)
        self.assertEqual(c.single_or_default(), 1)
        self.assertEqual(a.single_or_default(lambda x: x == 3), 3)
        self.assertEqual(d.single_or_default(lambda x: x["id"] == 1), None)

    def test_where(self):
        self.assertEqual(a.where(lambda x: x == 3), List([3]))
        self.assertEqual(a.where(lambda x: False), List())
        self.assertEqual(b.where(lambda x: True), List())
        self.assertEqual(d.where(lambda x: x["id"] == 1), d)

if __name__ == '__main__':
    main()
