steamed
=======

Spider for scraping Steam sales data from store.steampowered.com

## Installation
Currently steamed is only available on github but will be available via pip shortly.
Current installation can be done by downloading steamed and placing it in appropriate folder for access.

## Usage
To use steamed simply include it in your project:

```python
import steamed
```

Then call the sales function:

```python
steamed.sales()
```

Calling steamed.sales() will return an array of lists containing information on all the games currently on sale.

Current information returned is:

+ game - name of the game on sale
+ img - url to the Steam 120px thumbnail
+ appid - application id of the game
+ full - full price of the game (returned as a decimal)
+ sale - sale price of the game

## Future Revisions
Future enhancements include the following:

+ pct - calculated percentage of the discount
+ type - content type (e.g. software, dlc, game)
