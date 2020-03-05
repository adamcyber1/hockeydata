import hockeydata


def main():

    #shifts = hockeydata.get_game_shifts('2018020028')
    #res = hockeydata.get_season_play_by_play(2018)
    #print(res)
    # initializing dictionary
    old_dict = {
        "N.J": 1, "NYI": 2, "NYR": 3, "PHI": 4, "PIT": 5, "BOS": 6, "BUF": 7, "MTL": 8, "OTT": 9, "TOR": 10, "ATL": 11, "CAR": 12, "FLA": 13, "T.B": 14,
        "WSH": 15, "CHI": 16, "DET": 17, "NSH": 18, "STL": 19, "CGY": 20, "COL": 21, "EDM": 22, "VAN": 23, "ANA": 24, "DAL": 25, "L.A": 26, "ARI": 27, "S.J": 28,
        "CBJ": 29, "MIN": 30, "WPG": 52, "ARI": 53, "VGK": 54
    }

    new_dict = dict([(value, key) for key, value in old_dict.items()])

    # Printing original dictionary
    print ("Original dictionary is : ")
    print(old_dict)

    print()

    # Printing new dictionary after swapping keys and values
    print ("Dictionary after swapping is :  ")
    print("keys: values")
    for i in new_dict:
        print(i, " :  ", new_dict[i])

if __name__ == '__main__':
    main()