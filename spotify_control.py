#!/usr/bin/python

import sys, dbus, argparse

bus_name = 'org.mpris.MediaPlayer2.spotify'
object_path = '/org/mpris/MediaPlayer2'
interface_name = 'org.freedesktop.DBus.Properties'
dbus_interface = 'org.mpris.MediaPlayer2.Player'

def print_error():
    print 'Function not available'

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
		nargs = '*',
		choices = ['artist', 'title', 'album'],
		help = 'What to display to stdout')
args = parser.parse_args()

print args
try:
	bus = dbus.SessionBus()
	spotify = bus.get_object(bus_name, object_path)
	player = dbus.Interface(spotify, dbus_interface)

	if options.change:
		change(player, options.change.lower())
except dbus.exceptions.DBusException, e:
    print e
    sys.exit(1)


