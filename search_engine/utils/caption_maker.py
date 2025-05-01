from youtube_transcript_api import FetchedTranscript


def caption_maker(fetched_transcript : FetchedTranscript):
    """
    Function to create captions from a list of dictionaries.

    Args:
        caption_list (list): List of dictionaries containing caption data.

    Returns:
        str: Formatted string of captions.
    """
    captions = ""
    for snippet in fetched_transcript:
        text = snippet.text
        captions += text + " "

    return captions
