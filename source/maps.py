from folium import Map, Marker, Icon


def generate_map():
    map = Map(location=[40.694481, -73.98666], zoom_start=15)
    popup = '<A href="/center1.html">Callahan\'s Castaways</A>'
    map.add_child(
        Marker(location=[40.694481, -73.98666],
               popup=popup,
               icon=Icon(color='purple')))

    popup = '<A href="/center2.html">Tanya\'s Terrific Givers</A>'
    map.add_child(
        Marker(location=[40.69936, -73.97898],
               popup=popup,
               icon=Icon(color='purple')))

    popup = '<A href="/center3.html">Avik\'s Able Homes</A>'
    map.add_child(
        Marker(location=[40.69032, -73.999357],
               popup=popup,
               icon=Icon(color='purple')))

    popup = '<A href="/center4.html">Crystal Clear Cause</A>'
    map.add_child(
        Marker(location=[40.68579, -73.98040],
               popup=popup,
               icon=Icon(color='purple')))

    map.save("source/templates/maps.html")
