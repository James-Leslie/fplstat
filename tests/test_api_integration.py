import warnings

import pandas as pd
import pytest

from fplstat import FPLStat
from fplstat.api import APIClient
from fplstat.api.models import (
    BootstrapStaticResponse,
    Element,
    ElementType,
    Event,
    Fixture,
    FixtureStat,
    Team,
)


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


@pytest.fixture(scope="session")
def fixtures_data():
    """Get real fixtures data once per test session (cached for performance)"""
    try:
        client = APIClient()
        return client.get_fixtures()
    except Exception as e:
        pytest.skip(f"Skipping tests: API unavailable ({e})")


@pytest.fixture
def sample_fixture(fixtures_data):
    """Get a real fixture from live API data"""
    # Return the first fixture from real API data
    return fixtures_data.fixtures[0]


def test_fixture_model(sample_fixture):
    """Test that a sample fixture from live API data is a valid Fixture model"""
    # The `sample_fixture` is already a `Fixture` instance, as Pydantic
    # validation occurs within the `APIClient`. This test verifies the
    # instance type and presence of key attributes.
    assert isinstance(sample_fixture, Fixture)
    assert hasattr(sample_fixture, "team_h")
    assert hasattr(sample_fixture, "team_a")
    assert hasattr(sample_fixture, "kickoff_time")


def test_get_fixtures():
    """Test that get_fixtures() returns a proper DataFrame"""
    client = FPLStat()
    fixtures_df = client.get_fixtures()

    # Check it's a DataFrame
    assert isinstance(fixtures_df, pd.DataFrame)

    # Check it has data
    assert len(fixtures_df) > 0

    # Check it has expected columns
    expected_columns = {"team_h", "team_a", "kickoff_time", "finished"}
    assert expected_columns.issubset(fixtures_df.columns)


@pytest.fixture
def sample_team(bootstrap_static_data):
    """Get a real team from live API data"""
    return bootstrap_static_data.teams[0]


def test_team_model(sample_team):
    """Test that a sample team from live API data validates against Team model"""
    assert isinstance(sample_team, Team)
    assert hasattr(sample_team, "name")
    assert hasattr(sample_team, "short_name")
    assert hasattr(sample_team, "strength")


@pytest.fixture
def sample_event(bootstrap_static_data):
    """Get a real event from live API data"""
    return bootstrap_static_data.events[0]


def test_event_model(sample_event):
    """Test that a sample event from live API data validates against Event model"""
    assert isinstance(sample_event, Event)
    assert hasattr(sample_event, "name")
    assert hasattr(sample_event, "deadline_time")
    assert hasattr(sample_event, "finished")


@pytest.fixture
def sample_element_type(bootstrap_static_data):
    """Get a real element type from live API data"""
    return bootstrap_static_data.element_types[0]


def test_element_type_model(sample_element_type):
    """Test that a sample element type validates against ElementType model"""
    assert isinstance(sample_element_type, ElementType)
    assert hasattr(sample_element_type, "singular_name")
    assert hasattr(sample_element_type, "plural_name")
    assert hasattr(sample_element_type, "squad_select")


def test_fixture_stat_model(fixtures_data):
    """Test that fixture stats from live API data validate against FixtureStat model"""
    # Find a finished fixture with stats
    finished_fixtures = [f for f in fixtures_data.fixtures if f.finished]
    if not finished_fixtures:
        pytest.skip("No finished fixtures available for testing stats")

    fixture = finished_fixtures[0]
    assert isinstance(fixture.stats, list)
    if fixture.stats:
        stat = fixture.stats[0]
        assert isinstance(stat, FixtureStat)
        assert hasattr(stat, "identifier")
        assert hasattr(stat, "a")
        assert hasattr(stat, "h")
