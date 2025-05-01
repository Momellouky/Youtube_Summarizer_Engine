from abc import ABC, abstractmethod


class ICaptionGenerator(ABC):
    """
    Abstract class for caption generation.
    """

    @abstractmethod
    def generate_captions(self, video_id: str) -> str:
        """
        Abstract method to be implemented by subclasses.
        """
        pass