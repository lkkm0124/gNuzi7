import streamlit as st
from deep_translator import GoogleTranslator  # googletrans 대신 사용

st.title('나의 첫 번역기 웹 서비스!!')

# 사용자 입력
text = st.text_area('번역할 문장을 입력해주세요:')
lang = st.selectbox('번역할 언어를 선택해주세요:', ['영어', '일본어', '중국어', '프랑스어', '독일어'])

# 언어 코드 매핑
lang_dict = {
    '영어': 'en',
    '일본어': 'ja',
    '중국어': 'zh-CN',
    '프랑스어': 'fr',
    '독일어': 'de'
}

# 번역 버튼
if st.button('번역하기'):
    if text:
        translated = GoogleTranslator(source='auto', target=lang_dict[lang]).translate(text)
        st.write('번역 결과:')
        st.write(translated)
    else:
        st.warning('번역할 문장을 입력해주세요!')
