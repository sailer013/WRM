import pandas as pd

# TODO automatyczne pobieranie danych z API
csv_station = r'C:\Users\mszpa\OneDrive\Pulpit\42eea6ec-43c3-4d13-aa77-a93394d6165a.csv'
csv_paths = r'C:\Users\mszpa\OneDrive\Pulpit\Historia_przejazdow (1).csv'


def name_loc(station_csv):  # Return dic {station name:(lat,lng)}
    file = pd.read_csv(station_csv)
    lat_lng = list(zip([lat for lat in file['lat']], [lng for lng in file['lng']]))
    stat_names = [st for st in file['name']]
    loc_name = list(zip(stat_names, lat_lng))
    loc_name = {k: v for (k, v) in loc_name}
    return loc_name


nm_loc = name_loc(csv_station)


def rides_locations(station_csv, names_location):  # Return location of all rides (both ways as one)
    file = pd.read_csv(station_csv, encoding='cp1250')
    file_nan = file.dropna()
    all_stat = list(zip(file_nan['Stacja wynajmu'], file_nan['Stacja zwrotu']))
    rnt_ret = []
    for stat in all_stat:
        if 'Poza stacją' not in stat and '.RELOKACYJNA' not in stat and '#Magazyn Wrocław 2020/21' not in stat:
            rnt_ret.append(stat)
    loc = []
    for stat in rnt_ret:
        for i in stat:
            loc.append(names_location[i])
    stat_loc = [loc[n:n+2] for n in range(0, len(loc), 2)]
    stat_loc_both = []
    while stat_loc:
        if (list((stat_loc[0][1], stat_loc[0][0])) in stat_loc_both) or (stat_loc[0] in stat_loc_both):
            if stat_loc[0] in stat_loc_both:
                stat_loc_both.append(stat_loc[0])
            else:
                stat_loc_both.append(list((stat_loc[0][1], stat_loc[0][0])))
            stat_loc = stat_loc[1:]
        else:
            stat_loc_both.append(stat_loc[0])
            stat_loc = stat_loc[1:]
    return stat_loc_both


print(rides_locations(csv_paths, nm_loc))
