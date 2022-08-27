#!/bin/sh

exec < /dev/tty
oldstty=$(stty -g)
stty raw -echo min 0
tput u7 > /dev/tty
sleep 1
IFS=';' read -r row col
stty $oldstty

row=$(expr $(expr substr $row 3 99) - 1)        # Strip leading escape off
col=$(expr ${col%R} - 1)                        # Strip trailing 'R' off

echo $col
echo $row
