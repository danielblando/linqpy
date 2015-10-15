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
        if len(self) < index:
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

    def new_list(self):
        return List(self)

