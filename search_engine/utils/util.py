

ENGLISH = ['en', 'en-US', 'en-GB', 'en-CA', 'en-AU', 'en-NZ', 'en-IE', 'en-ZA', 'en-PH', 'en-IN', 'en-SG']


def augment_query(search_query: str) -> str:
    """Augment the search query with additional keyword
    to improve search results. The aim is to add keywords that
    will help to fetch conference and talks videos.
    :param search_query: The search query to augment.
    :return: The augmented search query.
    """
    # Add keywords to the search query
    augmented_query = search_query + " conference OR talk"
    return augmented_query