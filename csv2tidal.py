#!/usr/bin/env python3

import sys
import csv
from auth import open_tidal_session
import tidalapi
from tqdm import tqdm  # ✅ progress bar

# Connect to Tidal
tidal_session = open_tidal_session()
if not tidal_session.check_login():
    sys.exit("Could not connect to Tidal")

csvfile = sys.argv[1]
print("Importing from %s" % csvfile)

user = tidal_session.user
existing_playlists = {pl.name: pl for pl in user.playlists()}
created_playlists = {}

# ✅ Count total rows to show % progress
with open(csvfile, encoding="utf8") as f:
    total_rows = sum(1 for _ in f)

with open(csvfile, encoding="utf8") as csvfile:
    rows = csv.reader(csvfile)
    for artist, album, playlist_name in tqdm(rows, total=total_rows, desc="Importing albums", leave=True):
        tqdm.write(f"\nProcessing: {artist} - {album} -> Playlist: {playlist_name}")

        # Search for album
        search_result = tidal_session.search(f"{artist} - {album}")
        albums = search_result['albums']
        if not albums:
            tqdm.write(f"WARNING: Album not found: {artist} - {album}")
            continue

        album = albums[0]
        tracks = list(album.tracks())
        if not tracks:
            tqdm.write(f"WARNING: No tracks found for album: {artist} - {album}")
            continue

        # Get or create playlist
        if playlist_name not in created_playlists:
            if playlist_name in existing_playlists:
                playlist = existing_playlists[playlist_name]
                tqdm.write(f"Using existing playlist: {playlist_name}")
            else:
                playlist = user.create_playlist(playlist_name, f"Imported from CSV: {playlist_name}")
                tqdm.write(f"Created new playlist: {playlist_name}")
            created_playlists[playlist_name] = playlist

        # Add tracks to playlist safely
        playlist = created_playlists[playlist_name]
        tqdm.write(f"Adding {len(tracks)} tracks from '{album.name}' to playlist '{playlist.name}'")

        track_ids = [track.id for track in tracks if track.id is not None]

        if not track_ids:
            tqdm.write(f"WARNING: No valid track IDs for '{album.name}' — skipping")
            continue

        try:
            playlist.add(track_ids)
        except Exception as e:
            tqdm.write(f"ERROR adding tracks from '{album.name}' to playlist '{playlist.name}': {e}")
            with open("failed_to_add.txt", "a", encoding="utf8") as log:
                log.write(f"{artist} - {album} (Playlist: {playlist_name})\n")