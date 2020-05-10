from hockeydata import get_game_shifts, get_season_play_by_play, get_play_by_plays, list_games
from hockeydata.output import json, csv

def main():
    # get today's games ids
    game_list = list_games('2018-01-01', '2019-01-01')

    # get a full year of games id
    game_list = list_games('2018-01-01', '2019-01-01')

    # get play by play data for a game
    pbp = get_play_by_plays('2018021000')

    

    # get shift data for a game
    shifts = get_game_shifts('2018021000')

    # use the formatters to put your data in different formats (you could just use pandas builtin functions if you want :) )
    pbp_json = json.dumps(pbp)
    pbp_csv = csv.dumps(pbp)

    pbp_dict = json.to_dict(pbp)

    print(pbp_dict)
    # dump it to a file if you want
    # pbp_json = json.dump(pbp, file_handle)
    # pbp_csv = csv.dump(pbp, file_handle)

if __name__ == '__main__':
    main()