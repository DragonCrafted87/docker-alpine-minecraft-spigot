#!/usr/bin/python3

# System Imports
from os import getenv
from os import system
from pathlib import Path
from urllib.request import urlretrieve

# Local Imports
from python_logger import create_logger #pylint: disable=import-error

def main():
  logger = create_logger(Path(__file__).stem)

  if not getenv('SPIGOT_SKIP_BUILD', None):
    logger.info('Downloading BuildTools')
    url = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar'
    urlretrieve(url, '/minecraft/BuildTools.jar')

    spigot_version = getenv('SPIGOT_VERSION', None)

    logger.info(f'Running Build Tools for version {spigot_version}')
    system(f'cd /minecraft && java -jar BuildTools.jar --rev {spigot_version}')

    system('rm -f /mnt/minecraft/spigot-server.jar')
    system('mv /minecraft/spigot*.jar /mnt/minecraft/spigot-server.jar')

    system('rm -rf /minecraft/*')

  if not Path("/mnt/minecraft/start_spigot.sh").is_file():
    system('mv /scripts/start_spigot.sh /mnt/minecraft/start_spigot.sh')

if __name__ == "__main__":
  main()
