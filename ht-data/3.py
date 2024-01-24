# mpg.csv 자동차 관련한것
# 데이터 분석 -> web화면 보여준다.

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 회사만 입력 받아서 그회사 자동차 data를 화면에 출력한다.
# 회사에 따른 city 연비를 구한다.

mpg_original = pd.read_csv('mpg.csv')
mpg = mpg_original.copy()

st.title('자동차 데이터분석입니다.')
#st.title(mpg['manufacturer'].unique())
st.sidebar.title('sidebar title')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['static리스트', 'dynamic리스트',\
                            'multiselect', 'chart', '자유자재로 분석하기'])

with tab1:

    #1) 정해진 리스트에서 검색값을 가져오기. 
    selected_manufacturer = st.sidebar.selectbox('자동차회사 선택하세요', 
                        ['audi', 'hyundai'])
    result1 = mpg.query('manufacturer == @selected_manufacturer')

    result2 = mpg.query('manufacturer == @selected_manufacturer')\
                        [['manufacturer','model','year']]
    st.dataframe(result2)

with tab2:
    #2) mpg에서 manufacturer의 unique한 값을 list로 넣기
    selected_manufacturer2 = st.sidebar.selectbox('자동차회사 선택하세요2', 
                        mpg['manufacturer'].unique().tolist())
    result3 = mpg.query('manufacturer == @selected_manufacturer2')
    st.dataframe(result3)

with tab3:
    #3) multi select 가능
    ms_manufacturer = st.sidebar.multiselect('자동차 회사 선택하세요. 복수 선택 가능',
                        mpg['manufacturer'].unique().tolist())

    result4 = mpg.query('manufacturer in @ms_manufacturer')
    st.dataframe(result4) 

with tab4:
    #4) chart그리기
    # manufacturer 별로 city 연비 평균가 높은 순서로 바 그래프를 그려라.

    result5 = mpg.groupby('manufacturer', as_index=False)\
                    .agg(city_mean = ('cty', 'mean'))\
                        .sort_values('city_mean', ascending=False)\
                            .head(5)
    st.dataframe(result5)

    fig = plt.figure()
    sns.barplot(data= result5, x= 'manufacturer', y = 'city_mean')
    st.pyplot(fig)

with tab5:
    #5) selectbox로 값 입력 받기 - mpg
    # 첫번째 -> groupby 쓸것 , 'manufacturer', 'category','drv', 추가가능
    # 두번째 -> aggregate에 쓸것  'cty','hwy' 
    # 세번째 -> aggregate에 쓰는 함수 - 'mean', 'count', 'max', 'min'

    var1 = st.sidebar.selectbox('그룹을 선택하세요.',
                                ['manufacturer','category','drv'])
    var2 = st.sidebar.selectbox('연비종류를 선택하세요',
                                ['cty','hwy'])
    var3 = st.sidebar.selectbox('구하고자 하는 함수를 선택하세요',
                                ['mean','count','max','min'])
    result6 = mpg.groupby(var1, as_index=False)\
                    .agg(value = (var2, var3))\
                        .sort_values('value', ascending=False).head(5)
    st.dataframe(result6)
    fig1 = plt.figure()
    sns.barplot(data= result6, x= var1, y = 'value')
    st.pyplot(fig1)


st.title('맨 마지막 줄입니다.')


#6) selectbox로 값 입력 받기 - welfare
# 첫번째 -> groupby 쓸것 , 'sex', 'job','ageg', ....
# 두번째 -> aggregate에 쓸것  'income', 
# 세번째 -> aggregate에 쓰는 함수 - 'mean', 'count', 'max', 'min'