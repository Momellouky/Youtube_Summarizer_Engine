
from abc import ABC, abstractmethod

class IYoutubeSearch(ABC) :


    @abstractmethod
    def search(self, search_query : str, max_results : int = 5) -> dict:
        """Abstract method to be implemented by subclasses.
        """
        pass