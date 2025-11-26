from typing import List

import pandas as pd

from fplstat.api.models import Element


def transform_players(data: List[Element]) -> pd.DataFrame:
    """Transform a list of Element models into a DataFrame with additional stats"""

    # Convert Pydantic model to Pandas DataFrame
    df = pd.DataFrame([d.model_dump() for d in data])

    # Drop players with zero minutes played
    df = df.query("minutes > 0")

    # calculate additional per 90 stats
    df = df.assign(
        gi=lambda x: x.goals_scored + x.assists,
        p_90=lambda x: x.total_points / x.minutes * 90,
        g_90=lambda x: x.goals_scored / x.minutes * 90,
        a_90=lambda x: x.assists / x.minutes * 90,
        gi_90=lambda x: (x.goals_scored + x.assists) / x.minutes * 90,
        bps_90=lambda x: x.bps / x.minutes * 90,
        i_90=lambda x: x.influence / x.minutes * 90,
        c_90=lambda x: x.creativity / x.minutes * 90,
        t_90=lambda x: x.threat / x.minutes * 90,
        ict_90=lambda x: x.ict_index / x.minutes * 90,
    )

    return df
