### hockeydata
[![Build Status](https://travis-ci.org/adamfillion/hockeydata.svg?branch=master)](https://travis-ci.org/adamfillion/hockeydata)

A library and CLI tool for collecting live data from NHL games. 

All data is accessible identically through the Python API or command-line tool.

**CONTRIBUTIONS ENCOURAGED**

#### Install

Compatible with Python3.5+.

Use `pip`:

```bash
python3 -m pip install hockeydata
```

Or from source:

```bash
git clone https://github.com/adamfillion/hockeydata.git ~/dev/hockeydata
python3 -m pip install ~/dev/hockeydata
# or
python3 ~/dev/hockeydata/setup.py install
```

This will add a new command to your system, `hockeydata`.

#### What this Tool Is

This tool was created out of a need for a reliable data pipeline for NHL live data - something which the NHL 
*kind of* provides, but not really. Data is scraped from several public sources, checked for errors, and merged when 
possible.

Due to the dynamic nature of stats reporting in the NHL, it is possible for data to be missing/incorrect in this tool's
output. My philosophy when writing this was that **its better to output nothing than to output something wrong** - because
 I want downstream applications to be able to trust that my output is correct - and for the purposes of analysis missing 
 data points are normally better then wrong data points.
 
Parsing errors are logged and can be fixed after the fact by me or contributors. 


#### The GameID

The key to NHL stats data is the "gameid", an ID which uniquely identifies every game. 
It's a 10-digit numeric code which is formatted like so:

    2019020565
 
This tool uses the gameid to obtain data for specific games. You can use the `list_games` python function or the `list-games` CLI 
command to get game ID's.

#### Usage - library

Let's say you want to write a script which you'll run once a day, which will find all games played on the given day and download all play-by-play data for each game into a CSV file, labelled with the game's ID.

```python
from hockeydata import get_game_shifts, get_season_play_by_play, get_play_by_plays, list_games

# get a full year of games id
game_list = list_games('2018-01-01', '2019-01-01')

# get play by play data for a game
df = get_play_by_plays('2018021000')

# get shift data for a game
df = get_game_shifts('2018021000')

# get play by play data for an entire season. WARNING this will take a while...approx. 20 seconds per game on my machine.
df = get_season_play_by_play(2017)
```

##### Formatters

The output package formats the data in a few different formats, for example CSV, JSON, or a 
text-based table. Each formatter has a `dump` and `dumps` function which work similarly to Python's `json` module. 
If you want to save your data as JSON, for example:

```python
from hockeydata import list_games
from hockeydata.output import json

plays = list_games('2018021000')
with open('file.json', 'w') as f:
    json.dump(plays, f)

```

#### Usage - CLI

```sh
Usage: hockeydata [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list-games  Gets game_ids for a date range
  scrape      Scrape a game/list for all of its live data.
  shifts      Scrape a game for its shift data.

```

Use the `--output-format` or `-o`  to format the data in your format of choice: csv, json, pretty (which is a nice table), 
or text (which is a basic table). Internally the data is normally collected as Dataframes, so you can add additional
output formats using Pandas' nice formatting functions.

```bash
nhl list-plays 2019020406 --output-format csv > 2019020406.csv  # create a new file
nhl list-plays 2019020406 --output-format csv >> plays.csv  # append result to plays.csv
```

##### list-games

```bash
Usage: hockeydata list-games [OPTIONS] [START_DATE] [END_DATE]

  Gets game_ids for a date range

Options:
  -o, --output-format [text|csv|json|pretty]
  --help                          Show this message and exit.

```

##### game-info

```bash
hockeydata game-info --help
Usage: hockeydata game-info [OPTIONS] [GAME_IDS]...

  Get high-level data about a game

Options:
  -o, --output-format [text|csv|json|pretty]
  --help                          Show this message and exit.
```

##### scrape

```bash
$ hockeydata scrape --help
Usage: hockeydata scrape [OPTIONS] [GAME_IDS]...

  Scrape a game/list for all of its live data.

Options:
  -o, --output-format [text|csv|json|pretty]
  --help                          Show this message and exit.

```

##### shifts

```bash
hockeydata shifts --help
Usage: hockeydata shifts [OPTIONS] [GAME_IDS]...

  Scrape a game for its shift data.

Options:
  -o, --output-format [text|csv|json|pretty]
  --help                          Show this message and exit.

```

### Formatters

The currently available formatters are `csv`, `json`, `pretty` and `text`.

Using the `text` output format, we get a pretty-printed table with the data:

```text
        GAME_ID  PERIOD TEAM            PLAYER  PLAYER_ID   START     END  DURATION
0    2018021000       1  CHI      DUNCAN KEITH    8470281     0.0    49.0      49.0
1    2018021000       1  L.A      DION PHANEUF    8470602     0.0    47.0      47.0
2    2018021000       1  L.A      DUSTIN BROWN    8470606     0.0    47.0      47.0
3    2018021000       1  CHI    BRENT SEABROOK    8470607     0.0    49.0      49.0
...
763  2018021000       3  L.A          MATT ROY    8478911  1190.0  1200.0      10.0

```


Using the `csv` formatter, we get csv-like output:

```csv
,GAME_ID,PERIOD,TEAM,PLAYER,PLAYER_ID,START,END,DURATION
0,2018021000,1,CHI,DUNCAN KEITH,8470281,0.0,49.0,49.0
1,2018021000,1,L.A,DION PHANEUF,8470602,0.0,47.0,47.0
2,2018021000,1,L.A,DUSTIN BROWN,8470606,0.0,47.0,47.0
3,2018021000,1,CHI,BRENT SEABROOK,8470607,0.0,49.0,49.0
...
763,2018021000,3,L.A,MATT ROY,8478911,1190.0,1200.0,10.0


```

using the `json` formatter, we get json-like output:

```json
[{"GAME_ID":"2018021000","PERIOD":1,"TEAM":"CHI","PLAYER":"DUNCAN KEITH","PLAYER_ID":8470281,"START":0.0,"END":49.0,
"DURATION":49.0},{"GAME_ID":"2018021000","PERIOD":1,"TEAM":"L.A","PLAYER":"DION PHANEUF","PLAYER_ID":8470602,"START":0.0,
"END":47.0,"DURATION":47.0},{"GAME_ID":"2018021000","PERIOD":1,"TEAM":"L.A","PLAYER":"DUSTIN BROWN","PLAYER_ID":8470606,
"START":0.0,"END":47.0,"DURATION":47.0}, ...]
```

using the `pretty` formatter, we get a pretty table:

```text
+-----+------------+----------+--------+------------------+-------------+---------+-------+------------+
|     |    GAME_ID |   PERIOD | TEAM   | PLAYER           |   PLAYER_ID |   START |   END |   DURATION |
|-----+------------+----------+--------+------------------+-------------+---------+-------+------------|
|   0 | 2018021000 |        1 | CHI    | DUNCAN KEITH     |     8470281 |       0 |    49 |         49 |
|   1 | 2018021000 |        1 | L.A    | DION PHANEUF     |     8470602 |       0 |    47 |         47 |
|   2 | 2018021000 |        1 | L.A    | DUSTIN BROWN     |     8470606 |       0 |    47 |         47 |
...
| 763 | 2018021000 |        3 | L.A    | MATT ROY         |     8478911 |    1190 |  1200 |         10 |
+-----+------------+----------+--------+------------------+-------------+---------+-------+------------+

```

#### Acknowledgments

These projects helped greatly with the development of this tool:
- Dword4's [NHL API Documentation](https://github.com/dword4/nhlapi)
- Evolving Wild's [R Scraping Application](https://github.com/evolvingwild/evolving-hockey)
