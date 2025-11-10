

import streamlit as st
from googletrans import Translator

st.title('나의 첫 번역기 웹 서비스!!')


translator = Translator()


text = st.text_area('번역할 문장을 입력해주세요:')
lang = st.selectbox('번역할 언어를 선택해주세요:', ['영어', '일본어', '중국어', '프랑스어', '독일어'])


lang_dict = {
    '영어': 'en',
    '일본어': 'ja',
    '중국어': 'zh-cn',
    '프랑스어': 'fr',
    '독일어': 'de'
}

if st.button('번역하기'):
    if text:
        translated = translator.translate(text, dest=lang_dict[lang])
        st.write('번역 결과:')
        st.write(translated.text)
    else:
        st.warning('번역할 문장을 입력해주세요!')
