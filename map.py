import folium
import pandas as pd
import os
import branca




counties= os.path.join('data' ,'co.geojson')
populationdata=os.path.join('data', 'popdata.csv')
countydata=pd.read_csv(populationdata)


m=folium.Map(location=[-0.28866249,38.56480354],zoom_start=7)

folium.Choropleth(
    geo_data=counties,
    name='choropleth',
    data=populationdata,
    columns=['County','Total_Population19'],
    key_on='feature.properties.COUNTY_NAM',
    fill_color='Reds',
    fill_opacity=0.7,
    line_opacity=0.5,
     legend_name='Unemployment Rate (%)'
).add_to(m)


folium.LayerControl().add_to(m)
m.save('map2.html')



