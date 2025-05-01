from typing import overload
import logging
from youtube_api import YouTubeDataAPI
from Youtube_Search.I_youtube_search import IYoutubeSearch

class YoutubeSearch(IYoutubeSearch):

    def __init__(self):
        """Initialize the YoutubeSearch class."""
        super().__init__()

    def __init__(self, api_key: str):
        """Initialize the YoutubeSearch class with API key."""
        super().__init__()
        self.API_KEY = api_key
        self.ytb_client = YouTubeDataAPI(self.API_KEY)


    def search(self, search_query: str, max_results: int = 5) -> dict:
        """Search for videos using the search query and return the results."""

        # We are sure that the search_query is not empty and max_results is greater than 0
        # The controller has already checked this

        search_results = self.ytb_client.search(
            q=search_query,
            max_results=max_results
        )

        if len(search_results) < max_results :
            logging.warning("- The number of videos found is less than the required. ")

        if len(search_results) == 0 :
            logging.error("- No videos found for the search query.")
            raise ValueError("No videos found for the search query.")

        if not search_results :
            logging.error(f"The object holding the search result is None")
            raise Exception("The object holding the search results is None")

        search_res_dict = {}

        counter = 0
        for result in search_results :

            logging.info(f"- Making the dictionary of video {counter}")

            search_res_dict[f'video_{counter}'] = {}

            search_res_dict[f'video_{counter}']['video_id'] = result['video_id']
            search_res_dict[f'video_{counter}']['video_title'] = result['video_title']
            search_res_dict[f'video_{counter}']['video_description'] = result['video_description']
            search_res_dict[f'video_{counter}']['channel_title'] = result['channel_title']
            search_res_dict[f'video_{counter}']['video_thumbnail'] = result['video_thumbnail']



            logging.info("- video_id : %s", search_res_dict[f'video_{counter}']['video_id'])
            logging.info("- title : %s", search_res_dict[f'video_{counter}']['video_title'])
            logging.info("--------------------------------------------------")

            counter = counter + 1

        logging.info("- search results type : %s", type(search_results))
        del counter



        return search_res_dict