#!/usr/bin/python3
# Fabric script that generates a .tgz archive
# from the contents of the web_static folder
from fabric.api import local
from time import strftime
from datetime import datetime


def do_pack():
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".format(
              strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{:s}.tgz".format(
                strftime("%Y%m%d%H%M%S")))
    except Exception:
        return None
