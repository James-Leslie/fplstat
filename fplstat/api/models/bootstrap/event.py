from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class ChipPlay(BaseModel):
    """Model for chip usage statistics in an event"""

    model_config = ConfigDict(extra="allow")

    chip_name: str
    num_played: int


class Event(BaseModel):
    """Model for FPL event (gameweek) data from bootstrap-static events"""

    model_config = ConfigDict(extra="allow")

    # Identifiers
    id: int
    name: str

    # Scheduling
    deadline_time: datetime
    release_time: Optional[datetime] = None

    # Status flags
    finished: bool
    data_checked: bool
    is_previous: bool
    is_current: bool
    is_next: bool

    # Performance metrics (null for future gameweeks)
    average_entry_score: Optional[int] = None
    highest_score: Optional[int] = None
    highest_scoring_entry: Optional[int] = None

    # Participants
    ranked_count: Optional[int] = None

    # Chip usage
    chip_plays: List[ChipPlay]

    # Player stats (null for future gameweeks)
    most_selected: Optional[int] = None
    most_captained: Optional[int] = None
    most_vice_captained: Optional[int] = None
    most_transferred_in: Optional[int] = None
    top_element: Optional[int] = None
    top_element_info: Optional[Dict[str, Any]] = None

    # Transfer stats
    transfers_made: Optional[int] = None
