function spotify(){
	echo `python ~/.scripts/spotify_control.py -d artist title -m " -- "`
}

alias splay='spotify_control.py -c pp'
alias spause='spotify_control.py -c pp'
alias snext='spotify_control.py -c next'
alias sprevious='spotify_control.py -c previous'
alias sstop='spotify_control.py -c stop'
