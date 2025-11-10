# FPLstat
FPLstat is a Python library that provides easy access to Fantasy Premier League (FPL) data. It allows users to retrieve and analyze player statistics, team information, and gameweek details through a simple and intuitive interface.

## Installation

=== "`uv`"

    ``` sh
    uv add fplstat # (1)!
    ```
    
    1. If you haven't heard of [`uv`](https://docs.astral.sh/uv/), we highly recommend checking it out!

=== "`pip`"

    ``` sh
    pip install fplstat
    ```

## Usage

``` py
from fplstat import FPLstat

fpl = FPLstat()
```