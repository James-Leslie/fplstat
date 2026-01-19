from pydantic import BaseModel, ConfigDict


class Team(BaseModel):
    """Model for FPL team data from bootstrap-static teams"""

    model_config = ConfigDict(extra="allow")

    # Identifiers
    id: int
    code: int
    name: str
    short_name: str
    pulse_id: int

    # League standing
    position: int
    played: int
    points: int
    win: int
    draw: int
    loss: int

    # Strength ratings
    strength: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int

    # Status
    unavailable: bool
