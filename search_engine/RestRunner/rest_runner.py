"""rest_runner.py
Author: Mohamed MELLOUKY
Date: 29/04/2025
Description:
This module provides a class to run REST API tests using the flask framework.
It allows you to run the endpoints and get the response.

Example usage:
    from RestRunner.rest_runner import RestRunner

    runner = RestRunner()
    runner.run()

    # To stop the server, use:
    runner.stop()
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from utils.logger_util import LoggerUtil


class RestRunner :
    """RestRunner: A Python package for running REST API .
    This package provides and interface for running the REST API endpoints.

    It allows you to run the endpoints and get the response."""

    def __init__(self) -> None:
        """Initialize the RestRunner class."""
        self.app = Flask(__name__)
        CORS(self.app)

        logging.basicConfig(level=logging.INFO)

        self.setup_routes()

    def run(self) -> None:
        self.app.run()


    def setup_routes(self) -> None:
        """Setup the routes for the REST API."""

        def summarize() :

            logging.info("- request received")
            logging.info(f"- data received : {request.json}")

            search_query = request.json.get('search_query', 1)
            max_results = request.json.get('max_results', 2)

            res = {}


            return jsonify(
                {
                    "message" : "Hello world"
                }
            )



        self.app.add_url_rule(
            rule= '/summarize',
            endpoint= "summarize",
            methods=['POST'],
            view_func= summarize,
        )


