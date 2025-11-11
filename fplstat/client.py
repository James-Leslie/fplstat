from fplstat.api import APIClient


class FPLStat:
    def __init__(self):
        # Initialize API client, which fetches raw data from FPL API
        self.api = APIClient()

    def get_players(self, min_minutes=90):
        """Returns the fully transformed players dataframe"""
        data = self.api.fetch_bootstrap_static()
        return data.get("elements", [])

    def get_fixture_difficulty_matrix(self):
        """Returns fixture difficulty matrix"""
        pass
