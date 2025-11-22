from typing import Any, Dict, List

from pydantic import BaseModel


class FixturesResponse(BaseModel):
    """Response model for the fixtures endpoint"""

    fixtures: List[Dict[str, Any]]