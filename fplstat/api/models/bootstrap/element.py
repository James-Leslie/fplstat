from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class Element(BaseModel):
    """Model for FPL player data from bootstrap-static elements"""

    model_config = ConfigDict(extra="allow")

    # Basic info
    id: int
    web_name: str
    first_name: str
    second_name: str
    photo: str

    # Team and position
    element_type: int  # 1=GK, 2=DEF, 3=MID, 4=FWD
    team: int
    team_code: int

    # Pricing and ownership
    now_cost: int
    selected_by_percent: float
    cost_change_start: int
    cost_change_event: int
    cost_change_start_fall: int
    cost_change_event_fall: int

    # Performance metrics
    total_points: int
    event_points: int
    form: float
    points_per_game: float
    value_form: float
    value_season: float

    # Availability
    status: str  # 'a'=available, 'i'=injured, 'd'=doubtful, etc.
    chance_of_playing_this_round: Optional[int]
    chance_of_playing_next_round: Optional[int]
    news: str
    news_added: Optional[datetime] = None

    # Game stats
    minutes: int
    starts: int
    goals_scored: int
    assists: int
    clearances_blocks_interceptions: int
    recoveries: int
    tackles: int
    defensive_contribution: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int  # Bonus points system

    # Advanced stats
    influence: float
    creativity: float
    threat: float
    ict_index: float  # Combined ICT score

    # Expected stats
    expected_goals: float
    expected_assists: float
    expected_goal_involvements: float
    expected_goals_conceded: float

    # Per-90 stats
    expected_goals_per_90: float
    expected_assists_per_90: float
    expected_goal_involvements_per_90: float
    expected_goals_conceded_per_90: float
    goals_conceded_per_90: float
    saves_per_90: float
    starts_per_90: float
    clean_sheets_per_90: float
    defensive_contribution_per_90: float

    # Rankings
    influence_rank: int
    influence_rank_type: int
    creativity_rank: int
    creativity_rank_type: int
    threat_rank: int
    threat_rank_type: int
    ict_index_rank: int
    ict_index_rank_type: int
    form_rank: int
    form_rank_type: int
    points_per_game_rank: int
    points_per_game_rank_type: int
    selected_rank: int
    selected_rank_type: int
    now_cost_rank: int
    now_cost_rank_type: int

    # Transfer activity
    transfers_in: int
    transfers_in_event: int
    transfers_out: int
    transfers_out_event: int

    # Set pieces
    corners_and_indirect_freekicks_order: Optional[int] = None
    corners_and_indirect_freekicks_text: str
    direct_freekicks_order: Optional[int] = None
    direct_freekicks_text: str
    penalties_order: Optional[int] = None
    penalties_text: str

    # Other stats
    dreamteam_count: int

    # Flags
    can_select: bool
    can_transact: bool
    in_dreamteam: bool
    removed: bool
    special: bool
    has_temporary_code: bool

    # Additional info
    region: Optional[int] = None
    birth_date: Optional[date] = None
    team_join_date: Optional[date] = None
    code: int
    opta_code: str
    squad_number: Optional[int] = None

    # Predicted points
    ep_this: float  # Expected points this gameweek
    ep_next: float  # Expected points next gameweek
