from Caption_Generator.i_caption_generator import ICaptionGenerator
from youtube_transcript_api import YouTubeTranscriptApi
from utils.caption_maker import caption_maker
from utils.util import english
import logging

class CaptionGenerator(ICaptionGenerator):
    """
    Class for generating captions.
    """

    def __init__(self) -> None:
        """Initialize the CaptionGenerator class."""
        super().__init__()
        self.ytb_transcript = YouTubeTranscriptApi()

    def generate_captions(self, video_id: str) -> str:
        """
        Generate captions for a given video ID.

        Args:
            video_id (str): The ID of the video to generate captions for.

        Returns:
            str: The generated captions.
        """

        logging.info("- Downloading captions for video %s", video_id)
        # In the next releases, we will add the ability to choose the language of the captions
        # for now, we will only download the english captions
        # if the video has no captions, we will skip it
        # If a network error happen while downloading the captions, we will skip the video
        try :
            fetched_transcript = self.ytb_transcript.fetch(
                video_id,
                languages=english
            )
            logging.info("- Captions downloaded successfully for video %s", video_id)
            logging.info("- Number of captions : %s", len(fetched_transcript))

            captions = caption_maker(fetched_transcript)

            print(f"captions : {captions}")

            return captions

        except Exception as e:
            raise Exception("Error while downloading captions for the video." + video_id)
