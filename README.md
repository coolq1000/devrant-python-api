# devrant-python-api

Another unofficial https://www.devrant.io api.

## Installation
To include this into your project, it is very simple, all you must do is download(clone) this repo, and extract it in the same directory as your project, then import it.

Here is what your directory tree should look a little like.
```
Project/
  DevrantAPI/
    devrant.py
  scriptthatispartoftheproject.py
  ..etc.
```

## Usage
To use this library, you must first import it.
```python
from Devrant import devrant
```

Now we can create our devrant object.
```python
dr = devrant.Devrant()
```

Then we can call some functions.
```python
dr.get_rants('SORT', LIMIT, SKIP)
dr.get_rant('SORT', INDEX)
dr.get_user_id('NAME')
dr.get_profile(ID)
dr.get_search('TERM')
```

## Options
There are a few different options to choose from, in the above example you may have noticed `SORT`, `LIMIT`..etc.
These are options, here are what you can choose from.
```
get_rants():
  SORT - STRING:
    algo,
    recent,
    top
  LIMIT - INTEGER:
    0-50
  SKIP - INTEGER:
    0-~788
get_rant():
  SORT - STRING:
    algo,
    recent,
    top
  INDEX - INTEGER:
    0-~788
get_user_id():
  NAME - STRING:
    ANY STRING
get_profile():
  ID - INTEGER:
    0-?
get_search():
  TERM - STRING:
    ANY STRING
```

If you are stuck you may look at the demo at the bottom of the api script.

Hope this API comes in handy!
