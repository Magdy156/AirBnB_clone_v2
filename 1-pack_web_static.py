#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('sudo mkdir -p versions')
    created = local(f'sudo tar -cvzf versions/{archive} web_static')
    if created:
        return archive
    else:
        return None
