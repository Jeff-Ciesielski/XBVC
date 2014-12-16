import os
from setuptools import setup
import glob
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "XBVC",
    version = "0.0.1",
    author = "Jeff Ciesielski",
    author_email = "jeffciesielski@gmail.com",
    description = ("eXtensible Bit Vector Communication (protocol)"),
    license = "MIT",
    keywords = "usart communication microcontroller",
    url = "https://github.com/Jeff-Ciesielski/XBVC",
    packages=['XBVC', 'XBVC.emitters', 'XBVC.emitters'],
    package_dir={'XBVC': 'src/', 'XBVC.emitters':'src/emitters'},
    package_data={'XBVC.emitters': ['templates/*.*']},
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            'xbvcgen = XBVC.xbvcgen:main'
    ]},
    install_requires=[
          'pyyaml >= 3.10',
          'jinja2 == 2.7.2',
    ],
)
