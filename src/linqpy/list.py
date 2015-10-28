# -*- coding: utf-8 -*-
__author__ = 'Daniel'


class List(list):

    def all(self, func):
        return len([x for x in self if func(x)]) == len(self)

    def any(self, func=None):
        if not func:
            return len(self) > 0
        return self.first_or_default(func) is not None

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
        return List(self)

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

    def where(self, func):
        return List([x for x in self if func(x)])
