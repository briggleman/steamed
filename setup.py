from authy import __version__
from setuptools import setup, find_packages

setup(
    name = "steamed",
    version = __version__,
    description = "Steam sales web scraper",
    author = "Ben Riggleman",
    author_email = "ben.riggleman@gmail.com",
    url = "https://github.com/briggleman/steamed",
    keywords = ["steamed", "steam sales", "steam python", "web scraper", "spider"],
    install_requires = ["requests>=2.2.1", "bs4>=4.0.0"],
    packages = find_packages(),
    classifiers = [],
    long_description = """\
    steamed: Steam sales web scraper for store.steampowered.com
""" )