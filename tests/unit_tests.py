# -*- coding: utf-8 -*-
__author__ = 'Daniel'


import os, sys
sys.path.insert(0, os.path.abspath(__file__+"/../../src"))

from unittest import TestCase, main
from linqpy.list import List

a = List([2, 1, 3])
b = List()
c = List([1])
d = List([{"id": 1, "name": "bla"}, {"id": 1, "name": "ble"}, {"id": 2, "name": "ble"}])
e = List([{"age": 12}, {"age": 10}, {"age": 15}])


class Tests(TestCase):

    def test_all(self):
        self.assertTrue(a.all(lambda x: x < 5))
        self.assertFalse(a.all(lambda x: x < 2))

    def test_any(self):
        self.assertTrue(a.any())
        self.assertTrue(a.any(lambda x: x > 2))
        self.assertFalse(a.any(lambda x: x > 4))

    def test_avarage(self):
        self.assertEqual(a.avarage(), 2)
        self.assertEqual(d.avarage(lambda x: x["id"]), 1.33)

    def test_element_at(self):
        self.assertEqual(a.element_at(0), 2)

    def test_element_at_or_default(self):
        self.assertEqual(a.element_at_or_default(0), 2)
        self.assertEqual(a.element_at_or_default(4), None)

    def test_first(self):
        self.assertEqual(a.first(), 2)
        self.assertEqual(a.first(lambda x: x == 2), 2)

    def test_first_or_default(self):
        self.assertEqual(a.first_or_default(), 2)
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

        __l1 = List([1, 2, 3])
        __l2 = __l1.new_list()
        __l2.append(4)
        self.assertEqual(__l1, [1, 2, 3])
        self.assertEqual(__l2, [1, 2, 3, 4])

        __l3 = List([{"id": 1, "name": "bla"}, {"id": 2, "name": "ble"}])
        __l4 = __l3.new_list()
        __l4[0]["name"] = "bli"
        self.assertEqual(__l3[0]["name"], "bla")
        self.assertEqual(__l4[0]["name"], "bli")

    def test_max(self):
        self.assertEqual(a.max(), 3)
        self.assertEqual(d.max(lambda x: x["id"]), 2)

    def test_min(self):
        self.assertEqual(a.min(), 1)
        self.assertEqual(d.min(lambda x: x["id"]), 1)

    def test_order_by(self):
        self.assertEqual(a.order_by(), [1, 2, 3])
        self.assertEqual(e.order_by(lambda x: x["age"]), [{"age": 10}, {"age": 12}, {"age": 15}])

    def test_order_by_descending(self):
        self.assertEqual(a.order_by_descending(), [3, 2, 1])
        self.assertEqual(e.order_by_descending(lambda x: x["age"]), [{"age": 15}, {"age": 12}, {"age": 10}])

    def test_remove_where(self):
        __l1 = List([1, 2, 3, 4, 3])
        __l1.remove_where(lambda x: x == 3)
        self.assertEqual(__l1, [1, 2, 4])
        __l1.remove_where(lambda x: x == 5)
        self.assertEqual(__l1, [1, 2, 4])

    def test_select(self):
        self.assertEqual(a.select(lambda x: x), [2, 1, 3])
        self.assertEqual(d.select(lambda x: x["id"]), [1, 1, 2])

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

    def test_sum(self):
        self.assertEqual(a.sum(), 6)
        self.assertEqual(d.sum(lambda x: x["id"]), 4)

    def test_where(self):
        self.assertEqual(a.where(lambda x: x == 3), List([3]))
        self.assertEqual(a.where(lambda x: False), List())
        self.assertEqual(b.where(lambda x: True), List())
        self.assertEqual(d.where(lambda x: x["id"] == 1), [{"id": 1, "name": "bla"}, {"id": 1, "name": "ble"}])

if __name__ == '__main__':
    main()
