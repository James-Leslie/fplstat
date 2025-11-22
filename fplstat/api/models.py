from typing import Any, Dict, List, Union

from pydantic import BaseModel, ConfigDict


class BootstrapStaticResponse(BaseModel):
    """Response model for the bootstrap-static endpoint"""

    model_config = ConfigDict(extra="allow")  # Allow extra fields FPL might add

    chips: List[Dict[str, Any]]
    element_stats: List[Dict[str, Any]]
    element_types: List[Dict[str, Any]]
    elements: List[Dict[str, Any]]
    events: List[Dict[str, Any]]
    game_config: Dict[str, Any]
    game_settings: Dict[str, Any]
    phases: List[Dict[str, Any]]
    teams: List[Dict[str, Any]]
    total_players: int


class Fixture(BaseModel):
    """Model for a single fixture"""

    model_config = ConfigDict(extra="allow")

    code: int
    event: int
    finished: bool
    finished_provisional: bool
    id: int
    kickoff_time: str
    minutes: int
    provisional_start_time: bool
    pulse_id: int
    started: bool
    stats: List[Dict[str, Any]]
    team_a: int
    team_a_difficulty: int
    team_a_score: Union[int, None]
    team_h: int
    team_h_difficulty: int
    team_h_score: Union[int, None]


class FixturesResponse(BaseModel):
    """Response model for the fixtures endpoint"""

    fixtures: List[Fixture]