"""Transform legacy Scrabble score data into a letter-to-score mapping."""
def transform(legacy_data):
    """Return a dictionary mapping lowercase letters to their Scrabble scores."""
    data = {}
    for key,value in legacy_data.items():
        for item in value:
            data[item.lower()] = key
    return data
