

ENGLISH = ['en', 'en-US', 'en-GB', 'en-CA', 'en-AU', 'en-NZ', 'en-IE', 'en-ZA', 'en-PH', 'en-IN', 'en-SG']
MAX_TOKENS = 6000

def augment_query(search_query: str) -> str:
    """Augment the search query with additional keyword
    to improve search results. The aim is to add keywords that
    will help to fetch conference and talks videos.
    :param search_query: The search query to augment.
    :return: The augmented search query.
    """
    # Add keywords to the search query
    augmented_query = search_query + " conference OR talk OR presentation OR lecture OR seminar OR symposium OR workshop"
    return augmented_query


def fragment_captions(captions: str, max_tokens : int = MAX_TOKENS ) -> list:
    """Fragment the captions into smaller chunks.
    :param captions: The captions to fragment.
    :param max_tokens: The maximum number of tokens in each chunk.
    :return: A list of chunks.
    """
    # Split the captions into chunks of max_tokens
    chunks = []
    for i in range(0, len(captions), max_tokens):
        chunks.append(captions[i:i + max_tokens])
    return chunks