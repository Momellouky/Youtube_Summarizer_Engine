from Video_Summmarizer.i_video_summarizer import IVideoSummarizer
from groq import Groq
import os
import logging


class VideoSummarizer(IVideoSummarizer):
    """
    Class for summarizing videos.
    """

    def __init__(self) -> None:
        """Initialize the VideoSummarizer class."""
        super().__init__()
        self.groq = Groq(
            api_key=os.getenv("GROQ_API_KEY"),

        )


    def summarize(self, captions: str) -> str:
        """
        Summarize the video at the given path.
        :param caption: The caption of the video to summarize.
        :return: The summarized caption.
        """

        chat_completion = self.groq.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following captions : {captions}"
                }
            ],
            model="gemma2-9b-it",
            temperature=0.7,
        )
        summary = chat_completion.choices[0].message.content

        return summary


    def summarize(self, captions_array : list) -> str:
        """Summarize the caption chunks
        :param caption: The caption of the video to summarize.
        :return: The summarized caption.
        """

        if len(captions_array) == 0 :
            raise ValueError("Captions array cannot be empty.")
        if not isinstance(captions_array, list) :
            raise TypeError("Captions array should be a list.")
        if len(captions_array) == 1 :
            logging.info("- Only one chunk found. Summarizing it.")
            return self.summarize(captions_array[0])
        else :
            logging.info("- More than one chunk found. Summarizing them.")
            summary = ""
            for caption in captions_array :
                summary += self.summarize(caption)

            return self.summarize(summary)
