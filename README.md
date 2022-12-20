# csv2tidal

A command line tool for importing a list of Albums into your Tidal profile.

## Installation

Clone this git repository and then run:

```bash
python3 -m pip install -r requirements.txt
```

## CSV Format

the CSV file should be in format:

```csv
artist,title
```

The file must be UTF8 encoded and must not have a heading line. 

## Usage

To import your list of albums into you Tidal profile run:

```sh
python3 csv2tidal.py [file]
```

On first usage you will be asked to login into Tidal with the provided URL to register the API client. The session will be saved for future use, but when it expires you might be asked to login again.

__Important!__
The script is writing a file named `.session` after first login. Keep this file secret as it contains the session keys to login into your Tidal account. 


## Credits

The inspiration to write this script came from [RZetko](https://gist.github.com/RZetko/71801a20188e842ef03bed3b6d7a297f), login code was borrowed from [spotify_to_tidal](https://github.com/timrae/spotify_to_tidal).
