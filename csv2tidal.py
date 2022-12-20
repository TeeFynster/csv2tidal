#!/usr/bin/env python3

import sys
import argparse
import csv
import pprint
from auth import open_tidal_session
import tidalapi

tidal_session = open_tidal_session()
if not tidal_session.check_login():
    sys.exit("Could not connect to Tidal")

csvfile = sys.argv[1]

print("Import %s" % csvfile)

favorites = tidalapi.Favorites(tidal_session, tidal_session.user.id)

with open(csvfile, encoding="utf8") as csvfile:
	rows = csv.reader(csvfile)
	for artist, album in rows:
		print('Processing {} - {}'.format(artist, album))
		
		albums_data = tidal_session.search('{} - {}'.format(artist, album))['albums']

		if len(albums_data) == 0:
			print('WARNING: No albums found for {} - {}, continuing\n'.format(artist, album))
			continue

		selection = 0

		album_to_add = albums_data[selection]
		favorites.add_album(album_to_add.id)