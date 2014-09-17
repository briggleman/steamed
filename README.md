steamed
=======

Spider for scraping Steam sales data from store.steampowered.com

<<<<<<< HEAD
## Installation
To install steamed, simply:

```python
pip install steamed
```
=======
<h2>Installation</h2>
Currently steamed is only available on github but will be available via pip shortly.
Current installation can be done by downloading steamed and placing it in appropriate folder for access.
>>>>>>> parent of 3bc975f... minor corrections

<h2>Usage</h2>
To use steamed simply include it in your project:

```python
import steamed
```

Then call the sales function:

```
steamed.sales()
```

Calling steamed.sales() will return an array of lists containing information on all the games currently on sale.

Current information returned is:

+ game - name of the game on sale
+ img - url to the Steam 120px thumbnail
+ appid - application id of the game
+ full - full price of the game (returned as a decimal)
+ sale - sale price of the game
+ pct - calculated percentage of the discount

<h2>Future Revisions</h2>
Future enhancements include the following:

+ type - content type (e.g. software, dlc, game)
