import streamlit as st
import page1
import page2
import cloud
import map
import plotlychart

def main() :
    st.sidebar.title('mystreamlit sidebar')
    selected = st.sidebar.selectbox('페이지선택하세요', ['home','page1','page2','baseball','map','plotly'])
    if(selected == 'home'):
        page()
    elif(selected == 'page1'):
        page1.page()
    elif(selected == 'page2'):
        page2.page()
    elif(selected == 'baseball'):
        cloud.page()
    elif(selected == 'map'):
        map.page()
    elif(selected == 'plotly'):
        plotlychart.page()

def page():    
    st.title('한국폴리텍대학 인공지능SW학과')
    st.image('dog.jpg')

if __name__ == '__main__':
    main()