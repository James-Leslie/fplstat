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
        return client.get_bootstrap_static()
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


def test_price_transformation(sample_player):
    """Test that PlayerTransformer converts price from API units to millions"""
    original_price = sample_player["now_cost"]
    transformed = PlayerTransformer.transform(sample_player)

    # Only test the price transformation logic
    assert transformed["now_cost"] == original_price / 10


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
