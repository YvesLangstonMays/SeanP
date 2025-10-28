import nflreadpy as nfl

seanp_teams = ["NYG", "PHI", "DAL", "NO"]  # use team abbreviations

# Load player stats (regular season)
qb_stats = nfl.load_pbp_data("player_stats")

# Filter for QBs and Sean Payton teams
peyton_qbs = qb_stats[
    (qb_stats["position"] == "QB") & (qb_stats["team"].isin(seanp_teams))
]

peyton_qbs
