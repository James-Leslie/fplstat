from typing import List

from .api import APIClient
from .models import Fixture, Player, PlayerTransformer


class FPLStat:
    def __init__(self):
        # Initialize API client, which fetches raw data from FPL API
        self.api = APIClient()
        # Get raw data from bootstrap-static endpoint
        self.raw_data = self.api.get_bootstrap_static()

    def get_players(self) -> List[Player]:
        """Get transformed player data"""

        # Transform raw dict elements, then create Player objects
        return [
            Player(**PlayerTransformer.transform(raw_element))
            for raw_element in self.raw_data.elements
        ]

    def get_fixtures(self) -> List[Fixture]:
        """Returns list of fixtures"""

        # Get raw fixture data from API client
        raw_fixtures = self.api.get_fixtures()
        return [Fixture(**fixture) for fixture in raw_fixtures.fixtures]

    def get_fixture_difficulty_matrix(self):
        """Returns fixture difficulty matrix"""
        pass
