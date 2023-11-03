#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
"""

from datetime import datetime
from fabric import task


@task
def do_pack(c):
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    c.local('sudo mkdir -p versions')
    created = c.local('sudo tar -cvzf versions/{archive} web_static')
    if created:
        return archive
    else:
        return None
