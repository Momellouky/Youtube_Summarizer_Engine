import logging

from Controller.i_controller import IController
from youtube_api import YouTubeDataAPI
import os


class Controller(IController) :

    def __init__(self) -> None:
        """Initialize the Controller class."""
        super().__init__()
        self.API_KEY = os.getenv("YTB_DATA_API_KEY")

    def work(self, search_query : str, max_results : int = 5) -> None:
        """The implementation of the work method.
        """

        if not search_query :
            raise ValueError("Search query cannot be empty.")

        if max_results <= 0 :
            raise ValueError("Max results should be greater than 0.")

        if not isinstance(max_results, int) :
            raise TypeError("Max results should be an integer.")

        # start working on the request

        # 1. Search for videos using the search query
        ytb_client = YouTubeDataAPI(self.API_KEY)
        search_results = ytb_client.search(
            q=search_query,
            max_results=max_results
        )

        for result in search_results :
            logging.info("- video_id : %s", result['video_id'])
            logging.info("- title : %s", result['video_title'])
            logging.info("--------------------------------------------------")

        logging.info("- search results type : %s", type(search_results))

        # 2. Download captions for the videos

        # 3. Summarize the captions
        # 4. Return the summarized videos
        return search_results