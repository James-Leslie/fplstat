# Usage Guides

This guide covers common operations and usage patterns for FPLstat.

## Getting Player Data

### Basic Usage

```python
from fplstat import FPLStat

fpl = FPLStat()
players = fpl.get_players()
```

### Understanding the Output

The `get_players()` method returns a pandas DataFrame with:

- Only players who have played minutes this season (`minutes > 0`)
- Only players available for selection (`can_select == True`)
- Price converted from API format (tenths) to millions (e.g., 125 becomes 12.5)
- Computed statistics like `goal_involvements`, `expected_points`, and per-90 metrics

See the [Column Reference](columns.md) for complete column documentation.

## Common DataFrame Operations

### Filter by Position

Position IDs: 1=GK, 2=DEF, 3=MID, 4=FWD

```python
# Get all midfielders
midfielders = players[players['position_id'] == 3]

# Get defenders and goalkeepers
defenders_gks = players[players['position_id'].isin([1, 2])]
```

### Filter by Team

```python
# Get players from a specific team
team_players = players[players['team_id'] == 1]
```

### Sort by Expected Points

```python
# Top 10 players by expected points
top_xp = players.nlargest(10, 'expected_points')

# Top 10 by expected points per 90 minutes
top_xp_90 = players.nlargest(10, 'expected_points_per_90')
```

### Find Value Picks

```python
# Players with xP > actual points (potentially unlucky, may improve)
underperformers = players[players['expected_points'] > players['points']]

# Best value: high xP per 90 at low price
value_picks = players[players['price'] < 6.0].nlargest(10, 'expected_points_per_90')
```

### Compare Expected vs Actual

```python
# Add a luck metric
players['luck'] = players['points'] - players['expected_points']

# Most lucky players (outperforming expectations)
lucky = players.nlargest(10, 'luck')

# Most unlucky players (underperforming expectations)
unlucky = players.nsmallest(10, 'luck')
```

## Getting Fixture Data

### Basic Usage

```python
fixtures = fpl.get_fixtures()
```

### Filtering Fixtures

```python
# Upcoming fixtures (not yet played)
upcoming = fixtures[~fixtures['finished']]

# Completed fixtures
completed = fixtures[fixtures['finished']]

# Fixtures for a specific gameweek
gw5 = fixtures[fixtures['event'] == 5]

# Fixtures for a specific team
team_fixtures = fixtures[
    (fixtures['team_h'] == 1) | (fixtures['team_a'] == 1)
]
```

## Accessing Raw API Data

FPLstat provides access to the underlying API data via properties.

### Via Properties (Lazy-loaded)

```python
fpl = FPLStat()

# Bootstrap-static data (BootstrapStaticResponse)
raw = fpl.raw_data

# Access teams
teams = raw.teams  # List[Team]

# Access events (gameweeks)
events = raw.events  # List[Event]

# Access element types (positions)
positions = raw.element_types  # List[ElementType]

# Access all players (unfiltered)
all_elements = raw.elements  # List[Element]
```

### Via APIClient (Direct Access)

```python
from fplstat.api import APIClient

client = APIClient()

# Bootstrap-static (validated Pydantic model)
bootstrap = client.get_bootstrap_static()

# Fixtures (validated Pydantic model)
fixtures = client.get_fixtures()
```

## Getting Single Player Data

The `get_element_summary` endpoint provides detailed per-gameweek history for a specific player.

### Finding a Player's ID

```python
fpl = FPLStat()
players = fpl.get_players()

# Find a player by name
salah = players[players['short_name'] == 'Salah']
player_id = salah['player_id'].iloc[0]
```

### Fetching Player History

```python
from fplstat.api import APIClient

client = APIClient()
player_data = client.get_element_summary(element_id=player_id)

# Returns dict with keys:
# - 'history': Per-gameweek stats for current season
# - 'history_past': Per-season stats for previous seasons
# - 'fixtures': Upcoming fixtures for the player
```

## Error Handling

### Network Errors

```python
import requests
from fplstat import FPLStat

try:
    fpl = FPLStat()
    players = fpl.get_players()
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
```

### Rate Limiting

The FPL API may rate limit requests. When making multiple requests, add delays:

```python
import time
from fplstat.api import APIClient

client = APIClient()
player_ids = [1, 2, 3, 4, 5]

for player_id in player_ids:
    data = client.get_element_summary(player_id)
    time.sleep(1)  # 1 second delay between requests
```

## Data Freshness

### Update Frequency

- FPL updates data after each Premier League match
- Live data during matches may have slight delays
- Historical stats are typically finalized within hours of match completion

### Caching Behavior

FPLstat caches data within a single `FPLStat` instance:

```python
# Data is cached for this instance
fpl = FPLStat()
players1 = fpl.get_players()  # Fetches from API
players2 = fpl.get_players()  # Uses cached data

# For fresh data, create a new instance
fpl = FPLStat()
players_fresh = fpl.get_players()  # Fetches from API again
```

## Understanding Expected Points (xP)

FPLstat computes `expected_points` using underlying xG (expected goals) and xA (expected assists) metrics combined with FPL scoring rules.

See [Expected Points (xP)](expected-points.md) for the full methodology.

### Quick Interpretation

| Scenario                         | Meaning                            |
| -------------------------------- | ---------------------------------- |
| xP > Points                      | Player unlucky, may improve        |
| xP < Points                      | Player overperforming, may regress |
| xP approximately equal to Points | Sustainable performance            |
