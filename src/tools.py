from duckduckgo_search import DDGS

def web_search(query: str) -> str:
    with DDGS() as ddgs:
        results = list(ddgs.text(f"music {query}", max_results=1))
        if results:
            return results[0].get("title", "No title found")
    return "No results found."