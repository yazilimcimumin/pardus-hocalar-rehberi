#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Kurulum Scripti
Ottoman Techs - Teknofest 2026
"""

from setuptools import setup, find_packages
import os

# Uzun açıklama için README dosyasını oku
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Versiyon bilgisi
VERSION = "1.0.0"

setup(
    name="pardus-yol-arkadasi",
    version=VERSION,
    author="Ottoman Techs",
    author_email="ottoman.techs@example.com",
    description="Pardus için interaktif kullanıcı rehberi ve on-boarding sistemi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OttomanTechs/pardus-yol-arkadasi",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "Topic :: Desktop Environment",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: Turkish",
    ],
    python_requires=">=3.10",
    install_requires=[
        "PyQt5>=5.15.9",
    ],
    entry_points={
        "console_scripts": [
            "pardus-yol-arkadasi=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": [
            "data/tutorials/*.json",
            "data/audio/*.mp3",
            "../resources/icons/*.png",
            "../resources/icons/*.svg",
            "../resources/images/*.png",
            "../resources/styles/*.qss",
        ],
    },
    zip_safe=False,
)
