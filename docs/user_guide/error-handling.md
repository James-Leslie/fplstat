# Error Handling

## Network Errors

```python
import requests
from fplstat import FPLStat

try:
    fpl = FPLStat()
    players = fpl.get_players()
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
```

## Rate Limiting

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
