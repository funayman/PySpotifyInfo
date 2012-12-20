#!/usr/bin/python

import sys, dbus, argparse

bus = dbus.SessionBus()
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

parser = argparse.ArgumentParser(description="Controls Spotify via the command line.")
parser.add_argument("command", type=str, help="")
args = parser.parse_args()

try:
    spotify = bus.get_object(bus_name, object_path)
    player = dbus.Interface(spotify, dbus_interface)

    change(player, args.command)

except dbus.exceptions.DBusException, e:
    print e
    sys.exit(1)


