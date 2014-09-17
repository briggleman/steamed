steamed
=======

Spider for scraping Steam sales data from store.steampowered.com

## Installation
To install steamed, simply:

```python
pip install steamed
```

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
+ pct - calculated percentage of the discount

## Future Revisions
Future enhancements include the following:

+ type - content type (e.g. software, dlc, game)
