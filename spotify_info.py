#!/usr/bin/python

import sys, dbus

bus = dbus.SessionBus()
bus_name = 'org.mpris.MediaPlayer2.spotify'
object_path = '/org/mpris/MediaPlayer2'
interface_name = 'org.freedesktop.DBus.Properties'
dbus_interface = 'org.mpris.MediaPlayer2.Player'

artist_desc = 'xesam:artist'
title_desc = 'xesam:title'

try:
	spotify = bus.get_object(bus_name, object_path)
	iface = dbus.Interface(spotify, interface_name)
	props = iface.Get(dbus_interface, 'Metadata')

	if(props.has_key(artist_desc)):
		artist = props.get(artist_desc)[0]
	
	if(props.has_key('xesam:title')):
		title = props.get('xesam:title')

	message = '%s - %s' % (artist, title)
except dbus.exceptions.DBusException, e:
	message = 'SPOTIFY'

#sys.stdout.write(message)
print message
