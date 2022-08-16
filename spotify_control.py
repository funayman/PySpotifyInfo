#!/usr/bin/env python3

import sys, dbus, argparse

# reload(sys).setdefaultencoding('utf8')

bus_name = 'org.mpris.MediaPlayer2.spotify'
object_path = '/org/mpris/MediaPlayer2'
interface_name = 'org.freedesktop.DBus.Properties'
dbus_interface = 'org.mpris.MediaPlayer2.Player'

d_values = {
	'artist' : 'xesam:artist',
	'title' : 'xesam:title',
	'album' : 'xesam:album'
}

def print_error():
    print('Function not available')

def change(dbus_object, action):
    actions = {
        'next' : dbus_object.Next,
        'previous' : dbus_object.Previous,
        'stop' : dbus_object.Stop,
        'pp' : dbus_object.PlayPause,
        'play' : dbus_object.Play,
        'pause' : dbus_object.Pause,
    }

    actions.get(action, print_error)()

parser = argparse.ArgumentParser(description="Spotify command line controller and song information displayer")
parser.add_argument(
		'-c',
		'--control',
		dest = 'change',
		default = None,
		choices = ['next', 'previous', 'stop', 'pp', 'play', 'pause'],
		help = 'Options to control spotify')
parser.add_argument(
		'-d',
		'--display',
		dest = 'display',
		default = None,
		nargs = '+',
		choices = d_values.keys(),
		help = 'What to display to stdout')
parser.add_argument(
		'-m',
		'--modifier',
		dest = 'mod',
		default = ' - ',
		help = 'What character seperates in the display. To include spaces wrap the character in quotes')

args = parser.parse_args()

try:
	bus = dbus.SessionBus()
	spotify = bus.get_object(bus_name, object_path)
	player = dbus.Interface(spotify, dbus_interface)
	iface = dbus.Interface(spotify, interface_name)
	props = iface.Get(dbus_interface, 'Metadata')

	if args.change:
		change(player, args.change.lower())

	if args.display:
		spotify_display = ''
		for d in args.display:
			if(d_values[d] in props):
				spotify_display += '{0}{1}'.format(props.get(d_values[d])[0] if (d == 'artist') else props.get(d_values[d]), args.mod)
		sys.stdout.write(spotify_display[:len(spotify_display) - len(args.mod)])

except dbus.exceptions.DBusException as e:
    print("SPOTIFY")
    sys.exit(1)
except NameError as e:
	sys.stderr.write("SPOTIFY")


