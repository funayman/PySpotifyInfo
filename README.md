You need to update your PATH to include the location of the python script
```bash
export PATH=$PATH:/path/to/PySpotifyInfo
```
```
python spotify_control.py -h
usage: spotify_control.py [-h] [-c {next,previous,stop,pp,play,pause}]
                          [-d {album,title,artist} [{album,title,artist} ...]]
                          [-m MOD]

Spotify command line controller and song information displayer

optional arguments:
  -h, --help            show this help message and exit
  -c {next,previous,stop,pp,play,pause}, --control {next,previous,stop,pp,play,pause}
                        Options to control spotify
  -d {album,title,artist} [{album,title,artist} ...], --display {album,title,artist} [{album,title,artist} ...]
                        What to display to stdout
  -m MOD, --modifier MOD
                        What character seperates in the display. To include
                        spaces wrap the character in quotes
```
