function spotify(){
	echo `python ~/.scripts/spotify_info.py`
}

alias spotify-play='spotify_control.py play'
alias spotify-pause='spotify_control.py pause'
alias spotify-next='spotify_control.py next'
alias spotify-previous='spotify_control.py previous'
alias spotify-stop='spotify_control.py stop'
alias spotify-pp='spotify_control.py pp'
