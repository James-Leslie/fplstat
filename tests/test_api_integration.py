import warnings

from fplstat.api import APIClient
from fplstat.models import BootstrapStaticResponse


def test_fetch_bootstrap_static_structure():
    """Verify the API response matches our expected structure"""
    client = APIClient()
    data = client.fetch_bootstrap_static()

    # This will raise ValidationError if structure doesn't match

    # Validate structure
    response = BootstrapStaticResponse.model_validate(data)

    # Check for new fields
    expected_fields = set(BootstrapStaticResponse.model_fields.keys())
    actual_fields = set(data.model_dump().keys())
    new_fields = actual_fields - expected_fields

    if new_fields:
        warnings.warn(f"⚠️ New fields detected in API: {new_fields}")

    # Additional sanity checks
    assert len(response.teams) == 20  # PL has 20 teams
