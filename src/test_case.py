# -*- coding: utf-8 -*-
__author__ = 'Daniel'


from unittest import TestCase, main

from linqpy import List


class Tests(TestCase):
    def test_new_list(self):
        a = List([1, 2, 3])
        b = a.new_list()
        self.assertNotEqual(id(a), id(b), "New list not returning different obj")


if __name__ == '__main__':
    main()
