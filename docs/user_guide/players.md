# Getting Player Data

## Basic Usage

```python
from fplstat import FPLStat

fpl = FPLStat()
players = fpl.get_players()
```

## Understanding the Output

The `get_players()` method returns a pandas DataFrame with:

- Only players who have played minutes this season (`minutes > 0`)
- Only players available for selection (`can_select == True`)
- Price converted from API format (tenths) to millions (e.g., 125 becomes 12.5)
- Computed statistics like `goal_involvements`, `expected_points`, and per-90 metrics

See the [Column Reference](../columns.md) for complete column documentation.

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

## Understanding Expected Points (xP)

FPLstat computes `expected_points` using underlying xG (expected goals) and xA (expected assists) metrics combined with FPL scoring rules.

See [Expected Points (xP)](../expected-points.md) for the full methodology.

### Quick Interpretation

| Scenario                         | Meaning                            |
| -------------------------------- | ---------------------------------- |
| xP > Points                      | Player unlucky, may improve        |
| xP < Points                      | Player overperforming, may regress |
| xP approximately equal to Points | Sustainable performance            |
