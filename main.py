import streamlit as st

st.title('간단한 번역기 (설치 없이 가능)')

# 예제 사전
translation_dict = {
    '안녕하세요': 'Hello',
    '감사합니다': 'Thank you',
    '사랑': 'Love',
    '학교': 'School'
}

text = st.text_input('번역할 한국어 문장을 입력해주세요:')

if st.button('번역하기'):
    if text:
        translated = translation_dict.get(text, '사전에 없는 단어입니다.')
        st.write('번역 결과:')
        st.write(translated)
    else:
        st.warning('문장을 입력해주세요!')
