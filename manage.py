#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drirfinder.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drfinder.settings")
>>>>>>> e34d721d43c41fa1deb6930ebc2c5fcc40766145

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
