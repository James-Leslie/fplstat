from typing import Any, Dict, List, Optional

import requests

from .models import BootstrapStaticResponse


class APIClient:
    """Handles all FPL API interactions"""

    BASE_URL = "https://fantasy.premierleague.com/api/"

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        # Add headers to avoid potential blocking
        self.session.headers.update({"User-Agent": "fplstat"})

    def _get(self, endpoint: str) -> Any:
        """Make a GET request to an endpoint"""
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def fetch_bootstrap_static(self) -> Dict[str, Any]:
        """Returns raw data with keys: elements, teams, element_types, events, etc."""
        data = self._get("bootstrap-static/")
        # Validate the response structure
        BootstrapStaticResponse.parse_obj(**data)
        return data

    def fetch_fixtures(self) -> List[Dict[str, Any]]:
        """Fetch all fixtures for the season"""
        return self._get("fixtures/")

    def fetch_element_summary(self, element_id: int) -> Dict[str, Any]:
        """
        Fetch detailed data for a specific element including historical data
        """
        return self._get(f"element-summary/{element_id}/")
