# Copyright 2012-2016 Jonathan Vasquez <jvasquez1011@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pkg.hooks.Hook import Hook

class Lvm(Hook):
    # Required Files
    _files = [
        "/sbin/lvm",
    ]
