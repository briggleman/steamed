from steamed import __version__
from setuptools import setup, find_packages

setup(
    name = "steamed",
    version = __version__,
    description = "Steam sales web scraper",
    author = "Ben Riggleman",
    author_email = "ben.riggleman@gmail.com",
    url = "https://github.com/briggleman/steamed",
    keywords = ["steamed", "steam sales", "steam python", "web scraper", "spider"],
    install_requires = ["requests>=2.4.1", "beautifulsoup4>=4.3.2"],
    packages = find_packages(),
    classifiers = [],
    long_description = """\
    steamed: Steam sales web scraper for store.steampowered.com
""" )