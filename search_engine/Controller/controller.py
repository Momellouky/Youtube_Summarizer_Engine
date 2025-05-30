import logging

from Controller.i_controller import IController
from Video_Summmarizer.MRL_VideoSummarizer import MRLVideoSummarizer
from Youtube_Search.youtube_search import YoutubeSearch
from Caption_Generator.caption_generator import CaptionGenerator
from Video_Summmarizer.VideoSummarizer import VideoSummarizer
from utils.util import augment_query, MAX_TOKENS
from utils.util import fragment_captions
import os


class Controller(IController) :

    def __init__(self) -> None:
        """Initialize the Controller class."""
        super().__init__()
        self.API_KEY = os.getenv("YTB_DATA_API_KEY")
        self.ytb_client = YoutubeSearch(self.API_KEY)
        self.caption_generator = CaptionGenerator()
        self.video_summarizer = VideoSummarizer()
        self.mr_video_summarizer = MRLVideoSummarizer()

    def work(self, search_query : str, max_results : int = 5) -> dict:
        """The implementation of the work method.
        """

        if not search_query :
            raise ValueError("Search query cannot be empty.")

        if max_results <= 0 :
            raise ValueError("Max results should be greater than 0.")

        if not isinstance(max_results, int) :
            raise TypeError("Max results should be an integer.")

        # 1. Search for videos using the search query

        #### Augment the search query with the word "Talk OR Conference"
        search_query = augment_query(search_query)
        ### Search for videos using the augmented search query
        videos_dict = self.ytb_client.search(search_query, max_results)

        # 2. Download captions for the videos

        captions_dict = {}
        for video in videos_dict :
            captions_dict[video] = {}
            try :
                captions = self.caption_generator.generate_captions(videos_dict[video]['video_id'])
                captions_dict[video]['captions'] = captions
            except Exception as e:
                logging.error(e)
                captions_dict[video]['captions'] = None
                continue


        # 3. Summarize the captions

        for video_nbr, captions in captions_dict.items() :
            logging.info(f"- Summarizing captions for video {video_nbr}")

            try :
                captions = captions_dict[video_nbr]['captions']
                if captions is None :
                    logging.error("No captions found for video %s", videos_dict[video_nbr]['video_id'])
                    logging.warning(f"- Skipping video {videos_dict[video_nbr]['video_id']}")
                    videos_dict[video_nbr]['summary'] = None
                    continue
                if len(captions) > MAX_TOKENS :
                    logging.info("- The video transcript is too long. We are processing it using MRVideoSummarizer.")
                    videos_dict[video_nbr]['summary'] = self.mr_video_summarizer.summarize(captions)
                    logging.info("- Summary : %s", videos_dict[video_nbr]['summary'])
                else :
                    logging.info("- Start summarizing the video...")
                    summary = self.video_summarizer.summarize(captions)
                    videos_dict[video_nbr]['summary'] = summary
                    logging.info("- Summary : %s", videos_dict[video_nbr]['summary'])
            except Exception as e:
                logging.error(e)
                videos_dict[video_nbr]['summary'] = None
                continue

        # delete captions_dict for memory efficiency
        del captions_dict

        # 4. Return the summarized videos
        return videos_dict