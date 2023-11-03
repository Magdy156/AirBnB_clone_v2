#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.89.109.87', '100.25.190.21']


def do_deploy(archivePath):
    """Distributes an archive to the web servers"""
    if exists(archivePath) is False:
        return False
    try:
        file = archivePath.split("/")[-1]
        no_ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archivePath, '/tmp/')
        run(f'mkdir -p {path}{no_ext}/')
        run(f'tar -xzf /tmp/{file} -C {path}{no_ext}/')
        run(f'rm /tmp/{file}')
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run(f'rm -rf {path}{no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {path}{no_ext}/ /data/web_static/current')
        return True
    except:
        return False
