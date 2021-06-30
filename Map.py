import folium
import pandas as pd
import stations

m = folium.Map(location=[51.11, 17.0325], zoom_start=12)

# TODO.txt spakowanie w funkcję
paths = stations.csv_paths
name_location = stations.name_loc()
rides_locations = stations.rides_locations(paths, name_location)


df = pd.DataFrame(rides_locations)
df_counts = df.value_counts()
df_to_dict = df_counts.to_dict()


for i in df_to_dict:
    if 1 < df_to_dict[i] < 5:
        line = folium.PolyLine(locations=[i], weight=df_to_dict[i] * 0.2, color='#0000FF', popup=df_to_dict[i])
    elif df_to_dict[i] >= 5:
        line = folium.PolyLine(locations=[i], weight=df_to_dict[i] * 0.5, color='#0000FF', popup=df_to_dict[i])
    m.add_child(line)

# color='#FF0000'
m.save('Wroclaw.html')
