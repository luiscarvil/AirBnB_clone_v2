#!/usr/bin/python3
"""script (based on the file 1-pack_web_static.py) using the function do_deploy
"""
from os.path import exists
from fabric.api import env, run, put
env.hosts = ['104.196.132.76', '35.243.198.29']


def do_deploy(archive_path):
    """ do_deploy function that distributes an archive to web servers
    """
    # print(archive_path)
    # file = archive_path.split("/")[-1]
    # print(file)
    # print(file.split(".")[0])
    if (exists(archive_path) is False):
        return False
    try:
        path = "/data/web_static/releases/"
        path_2 = "/data/web_static/current"
        file = archive_path.split("/")[-1]
        ext_file = file.split(".")[0]
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, ext_file))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, ext_file))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext_file))
        run('rm -rf {}{}/web_static'.format(path, ext_file))
        run('rm -rf {}'.format(path_2))
        run('ln -s {}{}/ {}'.format(path, ext_file, path_2))
        return True
    except Exception:
        return False
