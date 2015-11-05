# -*- coding: utf-8 -*-
__author__ = 'Daniel'

from copy import deepcopy

class List(list):

    def all(self, func):
        return len([x for x in self if func(x)]) == len(self)

    def any(self, func=None):
        if not func:
            return len(self) > 0
        return self.first_or_default(func) is not None

    def avarage(self, func=None):
        if not func:
            return round(sum(self) / float(len(self)), 2)
        l = self.select(func)
        return round(sum(l) / float(len(l)), 2)

    def element_at(self, index):
        return self[index]

    def element_at_or_default(self, index):
        if index < 0 or index >= len(self):
            return None
        return self.element_at(index)

    def first(self, func=None):
        if not func:
            return self.element_at(0)
        return next((x for x in self if func(x)))

    def first_or_default(self, func=None):
        if not func:
            return self.element_at_or_default(0)
        return next((x for x in self if func(x)), None)

    def last(self, func=None):
        if not func:
            return self.element_at(len(self)-1)
        l = self.where(func)
        return l.element_at(len(l)-1)

    def last_or_default(self, func=None):
        if not func:
            return self.element_at_or_default(len(self)-1)
        l = self.where(func)
        return l.element_at_or_default(len(l)-1)

    def new_list(self):
        return List(deepcopy(self))

    def max(self, func=None):
        if not func:
            return max(self)
        return max(self.select(func))

    def min(self, func=None):
        if not func:
            return min(self)
        return min(self.select(func))

    def order_by(self, func=None):
        if not func:
            return sorted(self)
        return sorted(self, key=func)

    def order_by_descending(self, func=None):
        if not func:
            return sorted(self, reverse=True)
        return sorted(self, key=func, reverse=True)

    def select(self, func):
        return List([func(x) for x in self])

    def single(self, func=None):
        l = self.where(func) if func else self
        if len(l) != 1:
            raise Exception("None or more than one element at the list")
        return l.element_at(0)

    def single_or_default(self, func=None):
        l = self.where(func) if func else self
        if len(l) != 1:
             return None
        return l.element_at(0)

    def sum(self, func=None):
        if not func:
            return sum(self)
        return sum(self.select(func))

    def where(self, func):
        return List([x for x in self if func(x)])

