# Accessing Raw API Data

FPLstat provides access to the underlying API data via properties.

## Via Properties (Lazy-loaded)

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

## Via APIClient (Direct Access)

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
