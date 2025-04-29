import logging


class LoggerUtil:

    def __init__(self) -> None:
        """Initialize the LoggerUtil class."""
        self.info_logger = logging.getLogger(__name__)
        self.info_logger.setLevel(logging.INFO)

        self.deug_logger = logging.getLogger(__name__)
        self.debug_logger.setLevel(logging.DEBUG)

        self.error_logger = logging.getLogger(__name__)
        self.error_logger.setLevel(logging.ERROR)

        self.warning_logger = logging.getLogger(__name__)
        self.warning_logger.setLevel(logging.WARNING)

    def get_info_logger(self):
        """Get the info logger."""
        return self.info_logger

    def get_debug_logger(self):
        """Get the debug logger."""
        return self.debug_logger

    def get_error_logger(self):
        """Get the error logger."""
        return self.error_logger

    def get_warning_logger(self):
        """Get the warning logger."""
        return self.warning_logger

    
