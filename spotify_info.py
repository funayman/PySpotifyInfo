#!/usr/bin/python

import sys, dbus

reload(sys).setdefaultencoding('utf8')

bus_name = 'org.mpris.MediaPlayer2.spotify'
object_path = '/org/mpris/MediaPlayer2'
interface_name = 'org.freedesktop.DBus.Properties'
dbus_interface = 'org.mpris.MediaPlayer2.Player'

artist_desc = 'xesam:artist'
title_desc = 'xesam:title'
album_desc = 'xesam:album'

try:
	bus = dbus.SessionBus()
	spotify = bus.get_object(bus_name, object_path)
	iface = dbus.Interface(spotify, interface_name)
	props = iface.Get(dbus_interface, 'Metadata')

	if(props.has_key(artist_desc)):
		artist = props.get(artist_desc)[0]
	
	if(props.has_key(title_desc)):
		title = props.get(title_desc)

	message = '%s - %s' % (artist, title)
except Exception, e:
	message = 'SPOTIFY'

sys.stdout.write(message)
