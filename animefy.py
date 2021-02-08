from mal import AnimeSearch

def search(anTitle):
    search = AnimeSearch(anTitle)
    return search.results[0].synopsis
