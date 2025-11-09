import pandas as pd

from .api.client import DataClient


class FPLstat:
    """Main interface for accessing Fantasy Premier League data.

    Provides a simple interface to load, transform, and access FPL data
    as ready-to-use pandas DataFrames.
    """

    def __init__(self):
        """Initialize the FPLstat client.

        # Example:

        ``` py
        from fplstat import FPLstat
        fpl = FPLstat()
        ```
        """
        self._data_client = DataClient()

    def get_players(self) -> pd.DataFrame:
        """Get DataFrame of all players with their stats.

        Returns:
            DataFrame with player information including stats, team, position, etc.

        # Example:
        ``` py
        players_df = fpl.get_players()
        ```
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.elements)

    def get_teams(self) -> pd.DataFrame:
        """Get DataFrame of all Premier League teams.

        Returns:
            DataFrame with team information including form, strength, etc.

        # Example:
        ``` py
        teams_df = fpl.get_teams()
        ```
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.teams)

    def get_fixtures(self) -> pd.DataFrame:
        """Get DataFrame of all fixtures for the season.

        Returns:
            DataFrame with fixture information including dates, scores, etc.

        # Example:
        ``` py
        fixtures_df = fpl.get_fixtures()
        ```
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.fixtures)

    def get_gameweeks(self) -> pd.DataFrame:
        """Get DataFrame of all gameweeks/events.

        Returns:
            DataFrame with gameweek information including dates, deadlines, etc.
        # Example:
        ``` py
        gameweeks_df = fpl.get_gameweeks()
        ```
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.events)

    def get_player_history(self, player_id: int) -> pd.DataFrame:
        """Get detailed history for a specific player.

        Args:
            player_id: The FPL player ID

        Returns:
            DataFrame with per-gameweek stats for the player

        # Example:
        ``` py
        history_df = fpl.get_player_history(player_id)
        ```
        """
        player_data = self._data_client.get_element_summary(player_id)
        # TODO: Transform raw data using transformers
        history_data = player_data["history"]
        return pd.DataFrame(history_data)

    def get_manager_team(self, manager_id: int) -> pd.DataFrame:
        """Get information about a manager's team.

        Args:
            manager_id: The FPL manager/entry ID

        Returns:
            DataFrame with manager team information
        """
        team_data = self._data_client.get_entry(manager_id)
        # TODO: Transform and structure the data appropriately
        return pd.DataFrame([team_data])
