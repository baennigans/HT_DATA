#page2.py
import streamlit as st
# mpg에 관한 데이터 분석을 넣고
def page():
    st.title('page 2.py 입니다. ')

def main():  
    st.title('지금은 page2가 main입니다.')
    st.title('이 화면은 streamlit run page2.py을 했을때 보는 화면입니다.')
    
if __name__ == '__main__':
    main()