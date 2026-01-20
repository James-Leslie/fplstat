# Getting Fixture Data

## Basic Usage

```python
fixtures = fpl.get_fixtures()
```

## Filtering Fixtures

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
