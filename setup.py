#!/usr/bin/env python
# coding=utf-8

#
# A Last.fm API interface.
# Copyright (C) 2013  Никола "hauzer" Вукосављевић
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from    lastfm      import  info
from    setuptools  import  find_packages, setup


readme_lines = open("README.rst", "r").read().splitlines()

description = readme_lines[0]
long_description = "\n".join(readme_lines[2:])

setup(name              = "{}h".format(info.NAME),
      version           = info.VERSION,
      packages          = find_packages(),
      install_requires  = ["requests"],

      author            = info.AUTHOR,
      author_email      = "hauzer@gmx.com",
      description       = description,
      long_description  = long_description,
      license           = "GPLv3",
      url               = "https://bitbucket.org/{}/{}/".format(info.AUTHOR_NICK, info.NAME),
      download_url      = "https://bitbucket.org/{}/{}/downloads".format(info.AUTHOR_NICK, info.NAME),
      
      classifiers = [
                     "Development Status :: 4 - Beta",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python :: 3",
                     "Topic :: Software Development :: Libraries",
                    ]
      )

