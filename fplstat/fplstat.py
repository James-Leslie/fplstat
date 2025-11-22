from typing import List, Optional

from .api import APIClient
from .models import Player


class FPLStatClient:
    def get_player(self, player_id: int) -> Optional[Player]:
        """Get a specific player by ID"""
        players = self.get_players()
        return next((p for p in players if p.id == player_id), None)

    def get_players_by_team(self, team_id: int) -> List[Player]:
        """Get all players from a specific team"""
        players = self.get_players()
        return [p for p in players if p.team == team_id]


class FPLStat:
    def __init__(self):
        # Initialize API client, which fetches raw data from FPL API
        self.api = APIClient()
        # Get raw data from bootstrap-static endpoint
        self.raw_data = self.api.fetch_bootstrap_static()

    def get_players(self) -> List[Player]:
        """Get transformed player data"""

        # Transform raw dict elements into Player objects
        return [Player(**element) for element in self.raw_data.elements]

    def get_fixture_difficulty_matrix(self):
        """Returns fixture difficulty matrix"""
        pass
