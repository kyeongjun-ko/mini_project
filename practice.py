import branca.element
import folium
from folium import plugins
import pandas as pd
from selenium import webdriver
import os
import webbrowser
from python.SQL.sql_open_close import open_close
from python.html.html_gupsik import popup_html
# from folium.plugins import MarkerCluster

free_stores = pd.read_csv("d:/files/seoul_sql.csv", sep=',', encoding="utf-8")


driver = webdriver.Chrome("d:/chromedriver.exe")
driver.get("https://mycurrentlocation.net/")

longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath
longitude = [x.text for x in longitude]
longitude = str(longitude[0])
latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
latitude = [x.text for x in latitude]
latitude = str(latitude[0])
driver.quit()
# print(latitude,longitude)

map_free = folium.Map(location=[latitude, longitude], zoom_start=11.49999999)

# 현재 위치
folium.Marker(location=[latitude, longitude], icon=folium.Icon(color='red', icon='star')).add_to(map_free)

# 미니맵
# minimap = plugins.MiniMap()
# map_free.add_child(minimap)
# map_free.save(os.path.join('results'))

# 그룹 간 마커 클러스터
mcg = folium.plugins.MarkerCluster(control=False)
map_free.add_child(mcg)

opened = folium.plugins.FeatureGroupSubGroup(mcg, '영업중')
map_free.add_child(opened)

closed = folium.plugins.FeatureGroupSubGroup(mcg, '영업 종료')
map_free.add_child(closed)

folium.LayerControl(collapsed=False).add_to(map_free)
map_free.save(os.path.join('results'))

final = open_close()

# marker_cluster = MarkerCluster().add_to(map_free)
for i in range(len(free_stores)):
    html = popup_html(i, free_stores)
    iframe = branca.element.IFrame(html=html)
    popup = folium.Popup(folium.Html(html, script=True))
    free = folium.Marker([free_stores['latitude'].iloc[i], free_stores['longitude'].iloc[i]], popup=popup)

    if free_stores['store_name'].iloc[i] in final:
        free.add_to(opened)
    else:
        free.add_to(closed)


output_file = 'C:/Users/bit/PycharmProjects/freefood/python/maps/gupsik_map.html'
map_free.save(output_file)
webbrowser.open(output_file, new=2)