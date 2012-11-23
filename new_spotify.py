#!/usr/bin/python

import sys, dbus

def print_error():
	print 'Function not available'

def change(dbus_object, action):
	actions = {
		'next' : dbus_object.Next,
		'previous' : dbus_object.Previous,
		'stop' : dbus_object.Stop,
		'pp' : dbus_object.PlayPause,
	}

	if action == 'exit':
		sys.exit(0)

	actions.get(action, print_error)()

bus = dbus.SessionBus()
bus_name = 'org.mpris.MediaPlayer2.spotify'
object_path = '/org/mpris/MediaPlayer2'
interface_name = 'org.freedesktop.DBus.Properties'
dbus_interface = 'org.mpris.MediaPlayer2.Player'

try:
	spotify = bus.get_object(bus_name, object_path)
	iface = dbus.Interface(spotify, interface_name)
	player = dbus.Interface(spotify, dbus_interface)
	props = iface.Get(dbus_interface, 'Metadata')

	while(True):
		s = raw_input()
		change(player, s)

except dbus.exceptions.DBusException, e:
	print e
	sys.exit(1)


