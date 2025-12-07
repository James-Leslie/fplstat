import pandas as pd

from .api import APIClient
from .transforms import transform_players


class FPLStat:
    def __init__(self):
        """Initializes the FPLStat client."""
        self.api = APIClient()
        self._raw_data = None
        self._fixtures_data = None

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

    @property
    def fixtures_data(self):
        """
        Property to lazily fetch and cache the fixtures data.
        The data is fetched only on the first access.
        """
        if self._fixtures_data is None:
            # Get fixtures data from fixtures endpoint
            self._fixtures_data = self.api.get_fixtures()
        return self._fixtures_data

    def get_players(self) -> pd.DataFrame:
        """Get transformed player data

        Returns:
            pd.DataFrame: A DataFrame containing player data.
        """

        # Transform players using the transform_players function
        players = transform_players(self.raw_data.elements)
        return players

    def get_fixtures(self) -> pd.DataFrame:
        """Get all fixtures for the season

        Returns:
            pd.DataFrame: A DataFrame containing fixture data.
        """
        return pd.DataFrame([f.model_dump() for f in self.fixtures_data.fixtures])

    def get_fixture_difficulty_matrix(self):
        """Returns fixture difficulty matrix"""
        pass
