"""Test the transformation pipeline from raw API data to business models"""

import pytest

from fplstat.api import APIClient
from fplstat.fplstat import FPLStat
from fplstat.models import Player, PlayerTransformer


@pytest.fixture(scope="session")
def live_api_data():
    """Get real API data once per test session (cached for performance)"""
    try:
        client = APIClient()
        return client.fetch_bootstrap_static()
    except Exception as e:
        pytest.skip(f"Skipping tests: API unavailable ({e})")


@pytest.fixture
def sample_player(live_api_data):
    """Get a real player from live API data"""
    # Return the first player from real API data
    return live_api_data.elements[0]


@pytest.fixture
def sample_players_list(live_api_data):
    """Get a small list of real players for testing"""
    # Return first 3 players for multi-player tests
    return live_api_data.elements[:3]


def test_player_transformer_price_conversion(sample_player):
    """Test that PlayerTransformer correctly converts price units"""
    # Using real API player data - much more realistic!
    original_price = sample_player["now_cost"]  # e.g., 59 from real API

    transformed = PlayerTransformer.transform(sample_player)

    # Test the transformation logic with real data
    expected_price = original_price / 10  # e.g., 59 -> 5.9
    assert transformed["now_cost"] == expected_price

    # Other fields should be unchanged
    assert transformed["web_name"] == sample_player["web_name"]
    assert transformed["id"] == sample_player["id"]


def test_player_model_with_transformed_data(sample_player):
    """Test Player model validation with complete transformed data"""
    # Transform real API data and create Player model
    transformed_data = PlayerTransformer.transform(sample_player)
    player = Player(**transformed_data)

    # Test that transformation + validation worked
    expected_price = sample_player["now_cost"] / 10
    assert player.now_cost == expected_price  # Transformed from real API price
    assert isinstance(player.now_cost, float)
    assert player.web_name == sample_player["web_name"]  # From real API data


def test_full_pipeline_transform_then_validate(sample_player):
    """Test the complete pipeline: raw data → transform → validate"""
    # Step 1: Start with real API data
    original_price = sample_player["now_cost"]

    # Step 2: Transform
    transformed = PlayerTransformer.transform(sample_player)

    # Step 3: Verify transformation
    expected_price = original_price / 10
    assert transformed["now_cost"] == expected_price

    # Step 4: Create Player object (complete pipeline test!)
    player = Player(**transformed)
    assert player.now_cost == expected_price
    assert isinstance(player, Player)


def test_fplstat_integration(sample_players_list):
    """Integration test: FPLStat client with real API data"""
    # Test that FPLStat can handle multiple real players
    fpl = FPLStat()
    players = fpl.get_players()

    # Basic checks
    assert len(players) > 0
    assert isinstance(players[0], Player)
    assert isinstance(players[0].now_cost, float)

    # Check price transformation worked on real data
    # All prices should be reasonable (0.1 to 20.0 millions)
    for player in players[:5]:  # Check first 5
        assert 0.1 <= player.now_cost <= 20.0

    # Test against our known sample data
    assert len(players) >= len(sample_players_list)
