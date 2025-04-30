from abc import ABC, abstractmethod

class IController(ABC) :
    """ Abstract base class for controllers.
    """

    @abstractmethod
    def work(self, search_query : str, max_results : int = 5) -> None:
        """Abstract method to be implemented by subclasses.
        """
        pass