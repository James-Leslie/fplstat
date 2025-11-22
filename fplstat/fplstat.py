import pandas as pd

from .api import APIClient
from .transforms import transform_players


class FPLStat:
    def __init__(self):
        # Initialize API client, which fetches raw data from FPL API
        self.api = APIClient()
        # Get raw data from bootstrap-static endpoint
        self.raw_data = self.api.get_bootstrap_static()

    def get_players(self) -> pd.DataFrame:
        """Get transformed player data"""

        # Transform each player using the transform_player function
        players = transform_players(self.raw_data.elements)
        # Convert list of dicts to DataFrame
        return players

    def get_fixtures(self):
        """Returns list of fixtures"""
        pass

    def get_fixture_difficulty_matrix(self):
        """Returns fixture difficulty matrix"""
        pass
