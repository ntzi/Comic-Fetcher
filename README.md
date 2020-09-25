# Comic Fetcher

Fetch new comic from https://xkcd.com/ every 1 hour. Save up to 2 comics in total in 'comics' directory.


### Prerequisites

* Python 3


### Usage

#### Example

```
>>> from src.comic_fetcher import Comic
>>> comic = Comic()
>>> comic.fetch()
New comic downloaded!            
60 minutes remaining until new comic arrives.
```


## Tests

#### Example

```
$ python comic_fetcher_test.py
```
