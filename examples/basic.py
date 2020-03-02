import hockeydata


def main():

    shifts = hockeydata.get_game_shifts('2018020028')
    res = hockeydata.get_season_play_by_play(2018)
    print(res)

if __name__ == '__main__':
    main()