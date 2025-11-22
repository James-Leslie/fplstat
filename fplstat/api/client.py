from typing import Any, Dict, Optional

import requests

from .models import BootstrapStaticResponse, FixturesResponse


class APIClient:
    """Handles all FPL API interactions"""

    BASE_URL = "https://fantasy.premierleague.com/api/"

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        # Add headers to avoid potential blocking
        self.session.headers.update({"User-Agent": "fplstat"})

    def _get(self, endpoint: str) -> Any:
        """Make a GET request to an endpoint and return the JSON response"""

        # Construct full URL
        url = f"{self.BASE_URL}{endpoint}"
        # Make the GET request
        response = self.session.get(url)
        # Raise an error for bad responses
        response.raise_for_status()
        # Return the JSON content of the response
        return response.json()

    def get_bootstrap_static(self) -> BootstrapStaticResponse:
        """Returns raw data with keys: elements, teams, element_types, events, etc."""

        # Fetch data from the bootstrap-static endpoint
        data = self._get("bootstrap-static/")
        # Validate the response structure
        return BootstrapStaticResponse(**data)

    def get_fixtures(self) -> FixturesResponse:
        """Fetch all fixtures for the season"""

        # Fetch data from the fixtures endpoint
        data = self._get("fixtures/")
        return FixturesResponse(fixtures=data)

    def get_element_summary(self, element_id: int) -> Dict[str, Any]:
        """
        Fetch detailed data for a specific element including historical data
        """

        # Fetch data from the element-summary endpoint
        return self._get(f"element-summary/{element_id}/")
