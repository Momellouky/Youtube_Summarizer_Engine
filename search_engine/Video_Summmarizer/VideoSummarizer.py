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
