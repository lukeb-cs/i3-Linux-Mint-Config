#!/bin/bash

options="Shutdown\nReboot\nLogout\nLock"
chosen=$(echo -e "$options" | rofi -dmenu -p "Power Menu")
case "$chosen" in
    Shutdown) shutdown now ;;
    Reboot) reboot ;;
    Logout) i3-msg exit ;;
    Lock) dm-tool lock ;;
esac
