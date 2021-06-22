import folium
import pandas as pd
import stations

m = folium.Map(location=[51.11, 17.0325], zoom_start=12)


# TODO.txt spakowanie w funkcję

name_loc = stations.name_loc(stations.csv_station)
x = stations.rides_locations(stations.csv_paths, name_loc)

print(name_loc)

df = pd.DataFrame(x)
df_counts = df.value_counts()
df_to_dict = df_counts.to_dict()


for i in df_to_dict:
    if df_to_dict[i] < 5:
        line = folium.PolyLine(locations=[i], weight=df_to_dict[i] * 0.2, color='#0000FF', popup=df_to_dict[i])
    else:
        line = folium.PolyLine(locations=[i], weight=df_to_dict[i] * 0.5, color='#FF0000', popup=df_to_dict[i])
    m.add_child(line)


m.save('Wroclaw.html')
