import wikipedia

def wiki(name="War Goddess", length=1):
    """Searches for a Wikipedia article and returns a summary."""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Searches for a Wikipedia article and returns a summary."""
    result = wikipedia.search(name)
    return result
