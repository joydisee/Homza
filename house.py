# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:26:41 2015

@author: ilyass
"""
import yaml, os
from . import Entity

class House(Entity):
    _collection = 'homza'
    _type = 'home'

    def __init__(self, name=None, latitude=None, longitude=None):
        self._id = 'house'
        already_saved = super(House, self).get()
        if already_saved:
            self = already_saved
        else:
            if name:
                self.name = name
            if longitude:
                self.longitude = longitude
            if latitude:
                self.latitude = latitude
            self.create()
    
    @classmethod
    def init(klass):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "data/house.yml"), 'r') as ymlfile:
            houseData = yaml.load(ymlfile)
            house = House(
                houseData['name'],
                houseData['latitude'],
                houseData['longitude']
            )
            return house