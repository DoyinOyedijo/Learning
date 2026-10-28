# Learning

Mini projects I build while learning Python, from the 30 Days of Python roadmap and beyond.

## Projects

### Statistics Class (`statistics_class.py`)
A from-scratch rebuild of Python's built-in `statistics` module, written as a class.
- Computes count, sum, min, max, range, mean, median, mode, variance, standard deviation, and frequency distribution
- Every calculation is implemented by hand, with no statistics libraries

**Run:** `python statistics_class.py`

### Cat Breeds API Analysis (`cats_api.py`)
Pulls live breed data from [The Cat API](https://thecatapi.com/) and analyzes it.
- Fetches every breed with `requests` and parses the JSON response
- Uses regular expressions to turn weight and lifespan ranges (e.g. "3 - 5") into averages
- Calculates mean, median, mode, and standard deviation of breed weight (kg) and lifespan (years)
- Builds a frequency table of breeds by country of origin

**Run:** `pip install requests`, then `python cats_api.py`

## Author
Doyin Oyedijo — [github.com/DoyinOyedijo](https://github.com/DoyinOyedijo)
