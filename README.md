# csv2tidal

A command-line tool to import individual **tracks** into **Tidal playlists** from a `.csv` file.  
✅ Supports playlist overwrite prompt  
✅ Adds only selected songs (not full albums)  
✅ Includes a progress bar for visual feedback

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

---

## 📄 CSV Format

Your `.csv` file must be UTF-8 encoded with **no header line** and each row in the format:

```csv
artist,track title,playlist name
```

✅ Example:

```csv
Clairo,4EVER,Favorite Songs
Red Hot Chili Peppers,Californication,Summer Jams
```

This will add **just those tracks** to the specified playlist.

---

## ▶️ Usage

Run the script like so:

```bash
python3 csv2tidal.py path/to/your.csv
```

On first use, you'll be prompted to log in to Tidal via a provided link. A `.session` file will be saved for future authenticated use.

---

## ⚠️ Playlist Overwrite Warning

This script will ask if you want to **delete all your existing playlists before import**. You can choose:

- **Y** to delete and start clean
- **N** to add to your existing playlists without deleting

---

## 🔐 Authentication Notes

The script creates a `.session` file to cache your Tidal login.  
Keep this file private — it contains your **access credentials**!

---

## 🙌 Credits

Originally inspired by:
- [RZetko's album importer](https://gist.github.com/RZetko/71801a20188e842ef03bed3b6d7a297f)
- [spotify_to_tidal](https://github.com/timrae/spotify_to_tidal) (login system)

Tweaks and enhancements by **[Ty!](https://github.com/TeeFynster)** — track-level support, error handling, and more!
