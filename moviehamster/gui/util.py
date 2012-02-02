##  Hamster - Nice and friendly movie collection manager
##  Copyright (C) 2012 Christoph Meinhart, Michael Seiwald
##
##  This file is part of Hamster.
##
##  Hamster is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License along
##  with this program; if not, write to the Free Software Foundation, Inc.,
##  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##
#############################################################################

import platform
from subprocess import Popen


def humanize_mins(minutes):
    minutes = int(minutes)
    hours = minutes / 60
    minutes = minutes % 60
    if hours > 0:
        return "%02d:%02d" % (hours, minutes)
    return "%02d" % minutes

def os_open_file(full_file_path):
    os_type = platform.system()
    if os_type == 'Linux':
        cmd = 'xdg-open'
    elif os_type == 'Windows':
        cmd = 'start'
    elif os_type == 'Darwin':
        cmd = 'open'
    if cmd:
        print "opening %s with %s" % (full_file_path, cmd)
        Popen([cmd, full_file_path])
        return
    print "no suitible command to open file on system found"
