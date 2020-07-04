#!/bin/sh

cd /mnt/minecraft

exec java -Xms4G -Xmx4G -jar spigot-server.jar --forceUpgrade
