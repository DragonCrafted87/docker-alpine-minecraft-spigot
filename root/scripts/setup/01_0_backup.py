#!/usr/bin/python3

# System Imports
from datetime import datetime
from pathlib import PurePath
from tarfile import open as tar_open

# Local Imports
from python_logger import create_logger #pylint: disable=import-error

def main():
  logger = create_logger(PurePath(__file__).stem)

  if not getenv('SPIGOT_SKIP_BACKUP', None):
    logger.info('Creating Backup')

    date_stamp = datetime.now().strftime("%G-%V-%u-%H-%M-%S")

    with tar_open(f'/mnt/minecraft/spigot-backup-{date_stamp}.tar.lzma', 'w:xz') as tar:
      tar.add('/mnt/minecraft/.')

if __name__ == "__main__":
  main()
