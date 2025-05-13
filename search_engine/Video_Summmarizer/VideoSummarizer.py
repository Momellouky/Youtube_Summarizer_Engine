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

        # Check if the captions are empty
        if not captions:
            raise ValueError("Captions cannot be empty.")
        if not isinstance(captions, str) and not isinstance(captions, list):
            raise TypeError("Captions should be a string or a list. You have passed a %s", type(captions))

        # Summarize the captions when the data type is a string
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