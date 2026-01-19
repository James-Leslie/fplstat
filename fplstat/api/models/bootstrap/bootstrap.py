from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict

from .element import Element
from .element_type import ElementType
from .event import Event
from .team import Team


class BootstrapStaticResponse(BaseModel):
    """Response model for the bootstrap-static endpoint"""

    model_config = ConfigDict(extra="allow")  # Allow extra fields FPL might add

    chips: List[Dict[str, Any]]
    element_stats: List[Dict[str, Any]]
    element_types: List[ElementType]
    elements: List[Element]
    events: List[Event]
    game_config: Dict[str, Any]
    game_settings: Dict[str, Any]
    phases: List[Dict[str, Any]]
    teams: List[Team]
    total_players: int
