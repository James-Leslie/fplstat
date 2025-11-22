from fplstat.api.models import Element


def transform_player(data: Element) -> dict:
    """Element -> dict (ready for DataFrame)"""

    data = data.model_dump()

    # Example transformation: convert now_cost from int to float in millions
    data["now_cost"] = data["now_cost"] / 10.0

    return data
