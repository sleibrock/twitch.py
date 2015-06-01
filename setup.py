#!/usr/bin/python3
#-*- coding:utf-8 -*-

from distutils.core import setup
import Kappa.info as info

files = [] 

setup(name="Twitch.tv",
    version=info.__version__,
    description="Access Twitch from the Shell",
    author=info.__author__,
    author_email=info.__email__,
    url=info.__url__,
    packages=["Kappa"],
    scripts=['twitch'],
    long_description="""
    Access Twitch.tv from the Shell
    Check streams, see viewers, load streams up directly
    """,
    license=info.__license__,
    classifiers=[
        # Add more classifiers later maybe
        "Programming Language :: Python :: 3"
    ],
    keywords="twitch livestreamer videogames video games"
)
