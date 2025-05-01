from abc import ABC, abstractmethod


class IVideoSummarizer(ABC):
    """
    Abstract base class for video summarization.
    """

    @abstractmethod
    def summarize(self, video_path: str) -> str:
        """
        Abstract method to be implemented by subclasses.
        """
        pass