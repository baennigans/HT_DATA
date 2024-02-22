import streamlit as st
import folium
import streamlit as st
from streamlit_folium import st_folium
import json
import pandas as pd



def page():

    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
    st_folium(m, width=725)


    st.title('서울지역 대학교 지도.')
    univ = pd.read_excel('seoul_univ.xlsx', index_col=0) 
    seoul_map3=folium.Map(location=[37.56, 127] , tiles = 'cartodbpositron', zoom_start=11)
    for name, lat, lng in zip (univ.index, univ.위도, univ.경도) : 
         folium.Marker([lat, lng], popup=name).add_to(seoul_map3)
    geo_seoul_sig = json.load(open('SIG_Seoul.geojson', encoding='UTF-8'))
    folium.Choropleth(geo_data=geo_seoul_sig, fill_opacity=0, line_weight=4).add_to(seoul_map3)
    st_folium(seoul_map3, width=725)


    st.title('시군구별 인구 단계 구분도')
    geo = json.load(open('SIG.geojson', encoding='UTF-8'))
    df_pop = pd.read_csv('Population_SIG.csv')
    bins = list(df_pop["pop"].quantile([0, 0.2, 0.4, 0.6, 0.8, 1]))
    map_sig2 = folium.Map(location=[35.95, 127.7], zoom_start =7, titles='cartodbpositron', width = '50%', heigth = '50%')
    folium.Choropleth(geo_data=geo, data=df_pop, columns=('code','pop'), key_on='feature.properties.SIG_CD',
                  fill_color='YlGnBu', fill_opacity=1, line_opacity=0.5, bins = bins).add_to(map_sig2)
    st_folium(map_sig2, width=725)


    st.title('서울시 동별 외국인 인구 단계 구분도')
    geo_seoul = json.load(open('EMD_Seoul.geojson', encoding='UTF-8'))
    foreigner = pd.read_csv('Foreigner_EMD_Seoul.csv')
    bins=list(foreigner['pop'].quantile([0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))
    map_seoul = folium.Map(location=[37.56, 127], zoom_start=11, titles='cartodbpositron')
    folium.Choropleth(geo_data=geo_seoul, data=foreigner, columns=('code','pop'), key_on='feature.properties.ADM_DR_CD',
                  fill_color='Blues', nan_fill_color='White', fill_opacity = 1, line_opacity = 0.5, bins = bins).add_to(map_seoul)
    geo_seoul_sig = json.load(open('SIG_Seoul.geojson', encoding='UTF-8'))
    folium.Choropleth(geo_data=geo_seoul_sig, fill_opacity=0, line_weight=4).add_to(map_seoul)
    st_folium(map_seoul, width=725)



def main(): 
    st.title('pop')
 
if __name__ == '__main__':
    main()