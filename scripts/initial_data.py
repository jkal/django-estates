#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Generate initial fixtures.
#

from random import choice, randrange, sample
from datetime import datetime

USERS = 1000
USERNAMES = [ 'user%s' % i for i in xrange(1, USERS + 1)]
CATEGORIES = 3
ASSETS = 3

userdata = """
- model: auth.user
  pk: %(pk)s
  fields:
    username: %(username)s
    email: %(username)s@example.com
    password: sha1$06c12$67aa4cc0f2e1ca5dc19fcc64af6a5a0e5052d8cb
"""

placedata = """
- model: places.Place
  pk: %(pk)s
  fields:
    address: %(address)s
    zipcode: %(zipcode)s
    city: "Πάτρα" 
    country: "Ελλάδα"
    latitude: %(latitude)s
    longitude: %(longitude)s
    submitter: %(user)s
    action: %(action)s
    price: %(price)s
    area: %(area)s
    year: %(year)s
    category: %(category)s
    pub_date: %(date)s
    published: True
    assets: %(assets)s
"""

def randlocation(filename='addresses.sample'):
    "Pick a random location from the sample file."
    return choice(open(filename, "r").readlines()).strip().split(',')

def users():
    userfile = open('users.yaml', 'w')
    for i, u in enumerate(USERNAMES, start=2):
        userdict = { 'pk' : i, 'username': u }
        userfile.write(userdata % userdict)

def places():
    placefile = open('places.yaml', 'w')
    totalplaces = 0
    for i, u in enumerate(USERNAMES, start=2):
        places_per_user = randrange(5, 30)
        for j in xrange(places_per_user):
            totalplaces += 1
            action = choice(['S', 'R'])
            place = randlocation()
            placedict = {
                'pk': totalplaces,
                'address' : place[0],
                'zipcode' : randrange(26200, 26500),
                'latitude' : place[1],
                'longitude' : place[2],
                'user' : i,
                'action' : action,
                'price' : randrange(200, 500) if action == 'R' else randrange(50000, 300000),
                'area' : randrange(60, 300),
                'year' : randrange(1980, 2006),
                'category' : randrange(1, CATEGORIES+1),
                'date' : datetime.now(),
                'assets': sample(range(1, ASSETS+1), randrange(0, ASSETS+1)) # (population, length)
            }
            placefile.write(placedata % placedict)

if __name__ == '__main__':
    import os
    print 'Generating initial users...'
    users()
    print 'Generating initial places...'
    places()
