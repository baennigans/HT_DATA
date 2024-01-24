import re
import pandas as pd
import konlpy
import numpy as np
import PIL
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st


def page():
    print('다른곳에서 호출하겠습니다.')
    st.title('여기는 워드클라우드 화면입니다.')


    baseball = open('baseball.txt', encoding='UTF-8').read()
    baseball=re.sub('[^가-힣]',' ',baseball)
    hannanum = konlpy.tag.Hannanum()
    nouns = hannanum.nouns(baseball)

    df_word = pd.DataFrame({'word':nouns})
    df_word['word_n'] = df_word['word'].str.len()
    df_word = df_word.query('word_n >= 2')
    df_word.sort_values('word')
    df_word = df_word.groupby('word', as_index=False).agg(n=('word', 'count')).sort_values('n', ascending=False)
    top20 = df_word.head(20)
    st.dataframe(top20)


    plt.rcParams.update({'font.family':'malgun Gothic', 'figure.dpi':'120', 'figure.figsize':[6.5, 6]})
    fig1=plt.figure(figsize=(10,10))
    sns.barplot(data=top20, y='word', x='n')
    st.pyplot(fig1)

    st.bar_chart(data=top20.head(10), y='n', x='word')


    font = 'Dohyeon-Regular.ttf'
    dic_word = df_word.set_index('word').to_dict()['n']
    icon = PIL.Image.open('baseball3.jpg')
    img = np.array(icon)
    wc = WordCloud(random_state=1234, font_path=font, width=400, height=400, background_color='white', mask = img, colormap='inferno')
    img_wordcloud = wc.generate_from_frequencies(dic_word)

    fig=plt.figure(figsize=(10,10))
    plt.axis('off')
    plt.imshow(img_wordcloud)
    st.pyplot(fig)
    


def main():
    print('main hello')

    baseball = open('baseball.txt', encoding='UTF-8').read()
    baseball=re.sub('[^가-힣]',' ',baseball)
    hannanum = konlpy.tag.Hannanum()
    nouns = hannanum.nouns(baseball)

    df_word = pd.DataFrame({'word':nouns})
    df_word['word_n'] = df_word['word'].str.len()
    df_word = df_word.query('word_n >= 2')
    df_word.sort_values('word')
    df_word = df_word.groupby('word', as_index=False).agg(n=('word', 'count')).sort_values('n', ascending=False)
    top20 = df_word.head(20)

    plt.rcParams.update({'font.family':'malgun Gothic', 'figure.dpi':'120', 'figure.figsize':[6.5, 6]})
    sns.barplot(data=top20, y='word', x='n')

    dic_word = df_word.set_index('word').to_dict()['n']
    icon = PIL.Image.open('baseball3.jpg')
    img = np.array(icon)
    font = 'Dohyeon-Regular.ttf'
    
    wc = WordCloud(random_state=1234, font_path=font, width=400, height=400, background_color='white', mask = img, colormap='inferno')
    img_wordcloud = wc.generate_from_frequencies(dic_word)

    plt.figure(figsize=(10,10))
    plt.axis('off')
    plt.imshow(img_wordcloud)
    plt.show()

if __name__ == "__main__":
    main()