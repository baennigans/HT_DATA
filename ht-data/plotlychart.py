import plotly.express as px
import pandas as pd
import streamlit as st

def page():
    st.title('plotly')

    mpg = pd.read_csv('mpg.csv')
    fig = px.scatter(data_frame = mpg, x = 'cty', y = 'hwy', color = 'drv')
    st.plotly_chart(fig)





def main(): 
    print('메인입니다.')
 
if __name__ == '__main__':
    main()