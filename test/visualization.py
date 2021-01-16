import folium
import pandas as pd
import numpy as np

center = (37.2410864, 127.1775537)
zoom = 17

m = folium.Map(
    location=center,
    zoom_start=zoom,
    tiles='http://api.vworld.kr/req/wmts/1.0.0/E7AF57B8-E4AF-38EA-BF1F-490CDCBB8313/Base/{z}/{y}/{x}.png',
    attr='용인시'
)

# df = pd.read_csv("../data/17.용인시_소상공인_매출정보.csv")
df = pd.read_csv("./data/1.용인시_상권_정보.csv", encoding='utf-8')

# geo_data = "16.용인시_소상공인_매출정보.geojson"
geo_data = "./data/12.용인시_법정경계(읍면동).geojson"

# for index, row in data.iterrows():
#     folium.Marker([row['LATITUDE_위도'], row['LONGITUDE_경도']]).add_to(m)

folium.Choropleth(
    geo_data=None,
    data=df,
    columns=('gid', 'sales_est_amt_202006'),
    key_on='feature.properties.gid',
    fill_color='Blue',
    legend_name='상권 정보',
).add_to(m)

m
