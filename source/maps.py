from folium import Map, Marker, Icon


def generate_map():
    map = Map(location=[40.694481, -73.98666], zoom_start=15)

    popup = '<A href="http://www.google.com" target="_blank">Click Me!</A>'
    map.add_child(
        Marker(location=[40.694481, -73.98666],
               popup=popup,
               icon=Icon(color='purple')))

    map.save("source/templates/maps.html")
