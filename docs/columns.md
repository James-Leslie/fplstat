# Column Reference

This page documents all columns in the DataFrame returned by `get_players()`.

## Data Filtering

The DataFrame includes only players where:

- `minutes > 0` (has played this season)
- `can_select == True` (available for selection)

## Identifiers

| Column        | Type | Description                         |
| ------------- | ---- | ----------------------------------- |
| `player_id`   | int  | Unique player identifier            |
| `position_id` | int  | Position: 1=GK, 2=DEF, 3=MID, 4=FWD |
| `team_id`     | int  | Team identifier                     |
| `short_name`  | str  | Display name (e.g., "Salah")        |
| `full_name`   | str  | First + second name (computed)      |

## Pricing and Ownership

| Column          | Type  | Description                            |
| --------------- | ----- | -------------------------------------- |
| `price`         | float | Current price in millions (e.g., 12.5) |
| `ownership_pct` | float | Percentage of managers who own player  |

## Game Stats

| Column                            | Type | Description                       |
| --------------------------------- | ---- | --------------------------------- |
| `games_played`                    | int  | Number of games played (computed) |
| `starts`                          | int  | Number of starts (60+ minutes)    |
| `minutes`                         | int  | Total minutes played              |
| `points`                          | int  | Total FPL points this season      |
| `goals_scored`                    | int  | Goals scored                      |
| `assists`                         | int  | Assists                           |
| `goal_involvements`               | int  | Goals + assists (computed)        |
| `clean_sheets`                    | int  | Clean sheets                      |
| `goals_conceded`                  | int  | Goals conceded                    |
| `own_goals`                       | int  | Own goals                         |
| `penalties_saved`                 | int  | Penalties saved (GK)              |
| `penalties_missed`                | int  | Penalties missed                  |
| `yellow_cards`                    | int  | Yellow cards                      |
| `red_cards`                       | int  | Red cards                         |
| `saves`                           | int  | Saves (GK)                        |
| `clearances_blocks_interceptions` | int  | Defensive actions                 |
| `recoveries`                      | int  | Ball recoveries                   |
| `tackles`                         | int  | Tackles made                      |
| `defensive_contribution`          | int  | Combined defensive actions        |
| `bonus`                           | int  | Bonus points earned               |
| `bps`                             | int  | Bonus points system score         |

## Expected Stats

| Column                       | Type  | Description                                         |
| ---------------------------- | ----- | --------------------------------------------------- |
| `expected_goals`             | float | xG for the season                                   |
| `expected_assists`           | float | xA for the season                                   |
| `expected_goal_involvements` | float | xG + xA                                             |
| `expected_goals_conceded`    | float | xGC for the season                                  |
| `expected_points`            | float | Computed xP (see [methodology](expected-points.md)) |

## Per-90 Stats

All per-90 stats are computed as `(stat / minutes) * 90`.

| Column                              | Type  | Description                       |
| ----------------------------------- | ----- | --------------------------------- |
| `starts_per_90`                     | float | Starts per 90 minutes             |
| `points_per_90`                     | float | Points per 90 minutes (computed)  |
| `goals_per_90`                      | float | Goals per 90 minutes (computed)   |
| `assists_per_90`                    | float | Assists per 90 minutes (computed) |
| `goal_involvements_per_90`          | float | G+A per 90 minutes (computed)     |
| `bonus_per_90`                      | float | Bonus points per 90 (computed)    |
| `defensive_contribution_per_90`     | float | Defensive actions per 90          |
| `goals_conceded_per_90`             | float | Goals conceded per 90             |
| `saves_per_90`                      | float | Saves per 90 (GK)                 |
| `clean_sheets_per_90`               | float | Clean sheets per 90               |
| `expected_points_per_90`            | float | xP per 90 minutes (computed)      |
| `expected_goals_per_90`             | float | xG per 90 minutes                 |
| `expected_assists_per_90`           | float | xA per 90 minutes                 |
| `expected_goal_involvements_per_90` | float | xG+xA per 90                      |
| `expected_goals_conceded_per_90`    | float | xGC per 90                        |

## ICT Index

| Column       | Type  | Description        |
| ------------ | ----- | ------------------ |
| `influence`  | float | Influence score    |
| `creativity` | float | Creativity score   |
| `threat`     | float | Threat score       |
| `ict_index`  | float | Combined ICT score |

## Performance Metrics

| Column            | Type  | Description             |
| ----------------- | ----- | ----------------------- |
| `points_per_game` | float | Average points per game |
| `form`            | float | Recent form rating      |

## Status and Availability

| Column        | Type     | Description                                             |
| ------------- | -------- | ------------------------------------------------------- |
| `status`      | str      | 'a'=available, 'i'=injured, 'd'=doubtful, 's'=suspended |
| `scout_risks` | str      | Risk indicators from FPL scout                          |
| `news`        | str      | Latest news about player                                |
| `news_added`  | datetime | When news was added                                     |

## FPL Predictions

| Column    | Type  | Description                          |
| --------- | ----- | ------------------------------------ |
| `ep_this` | float | FPL's predicted points this gameweek |
| `ep_next` | float | FPL's predicted points next gameweek |

## Column Name Mapping

The FPL API uses different column names than FPLstat. Here's the mapping:

| API Name              | FPLstat Name               |
| --------------------- | -------------------------- |
| `id`                  | `player_id`                |
| `element_type`        | `position_id`              |
| `team`                | `team_id`                  |
| `web_name`            | `short_name`               |
| `now_cost`            | `price`                    |
| `selected_by_percent` | `ownership_pct`            |
| `total_points`        | `points`                   |
| `gi`                  | `goal_involvements`        |
| `xP`                  | `expected_points`          |
| `p_90`                | `points_per_90`            |
| `g_90`                | `goals_per_90`             |
| `a_90`                | `assists_per_90`           |
| `gi_90`               | `goal_involvements_per_90` |
| `b_90`                | `bonus_per_90`             |
| `xP_90`               | `expected_points_per_90`   |
