# Expected Points (xP)

## Overview

Expected Points (xP) is a metric that quantifies how many Fantasy Premier League points a player *should have* earned based on the quality of their underlying performances, similar to how Expected Goals (xG) measures goal-scoring opportunities.

**Key principle**: xP reflects the quality of chances and situations a player has been involved in, not their actual outcomes. It helps identify players who may be over-performing or under-performing relative to their underlying stats.

## Philosophy

Just like Expected Goals (xG):

- xP is **retrospective**, not predictive
- It measures the quality of opportunities and situations
- It uses underlying "expected" metrics (xG, xA, xGC) rather than actual outcomes
- Differences between actual points and xP can indicate luck or finishing quality

## Calculation

The xP calculation applies all official FPL scoring rules to expected and actual statistics:

### Appearance Points

- **1 point** for every game played
- **+1 point** for starts (60+ minutes)

### Goals (Position-dependent)

- **Goalkeepers & Defenders**: 6 points per expected goal
- **Midfielders**: 5 points per expected goal
- **Forwards**: 4 points per expected goal

### Assists

- **All positions**: 3 points per expected assist

### Clean Sheets

Clean sheet probability is estimated from expected goals conceded (xGC) using the Poisson distribution:

- **Probability**: `e^(-xGC)` (Poisson probability of zero goals)
- **Goalkeepers & Defenders**: 4 points × probability
- **Midfielders**: 1 point × probability
- **Forwards**: 0 points

**Example probabilities:**

- xGC = 0.5 → ~61% clean sheet chance → 2.4 points (GK/DEF)
- xGC = 1.0 → ~37% clean sheet chance → 1.5 points (GK/DEF)
- xGC = 2.0 → ~14% clean sheet chance → 0.5 points (GK/DEF)

### Goals Conceded

- **Goalkeepers & Defenders**: -0.5 points per expected goal conceded
- **Midfielders & Forwards**: 0 points

### Saves

- **Goalkeepers only**: 1 point per 3 saves (actual saves)
- **Other positions**: 0 points

### Defensive Contributions

FPL awards regular points for defensive actions (clearances, blocks, interceptions). The calculation differs by position:

- **Defenders**: 2 points per 10 defensive contributions
- **Midfielders & Forwards**: 2 points per 12 defensive contributions
- **Goalkeepers**: 0 points (not included in this metric)

### Penalties

- **Penalty saves**: +5 points (actual)
- **Penalty misses**: -2 points (actual)

### Disciplinary

- **Yellow cards**: -1 point (actual)
- **Red cards**: -3 points (actual)
- **Own goals**: -2 points (actual)

### Bonus Points

- Actual bonus points earned (no expected metric available)

## Formula

```python
xP = (
    games_played + starts
    + (6 × xG) for GK/DEF
    + (5 × xG) for MID
    + (4 × xG) for FWD
    + (3 × xA) for all
    + (4 × e^(-xGC)) for GK/DEF
    + (e^(-xGC)) for MID
    - (0.5 × xGC) for GK/DEF
    + (saves ÷ 3) for GK
    + (2 × defensive_contribution ÷ 10) for DEF
    + (2 × defensive_contribution ÷ 12) for MID/FWD
    + (5 × penalty_saves)
    - (2 × penalty_misses)
    - yellow_cards
    - (3 × red_cards)
    - (2 × own_goals)
    + bonus
)
```

## Interpretation

### xP > Actual Points

Player has been unlucky or finishing below expectation. They may be due for positive regression.

**Example**: A forward with 2.5 xG but only 1 actual goal has underperformed their xP.

### xP < Actual Points

Player has been lucky or finishing above expectation. They may regress toward their xP.

**Example**: A midfielder scoring from two low-quality chances (0.5 combined xG) has overperformed their xP.

### xP ≈ Actual Points

Player's output matches the quality of their chances - sustainable performance.

## Per-90 Version

Expected Points per 90 (xP_90) normalizes the metric for playing time:

```python
xP_90 = (xP ÷ minutes) × 90
```

This allows fair comparison between players with different amounts of playing time.

## Limitations

1. **Bonus points** use actual values (no expected bonus metric exists)
1. **Disciplinary actions** use actual cards (difficult to model expected cards)
1. **Penalties, saves, own goals** use actual values (rare events, small samples)
1. **Clean sheet estimation** uses Poisson distribution (assumes goals follow Poisson process)
1. **Defensive contribution** formula is specific to FPL's implementation

## Use Cases

- Identify players outperforming or underperforming their underlying stats
- Find value picks who have been unlucky with returns
- Compare players on underlying quality rather than actual outcomes
- Analyze fixture difficulty impact on defensive stats (xGC)
