from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict

from .element import Element


class BootstrapStaticResponse(BaseModel):
    """Response model for the bootstrap-static endpoint"""

    model_config = ConfigDict(extra="allow")  # Allow extra fields FPL might add

    chips: List[Dict[str, Any]]
    element_stats: List[Dict[str, Any]]
    element_types: List[Dict[str, Any]]
    elements: List[Element]
    events: List[Dict[str, Any]]
    game_config: Dict[str, Any]
    game_settings: Dict[str, Any]
    phases: List[Dict[str, Any]]
    teams: List[Dict[str, Any]]
    total_players: int
