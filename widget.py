# -*- coding: utf-8 -*-

# widget manager
class WidgetManager:
    def __init__(self):
        self.widget2text = {}

    def add(self, widget, text = None):
        self.widget2text[widget] = text

    def get(self, widget = None):
        return self.widget2text.get(widget)

    def get_all(self):
        return self.widget2text

    def clear(self):
        self.widget2text = {}