from ddgs import DDGS

def mock_web_search(query: str) -> str:
    """Mock web search function that returns predefined music results based on query keywords.
    
    Args:
        query (str): Search query for music
        
    Returns:
        str: A mock search result title
    """
    mock_results = {
        "sad": "Someone Like You by Adele",
        "happy": "Happy by Pharrell Williams",
        "love": "All of Me by John Legend",
        "rock": "Sweet Child O' Mine by Guns N' Roses",
        "dance": "Uptown Funk by Mark Ronson ft. Bruno Mars"
    }
    
    # Check if any keyword from mock_results is in the query
    for keyword, result in mock_results.items():
        if keyword.lower() in query.lower():
            return result
    return "No results found."

def web_search(query: str) -> str:
    
    with DDGS() as ddgs:
        results = list(ddgs.text(f"music {query}", max_results=1))
        if results:
            return results[0].get("title", "No title found")
    return "No results found."