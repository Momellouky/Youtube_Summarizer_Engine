from abc import ABC, abstractmethod


class IVideoSummarizer(ABC):
    """
    Abstract base class for video summarization.
    """

    @abstractmethod
    def summarize(self, captions: str) -> str:
        """
        Abstract method to be implemented by subclasses.
        """
        pass