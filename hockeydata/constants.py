NHLAPI_URL = 'https://statsapi.web.nhl.com/api/v1/'
NHLAPI = 'https://statsapi.web.nhl.com/api/v1/'
SHIFTS = 'https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId='
ESPN = 'http://www.espn.com/nhl/gamecast/data/masterFeed?lang=en&isAll=true&gameId='
HTMLREPORTS_URL = 'http://www.nhl.com/scores/htmlreports/'
HTMLREPORTS = 'http://www.nhl.com/scores/htmlreports/'
CURRENT_SEASON = '20192020'
DATABASE_PATH = '/tmp'

GOAL = "GOAL"
SHOT = "SHOT"
MISS = "MISS"
BLOCK = "BLOCK"
HIT = "HIT"
GIVE = "GIVE"
TAKE = "TAKE"
FAC = "FAC"
PENL = "PENL"

SHOT_EVENTS = (GOAL, SHOT)
FENWICK_EVENTS = (GOAL, SHOT, MISS)
CORSI_EVENTS = (GOAL, SHOT, MISS, BLOCK)
MAIN_EVENTS = ("GOAL", "SHOT", "MISS", "BLOCK", "HIT", "GIVE", "TAKE", "FAC", "PENL")

# this is the data that is extracted directly from the HTML report.
HTML_COLUMNS = ['EVENT_INDEX', 'PERIOD', 'STRENGTH', 'GAME_SECONDS', 'EVENT_TYPE', 'EVENT_DESCRIPTION', 'EVENT_DETAIL',
                'EVENT_ZONE', 'EVENT_TEAM', 'EVENT_PLAYER_1', 'EVENT_PLAYER_2', 'EVENT_PLAYER_3',
                'HOME_ON_1', 'HOME_ON_2', 'HOME_ON_3', 'HOME_ON_4', 'HOME_ON_5', 'HOME_ON_6', 'HOME_ON_7',
                'AWAY_ON_1', 'AWAY_ON_2', 'AWAY_ON_3', 'AWAY_ON_4', 'AWAY_ON_5', 'AWAY_ON_6', 'AWAY_ON_7']

# this is the data that is extracted directly from the HTML report + things we can infer from this data.
PBP_COLUMNS = HTML_COLUMNS + ['HOME', 'AWAY', 'GAME_ID', 'DATE', 'HOME_SCORE', 'AWAY_SCORE']

# all of the above + data from other sources (i.e. coordinates)
PBP_COLUMNS_ENHANCED = PBP_COLUMNS + ['X_CORD', 'Y_CORD']

GAME_INFO_COLUMNS = ['GAME_ID', 'GAME_DATE', 'HOME_TEAM_ID', 'HOME_TEAM_FULL_NAME', 'AWAY_TEAM_ID', 'AWAY_TEAM_FULL_NAME',
             'HOME_GOALS', 'AWAY_GOALS', 'RESULT', 'HOME_SHOTS', 'AWAY_SHOTS']


TEAMS = {
    'ANAHEIM DUCKS': 'ANA',
    'ARIZONA COYOTES': 'ARI',
    'ATLANTA THRASHERS': 'ATL',
    'BOSTON BRUINS': 'BOS',
    'BUFFALO SABRES': 'BUF',
    'CAROLINA HURRICANES': 'CAR',
    'COLUMBUS BLUE JACKETS': 'CBJ',
    'CALGARY FLAMES': 'CGY',
    'CHICAGO BLACKHAWKS': 'CHI',
    'COLORADO AVALANCHE': 'COL',
    'DALLAS STARS': 'DAL',
    'DETROIT RED WINGS': 'DET',
    'EDMONTON OILERS': 'EDM',
    'FLORIDA PANTHERS': 'FLA',
    'LOS ANGELES KINGS': 'L.A',
    'MINNESOTA WILD': 'MIN',
    'MONTREAL CANADIENS': 'MTL',
    u'MONTRÉAL CANADIENS': 'MTL',
    'CANADIENS MONTREAL': 'MTL',
    'NEW JERSEY DEVILS': 'N.J',
    'NASHVILLE PREDATORS': 'NSH',
    'NEW YORK ISLANDERS': 'NYI',
    'NEW YORK RANGERS': 'NYR',
    'OTTAWA SENATORS': 'OTT',
    'PHILADELPHIA FLYERS': 'PHI',
    'PHOENIX COYOTES': 'PHX',
    'PITTSBURGH PENGUINS': 'PIT',
    'SAN JOSE SHARKS': 'S.J',
    'ST. LOUIS BLUES': 'STL',
    'TAMPA BAY LIGHTNING': 'T.B',
    'TORONTO MAPLE LEAFS': 'TOR',
    'VANCOUVER CANUCKS': 'VAN',
    'VEGAS GOLDEN KNIGHTS': 'VGK',
    'WINNIPEG JETS': 'WPG',
    'WASHINGTON CAPITALS': 'WSH'
}

PART_TEAMS = {
    'DUCKS': 'ANA',
    'COYOTES': 'ARI',
    'THRASHERS': 'ATL',
    'BRUINS': 'BOS',
    'SABRES': 'BUF',
    'HURRICANES': 'CAR',
    'JACKETS': 'CBJ',
    'FLAMES': 'CGY',
    'BLACKHAWKS': 'CHI',
    'AVALANCHE': 'COL',
    'STARS': 'DAL',
    'RED WINGS': 'DET',
    'OILERS': 'EDM',
    'PANTHERS': 'FLA',
    'KINGS': 'L.A',
    'WILD': 'MIN',
    'CANADIENS': 'MTL',
    u'MONTRÉAL': 'MTL',
    'MONTREAL': 'MTL',
    'DEVILS': 'N.J',
    'PREDATORS': 'NSH',
    'ISLANDERS': 'NYI',
    'RANGERS': 'NYR',
    'SENATORS': 'OTT',
    'FLYERS': 'PHI',
    'COYOTES': 'PHX',
    'PENGUINS': 'PIT',
    'SHARKS': 'S.J',
    'BLUES': 'STL',
    'LIGHTNING': 'T.B',
    'MAPLE LEAFS': 'TOR',
    'CANUCKS': 'VAN',
    'GOLDEN KNIGHTS': 'VGK',
    'JETS': 'WPG',
    'CAPITALS': 'WSH'
}

TEAM_IDS = {
    "N.J": 1, "NYI": 2, "NYR": 3, "PHI": 4, "PIT": 5, "BOS": 6, "BUF": 7, "MTL": 8, "OTT": 9, "TOR": 10, "ATL": 11, "CAR": 12, "FLA": 13, "T.B": 14,
    "WSH": 15, "CHI": 16, "DET": 17, "NSH": 18, "STL": 19, "CGY": 20, "COL": 21, "EDM": 22, "VAN": 23, "ANA": 24, "DAL": 25, "L.A": 26, "S.J": 28,
    "CBJ": 29, "MIN": 30, "WPG": 52, "ARI": 53, "VGK": 54
}
# "ARI": 27, PHEONIX...

TEAM_IDS_REVERSE = {1: 'N.J', 2: 'NYI', 3: 'NYR', 4: 'PHI', 5: 'PIT', 6: 'BOS', 7: 'BUF', 8: 'MTL', 9: 'OTT', 10: 'TOR',
                    11: 'ATL', 12: 'CAR', 13: 'FLA', 14: 'T.B', 15: 'WSH', 16: 'CHI', 17: 'DET', 18: 'NSH', 19: 'STL',
                    20: 'CGY', 21: 'COL', 22: 'EDM', 23: 'VAN', 24: 'ANA', 25: 'DAL', 26: 'L.A', 53: 'ARI', 28: 'S.J',
                    29: 'CBJ', 30: 'MIN', 52: 'WPG', 54: 'VGK'}



NAMES = {
    'n/a': 'n/a', 'ALEXANDER OVECHKIN': 'Alex Ovechkin',
    'TOBY ENSTROM': 'Tobias Enstrom',
    'JAMIE MCGINN': 'Jamie McGinn',
    'CODY MCLEOD': 'Cody McLeod',
    'MARC-EDOUARD VLASIC': 'Marc-Edouard Vlasic',
    'RYAN MCDONAGH': 'Ryan McDonagh',
    'CHRIS TANEV': 'Christopher Tanev',
    'JARED MCCANN': 'Jared McCann',
    'P.K. SUBBAN': 'PK Subban',
    'DEVANTE SMITH-PELLY': 'Devante Smith-Pelly',
    'MIKE MCKENNA': 'Mike McKenna',
    'MICHAEL MCCARRON': 'Michael McCarron',
    'T.J. BRENNAN': 'TJ Brennan',
    'BRAYDEN MCNABB': 'Brayden McNabb',
    'PIERRE-ALEXANDRE PARENTEAU': 'PA Parenteau',
    'JAMES VAN RIEMSDYK': 'James van Riemsdyk',
    'OLIVER EKMAN-LARSSON': 'Oliver Ekman-Larsson',
    'TJ OSHIE': 'TJ Oshie',
    'J P DUMONT': 'JP Dumont',
    'J.T. MILLER': 'JT Miller',
    'R.J UMBERGER': 'RJ Umberger',
    'PA PARENTEAU': 'PA Parenteau',
    'PER-JOHAN AXELSSON': 'P.J. Axelsson',
    'MAXIME TALBOT': 'Max Talbot',
    'JOHN-MICHAEL LILES': 'John-Michael Liles',
    'DANIEL GIRARDI': 'Dan Girardi',
    'DANIEL CLEARY': 'Dan Cleary',
    'NIKLAS KRONVALL': 'Niklas Kronwall',

    'SIARHEI KASTSITSYN': 'Sergei Kostitsyn',
    'ANDREI KASTSITSYN': 'Andrei Kostitsyn',
    'ALEXEI KOVALEV': 'Alex Kovalev',

    'DAVID JOHNNY ODUYA': 'Johnny Oduya',
    'EDWARD PURCELL': 'Teddy Purcell',
    'NICKLAS GROSSMAN': 'Nicklas Grossmann',

    'PERNELL KARL SUBBAN': 'PK Subban',
    'VOJTEK VOLSKI': 'Wojtek Wolski',
    'VYACHESLAV VOYNOV': 'Slava Voynov',

    'FREDDY MODIN': 'Fredrik Modin',
    'VACLAV PROSPAL': 'Vinny Prospal',
    'KRISTOPHER LETANG': 'Kris Letang',

    'PIERRE ALEXANDRE PARENTEAU': 'PA Parenteau',
    'T.J. OSHIE': 'TJ Oshie',
    'JOHN HILLEN III': 'Jack Hillen',

    'BRANDON CROMBEEN': 'B.J. Crombeen',
    'JEAN-PIERRE DUMONT': 'JP Dumont',
    'RYAN NUGENT-HOPKINS': 'Ryan Nugent-Hopkins',

    'CONNOR MCDAVID': 'Connor McDavid',
    'TREVOR VAN RIEMSDYK': 'Trevor van Riemsdyk',
    'CALVIN DE HAAN': 'Calvin de Haan',

    'GREG MCKEGG': 'Greg McKegg',
    'NATHAN MACKINNON': 'Nathan MacKinnon',
    'KYLE MCLAREN': 'Kyle McLaren',

    'ADAM MCQUAID': 'Adam McQuaid',
    'DYLAN MCILRATH': 'Dylan McIlrath',
    'DANNY DEKEYSER': 'Danny DeKeyser',

    'JAKE MCCABE': 'Jake McCabe',
    'JAMIE MCBAIN': 'Jamie McBain',
    'PIERRE-MARC BOUCHARD': 'Pierre-Marc Bouchard',

    'JEAN-FRANCOIS JACQUES': 'JF Jacques',
    'OLE-KRISTIAN TOLLEFSEN': 'Ole-Kristian Tollefsen',

    'MARC-ANDRE BERGERON': 'Marc-Andre Bergeron',
    'MARC-ANTOINE POULIOT': 'Marc-Antoine Pouliot',

    'MARC-ANDRE GRAGNANI': 'Marc-Andre Gragnani',
    'JORDAN LAVALLEE-SMOTHERMAN': 'Jordan Lavallee-Smotherman',

    'PIERRE-LUC LETOURNEAU-LEBLOND': 'Pierre Leblond',
    'J-F JACQUES': 'JF Jacques',
    'JP DUMONT': 'JP Dumont',

    'MARC-ANDRE CLICHE': 'Marc-Andre Cliche',
    'J-P DUMONT': 'JP Dumont',
    'JOSHUA BAILEY': 'Josh Bailey',

    'OLIVIER MAGNAN-GRENIER': 'Olivier Magnan-Grenier',
    u'FRÉDÉRIC ST-DENIS': 'Frederic St-Denis',

    'MARC-ANDRE BOURDON': 'Marc-Andre Bourdon',
    'PIERRE-CEDRIC LABRIE': 'Pierre-Cedric Labrie',

    'JONATHAN AUDY-MARCHESSAULT': 'Jonathan Marchessault',
    'JEAN-GABRIEL PAGEAU': 'Jean-Gabriel Pageau',

    'JEAN-PHILIPPE COTE': 'Jean-Philippe Cote',
    'PIERRE-EDOUARD BELLEMARE': 'Pierre-Edouard Bellemare',

    'COLIN (JOHN) WHITE': 'Colin White',
    'BATES (JON) BATTAGLIA': 'Bates Battaglia',
    'MATHEW DUBMA': 'Matt Dumba',

    'NIKOLAI ANTROPOV': 'Nik Antropov',
    'KRYS BARCH': 'Krystofer Barch',
    'CAMERON BARKER': 'Cam Barker',

    'NICKLAS BERGFORS': 'Niclas Bergfors',
    'ROBERT BLAKE': 'Rob Blake',
    'MICHAEL BLUNDEN': 'Mike Blunden',

    'CHRISTOPHER BOURQUE': 'Chris Bourque',
    'MICHÃ«L BOURNIVAL': 'Michael Bournival',
    'NICHOLAS BOYNTON': 'Nick Boynton',

    'TJ BRENNAN': 'TJ Brennan',
    'DANIEL BRIERE': 'Danny Briere',
    'TJ BRODIE': 'TJ Brodie',
    'J.T. BROWN': 'JT Brown',

    'ALEXANDRE BURROWS': 'Alex Burrows',
    'MICHAEL CAMMALLERI': 'Mike Cammalleri',
    'DANIEL CARCILLO': 'Dan Carcillo',

    'MATTHEW CARLE': 'Matt Carle',
    'DANNY CLEARY': 'Dan Cleary',
    'JOSEPH CORVO': 'Joe Corvo',
    'JOSEPH CRABB': 'Joey Crabb',

    'BJ CROMBEEN': 'B.J. Crombeen',
    'EVGENII DADONOV': 'Evgeny Dadonov',
    'CHRIS VANDE VELDE': 'Chris VandeVelde',

    'JACOB DE LA ROSE': 'Jacob de la Rose',
    'JOE DIPENTA': 'Joe DiPenta',
    'JON DISALVATORE': 'Jon DiSalvatore',

    'JACOB DOWELL': 'Jake Dowell',
    'NICHOLAS DRAZENOVIC': 'Nick Drazenovic',
    'ROBERT EARL': 'Robbie Earl',

    'ALEXANDER FROLOV': 'Alex Frolov',
    'T.J. GALIARDI': 'TJ Galiardi',
    'TJ GALIARDI': 'TJ Galiardi',

    'ANDREW GREENE': 'Andy Greene',
    'MICHAEL GRIER': 'Mike Grier',
    'NATHAN GUENIN': 'Nate Guenin',

    'MARTY HAVLAT': 'Martin Havlat',
    'JOSHUA HENNESSY': 'Josh Hennessy',
    'T.J. HENSICK': 'TJ Hensick',

    'TJ Hensick': 'TJ Hensick',
    'CHRISTOPHER HIGGINS': 'Chris Higgins',
    'ROBERT HOLIK': 'Bobby Holik',

    'MATTHEW IRWIN': 'Matt Irwin',
    'P. J. AXELSSON': 'P.J. Axelsson',
    'PER JOHAN AXELSSON': 'P.J. Axelsson',

    'JONATHON KALINSKI': 'Jon Kalinski',
    'ALEXANDER KHOKHLACHEV': 'Alex Khokhlachev',
    'DJ KING': 'DJ King',

    'DWAYNE KING': 'DJ King',
    'MICHAEL KNUBLE': 'Mike Knuble',
    'KRYSTOFER KOLANOS': 'Krys Kolanos',

    'MICHAEL KOMISAREK': 'Mike Komisarek',
    'STAFFAN KRONVALL': 'Staffan Kronwall',
    'NIKOLAY KULEMIN': 'Nikolai Kulemin',

    'CLARKE MACARTHUR': 'Clarke MacArthur',
    'LANE MACDERMID': 'Lane MacDermid',
    'ANDREW MACDONALD': 'Andrew MacDonald',

    'RAYMOND MACIAS': 'Ray Macias',
    'CRAIG MACDONALD': 'Craig MacDonald',
    'STEVE MACINTYRE': 'Steve MacIntyre',

    'MAKSIM MAYOROV': 'Maxim Mayorov',
    'AARON MACKENZIE': 'Aaron MacKenzie',
    'DEREK MACKENZIE': 'Derek MacKenzie',

    'RODNEY PELLEY': 'Rod Pelley',
    'BRETT MACLEAN': 'Brett MacLean',
    'ANDREW MACWILLIAM': 'Andrew MacWilliam',

    'BRYAN MCCABE': 'Bryan McCabe',
    'OLIVIER MAGNAN': 'Olivier Magnan-Grenier',
    'DEAN MCAMMOND': 'Dean McAmmond',

    'KENNDAL MCARDLE': 'Kenndal McArdle',
    'ANDY MCDONALD': 'Andy McDonald',
    'COLIN MCDONALD': 'Colin McDonald',

    'JOHN MCCARTHY': 'John McCarthy',
    'STEVE MCCARTHY': 'Steve McCarthy',
    'DARREN MCCARTY': 'Darren McCarty',

    'JAY MCCLEMENT': 'Jay McClement',
    'CODY MCCORMICK': 'Cody McCormick',
    'MAX MCCORMICK': 'Max McCormick',

    'BROCK MCGINN': 'Brock McGinn',
    'TYE MCGINN': 'Tye McGinn',
    'BRIAN MCGRATTAN': 'Brian McGrattan',

    'DAVID MCINTYRE': 'David McIntyre',
    'NATHAN MCIVER': 'Nathan McIver',
    'JAY MCKEE': 'Jay McKee',

    'CURTIS MCKENZIE': 'Curtis McKenzie',
    'FRAZER MCLAREN': 'Frazer McLaren',
    'BRETT MCLEAN': 'Brett McLean',

    'BRANDON MCMILLAN': 'Brandon McMillan',
    'CARSON MCMILLAN': 'Carson McMillan',
    'PHILIP MCRAE':
        'Philip McRae',
    'FREDERICK MEYER IV': 'Freddy Meyer',
    'MICHAEL MODANO': 'Mike Modano',

    'CHRISTOPHER NEIL': 'Chris Neil',
    'MATTHEW NIETO': 'Matt Nieto',
    'JOHN ODUYA': 'Johnny Oduya',

    'PIERRE PARENTEAU': 'PA Parenteau',
    'MARC POULIOT': 'Marc-Antoine Pouliot',
    'MAXWELL REINHART': 'Max Reinhart',

    'MICHAEL RUPP': 'Mike Rupp',
    'ROBERT SCUDERI': 'Rob Scuderi',
    'TOMMY SESTITO': 'Tom Sestito',

    'MICHAEL SILLINGER': 'Mike Sillinger',
    'JONATHAN SIM': 'Jon Sim',
    'MARTIN ST LOUIS': 'Martin St. Louis',

    'MATTHEW STAJAN': 'Matt Stajan',
    'ZACHERY STORTINI': 'Zack Stortini',
    'PK SUBBAN': 'PK Subban',

    'WILLIAM THOMAS': 'Bill Thomas',
    'R.J. UMBERGER': 'RJ Umberger',
    'RJ UMBERGER': 'RJ Umberger',

    'MARK VAN GUILDER': 'Mark van Guilder',
    'BRYCE VAN BRABANT': 'Bryce van Brabant',

    'DAVID VAN DER GULIK': 'David van der Gulik',
    'MIKE VAN RYN': 'Mike van Ryn',
    'ANDREW WOZNIEWSKI': 'Andy Wozniewski',

    'JAMES WYMAN': 'JT Wyman',
    'JT WYMAN': 'JT Wyman',
    'NIKOLAY ZHERDEV': 'Nikolai Zherdev',

    'HARRISON ZOLNIERCZYK': 'Harry Zolnierczyk',
    'MARTIN ST PIERRE': 'Martin St. Pierre',
    'B.J CROMBEEN': 'B.J. Crombeen',

    'DENIS GAUTHIER JR.': 'DENIS GAUTHIER',
    'DENIS JR. GAUTHIER': 'DENIS GAUTHIER',
    'MARC-ANDRE FLEURY': 'Marc-Andre Fleury',

    'DAN LACOUTURE': 'Dan LaCouture',
    'RICK DIPIETRO': 'Rick DiPietro',
    'JOEY MACDONALD': 'Joey MacDonald',

    'TIMOTHY JR. THOMAS': 'Tim Thomas',
    'ILJA BRYZGALOV': 'Ilya Bryzgalov',
    'MATHEW DUMBA': 'Matt Dumba',

    'MICHAËL BOURNIVAL': 'Michael Bournival',
    'MATTHEW BENNING': 'Matt Benning',
    'ZACHARY SANFORD': 'Zach Sanford',

    'AJ GREER': 'A.J. Greer',
    'JT COMPHER': 'J.T. Compher',
    'NICOLAS PETAN': 'Nic Petan',

    'VINCENT HINOSTROZA': 'Vinnie Hinostroza',
    'PHILIP VARONE': 'Phil Varone',
    'JOSHUA MORRISSEY': 'Josh Morrissey',

    'Mathew Bodie': 'Mat Bodie',
    'MICHAEL FERLAND': 'Micheal Ferland',
    'MICHAEL SANTORELLI' :'Mike Santorelli',

    'CHRISTOPHER BREEN': 'Chris Breen',
    'BRYCE VAN BRABRANT': 'Bryce Van Brabant',
    'ALEXANDER KILLORN': 'Alex Killorn',

    'JOSEPH MORROW': 'Joe Morrow',
    'ALEX STEEN': 'Alexander Steen',
    'BRADLEY MILLS': 'Brad Mills',

    'MICHAEL SISLO': 'Mike Sislo',
    'MICHAEL VERNACE': 'Mike Vernace',
    'STEVEN REINPRECHT': 'Steve Reinprecht',

    'MATTHEW MURRAY': 'Matt Murray',
    'THOMAS MCCOLLUM': 'TOM MCCOLLUM',
    'MICHAEL MATHESON': 'MIKE MATHESON',

    'BOO NIEVES': 'CRISTOVAL NIEVES',
    'J.F. BERUBE': 'JEAN-FRANCOIS BERUBE',
    'TONY DEANGELO': 'ANTHONY DEANGELO',

    'JEFFREY HAMILTON': 'JEFF HAMILTON',
    'JAMES VANDERMEER': 'JIM VANDERMEER',
    'MICHAEL YORK': 'MIKE YORK',

    'EMMANUEL LEGACE': 'MANNY LEGACE',
    'JAMES DOWD': 'JIM DOWD',
    'ANDREW MILLER': 'DREW MILLER',

    'JOHN PEVERLEY': 'RICH PEVERLEY',
    'ILJA ZUBOV': 'ILYA ZUBOV',
    'CHRISTOPHER MINARD': 'CHRIS MINARD',

    'BENJAMIN ONDRUS': 'BEN ONDRUS',
    'ZACH FITZGERALD': 'ZACK FITZGERALD',
    'STEPHEN VALIQUETTE': 'STEVE VALIQUETTE',

    'OLAF KOLZIG': 'OLIE KOLZIG',
    'J-SEBASTIEN AUBIN': 'JEAN-SEBASTIEN AUBIN',
    'ALEXANDER AULD': 'ALEX AULD',

    'JAMES HOWARD': 'JIMMY HOWARD',
    'JEFF DROUIN-DESLAURIERS': 'JEFF DESLAURIERS',
    'SIMEON VARLAMOV': 'SEMYON VARLAMOV',

    'ALEXANDER PECHURSKI': 'Alexander Pechurskiy',
    'JEFFREY PENNER': 'JEFF PENNER',
    'EMMANUEL FERNANDEZ': 'Manny FERNANDEZ',

    'ALEXANDER PETROVIC': 'ALEX PETROVIC',
    'ZACHARY ASTON-REESE': 'ZACH ASTON-REESE',
    'J-F BERUBE': 'JEAN-FRANCOIS BERUBE',

    "DANNY O'REGAN": "DANIEL O'REGAN",
    "PATRICK MAROON": "PAT MAROON",
    "LEE  STEMPNIAK": "LEE STEMPNIAK",
    "JAMES REIMER ,": "JAMES REIMER",
    "CALVIN PETERSEN ,": "CALVIN PETERSEN",
    "CAL PETERSEN": "CALVIN PETERSEN",
    "ALEXANDER NYLANDER": "ALEX NYLANDER"
}