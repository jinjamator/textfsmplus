#!/usr/bin/python
#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup script."""

from setuptools import setup, find_packages
import textfsmplus
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding="utf8") as f:
    long_description = f.read()

setup(name='textfsmplus',
      maintainer='Wilhelm Putz',
      maintainer_email='wp@aci.guru',
      version=textfsmplus.__version__,
      description='Enhanced python module for parsing semi-structured text into python tables.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/jinjamator/textfsmplus',
      license='Apache License, Version 2.0',
      author='Wilhelm Putz',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries'],
      packages=['textfsmplus'],
      entry_points={
        'console_scripts': [
            'textfsm=textfsmplus.parser:main'
        ]
      },      
      include_package_data=True,
      package_data={'textfsmplus': ['../testdata/*']},
      install_requires=['six', 'future', 'regex'],
     )
