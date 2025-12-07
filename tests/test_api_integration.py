import warnings

import pytest

from fplstat.api import APIClient
from fplstat.api.models import BootstrapStaticResponse, Element


@pytest.fixture(scope="session")
def bootstrap_static_data():
    """Get real API data once per test session (cached for performance)"""
    try:
        client = APIClient()
        return client.get_bootstrap_static()
    except Exception as e:
        pytest.skip(f"Skipping tests: API unavailable ({e})")


@pytest.fixture
def sample_player(bootstrap_static_data):
    """Get a real player from live API data"""
    # Return the first player from real API data
    return bootstrap_static_data.elements[0]


def test_bootstrap_static_model(bootstrap_static_data):
    """Verify the API response matches our expected structure"""

    # This will raise ValidationError if structure doesn't match
    response = BootstrapStaticResponse.model_validate(bootstrap_static_data)

    # Check for new fields
    expected_fields = set(BootstrapStaticResponse.model_fields.keys())
    actual_fields = set(bootstrap_static_data.model_dump().keys())
    new_fields = actual_fields - expected_fields

    if new_fields:
        warnings.warn(f"⚠️ New fields detected in API: {new_fields}")

    # Additional sanity checks
    assert len(response.teams) == 20  # PL has 20 teams


def test_element_model(sample_player):
    """Test that a sample player from live API data validates against Element model"""
    # This will raise ValidationError if structure doesn't match
    player = Element.model_validate(sample_player)
    assert isinstance(player, Element)
    assert hasattr(player, "first_name")
    assert hasattr(player, "now_cost")
