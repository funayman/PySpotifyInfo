function spotify(){
	echo `python ~/.scripts/spotify_info.py`
}

alias splay='spotify_control.py pp'
alias spause='spotify_control.py pp'
alias snext='spotify_control.py next'
alias sprevious='spotify_control.py previous'
alias sstop='spotify_control.py stop'
