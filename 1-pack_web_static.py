#!/usr/bin/python3
# Fabric script that generates a .tgz archive
# from the contents of the web_static folder
from fabric.api import local
from time import strftime
from datetime import datetime


def do_pack():
    """Return the archive path if the archive has been correctly generated
    """
    time_format = strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -czvf versions/web_static_{:s}.tgz web_static/".format(
              time_format))
        return ("versions/web_static_{:s}.tgz".format(time_format))
    except Exception:
        return None
