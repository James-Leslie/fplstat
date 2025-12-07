from typing import List

import numpy as np
import pandas as pd

from fplstat.api.models import Element

# Keep-list of columns to include in final DataFrame, includes original api names and their renamed versions
# if None, then no rename is applied
KEEP_COLUMNS = {
    # Basic info
    "id": "player_id",
    "element_type": "position_id",  # 1=GK, 2=DEF, 3=MID, 4=FWD
    "team": "team_id",
    "web_name": "short_name",
    "full_name": None,
    # Pricing and ownership
    "now_cost": "price",
    "selected_by_percent": "ownership_pct",
    # Game stats
    "games_played": None,
    "starts": None,
    "minutes": None,
    "total_points": "points",
    "goals_scored": None,
    "assists": None,
    "gi": "goal_involvements",  # needs to be computed
    "clean_sheets": None,
    "goals_conceded": None,
    "own_goals": None,
    "penalties_saved": None,
    "penalties_missed": None,
    "yellow_cards": None,
    "red_cards": None,
    "saves": None,
    "clearances_blocks_interceptions": None,
    "recoveries": None,
    "tackles": None,
    "defensive_contribution": None,
    "bonus": None,
    "bps": None,  # Bonus points system
    # Expected stats
    "expected_goals": None,
    "expected_assists": None,
    "expected_goal_involvements": None,
    "expected_goals_conceded": None,
    "xP": "expected_points",  # needs to be computed
    # Per-90 stats
    "starts_per_90": None,
    "p_90": "points_per_90",  # needs to be computed
    "g_90": "goals_per_90",  # needs to be computed
    "a_90": "assists_per_90",  # needs to be computed
    "gi_90": "goal_involvements_per_90",  # needs to be computed
    "b_90": "bonus_per_90",  # needs to be computed
    "defensive_contribution_per_90": None,
    "goals_conceded_per_90": None,
    "saves_per_90": None,
    "clean_sheets_per_90": None,
    "xP_90": "expected_points_per_90",  # needs to be computed
    "expected_goals_per_90": None,
    "expected_assists_per_90": None,
    "expected_goal_involvements_per_90": None,
    "expected_goals_conceded_per_90": None,
    # Advanced stats
    "influence": None,
    "creativity": None,
    "threat": None,
    "ict_index": None,  # Combined ICT score
    # Performance metrics
    "points_per_game": None,
    "form": None,
    # Status and availability
    "status": None,
    "scout_risks": None,
    "news": None,
    "news_added": None,
    # Predicted points
    "ep_this": None,  # Expected points this gameweek
    "ep_next": None,  # Expected points next gameweek
}


def transform_players(data: List[Element]) -> pd.DataFrame:
    """Transform a list of Element models into a DataFrame with curated columns and computed stats.

    Args:
        data: List of Element models from the FPL API bootstrap-static endpoint

    Returns:
        DataFrame ready for easy analysis

        All columns are renamed for easier use (e.g., web_name -> name, element_type -> position)

    Note:
        - Only players with minutes > 0 are included
        - Price is converted from tenths (API format) to millions
    """

    # 1. Convert to DataFrame
    df = pd.DataFrame([d.model_dump() for d in data])

    # 2. Filter players with minutes > 0 and can_select == True
    df = df.query("minutes > 0 and can_select == True")

    # 3. Convert now_cost to millions
    df["now_cost"] = df["now_cost"] / 10

    # 4. Calculate extra columns
    df = df.assign(
        full_name=lambda x: x.first_name + " " + x.second_name,
        games_played=lambda x: (x.total_points / x.points_per_game)
        .where(x.total_points > 0, 0)
        .round(0)
        .astype(int),
        gi=lambda x: x.goals_scored + x.assists,
        p_90=lambda x: x.total_points / x.minutes * 90,
        g_90=lambda x: x.goals_scored / x.minutes * 90,
        a_90=lambda x: x.assists / x.minutes * 90,
        gi_90=lambda x: (x.goals_scored + x.assists) / x.minutes * 90,
        b_90=lambda x: x.bonus / x.minutes * 90,
        xP=lambda x: (
            # Appearance points
            x.games_played  # 1 point for every game played
            + x.starts  # 1 extra point for every start (60+ min)
            # Goals - position dependent
            + (6 * x.expected_goals).where(x.element_type.isin([1, 2]), 0)  # GK/DEF
            + (5 * x.expected_goals).where(x.element_type == 3, 0)  # MID
            + (4 * x.expected_goals).where(x.element_type == 4, 0)  # FWD
            # Assists - 3 points (all positions)
            + 3 * x.expected_assists
            # Clean sheets - Poisson probability from expected goals conceded
            + (4 * np.exp(-x.expected_goals_conceded)).where(
                x.element_type.isin([1, 2]), 0
            )  # GK/DEF
            + (np.exp(-x.expected_goals_conceded)).where(x.element_type == 3, 0)  # MID
            # Goals conceded - minus 1 point per 2 goals for GK/DEF
            - (x.expected_goals_conceded / 2).where(x.element_type.isin([1, 2]), 0)
            # Saves - 1 point per 3 saves for GK only
            + (x.saves / 3).where(x.element_type == 1, 0)
            # Defensive contribution points - position dependent
            + (2 * x.defensive_contribution / 10).where(x.element_type == 2, 0)  # DEF
            + (2 * x.defensive_contribution / 12).where(x.element_type.isin([3, 4]), 0)
            # Penalty saves - 5 points
            + 5 * x.penalties_saved
            # Penalty misses - minus 2 points
            - 2 * x.penalties_missed
            # Yellow cards - minus 1 point
            - x.yellow_cards
            # Red cards - minus 3 points
            - 3 * x.red_cards
            # Own goals - minus 2 points
            - 2 * x.own_goals
            # Bonus points
            + x.bonus
        ),
        xP_90=lambda x: x.xP / x.minutes * 90,
    )

    # 4. Calculate "expected points" per 90 (using expected per-90 stats)
    # Uses the FPL scoring rules to compute expected points based on expected goals, assists, etc.

    # 5. Keep only the columns in KEEP_COLUMNS, and rename them
    df = df[list(KEEP_COLUMNS.keys())]
    df = df.rename(columns={k: v for k, v in KEEP_COLUMNS.items() if v is not None})

    return df
