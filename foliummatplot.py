import folium
map=folium.Map(location=[45,-121],zoom_start=20)

#map=simple_marker(location=[45,-121],zoom_start=12,popup='ok',marker_color='red')
map.save(outfile='mapp11.html')

