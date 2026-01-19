from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class ElementType(BaseModel):
    """Model for FPL element type (position) data from bootstrap-static element_types"""

    model_config = ConfigDict(extra="allow")

    # Identifiers
    id: int
    singular_name: str
    singular_name_short: str
    plural_name: str
    plural_name_short: str

    # Squad requirements
    squad_select: int
    squad_min_play: int
    squad_max_play: int
    squad_min_select: Optional[int] = None
    squad_max_select: Optional[int] = None

    # Stats
    element_count: int

    # UI
    ui_shirt_specific: bool
    sub_positions_locked: List[int]
