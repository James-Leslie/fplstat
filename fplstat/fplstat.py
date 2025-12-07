import pandas as pd

from .api import APIClient
from .transforms import transform_players


class FPLStat:
    def __init__(self):
        """Initializes the FPLStat client."""
        self.api = APIClient()
        self._raw_data = None

    @property
    def raw_data(self):
        """
        Property to lazily fetch and cache the bootstrap-static data.
        The data is fetched only on the first access.
        """
        if self._raw_data is None:
            # Get raw data from bootstrap-static endpoint
            self._raw_data = self.api.get_bootstrap_static()
        return self._raw_data

    def get_players(self) -> pd.DataFrame:
        """Get transformed player data

        Returns:
            pd.DataFrame: A DataFrame containing player data.
        """

        # Transform players using the transform_players function
        players = transform_players(self.raw_data.elements)
        return players

    def get_fixtures(self):
        """Returns list of fixtures"""
        pass

    def get_fixture_difficulty_matrix(self):
        """Returns fixture difficulty matrix"""
        pass
