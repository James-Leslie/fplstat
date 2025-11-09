from typing import Any, Dict

import requests

BASE_URL = "https://fantasy.premierleague.com/api/"


class DataClient:
    """Handles FPL API requests with lazy loading and caching."""

    def __init__(self):
        """Initialize the DataClient with lazy loading."""
        self._bootstrap_static = None
        self._fixtures = None

    def _ensure_bootstrap_loaded(self):
        """Ensure bootstrap data is loaded."""
        if self._bootstrap_static is None:
            response = requests.get(f"{BASE_URL}bootstrap-static/")
            response.raise_for_status()
            self._bootstrap_static = response.json()

    @property
    def elements(self):
        """Get all elements (players) for the season."""
        self._ensure_bootstrap_loaded()
        return self._bootstrap_static.get("elements", [])

    @property
    def teams(self):
        """Get all teams for the season."""
        self._ensure_bootstrap_loaded()
        return self._bootstrap_static.get("teams", [])

    @property
    def events(self):
        """Get all events (gameweeks) for the season."""
        self._ensure_bootstrap_loaded()
        return self._bootstrap_static.get("events", [])

    @property
    def element_types(self):
        """Get player position types."""
        self._ensure_bootstrap_loaded()
        return self._bootstrap_static.get("element_types", [])

    @property
    def fixtures(self):
        """Get all fixtures for the season."""
        if self._fixtures is None:
            response = requests.get(f"{BASE_URL}/fixtures/")
            response.raise_for_status()
            self._fixtures = response.json()
        return self._fixtures

    def get_element_summary(self, player_id: int) -> Dict[str, Any]:
        """Get detailed history for a specific player."""
        response = requests.get(f"{BASE_URL}/element-summary/{player_id}/")
        response.raise_for_status()
        return response.json()
