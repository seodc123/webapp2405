# 설치 필요
# pip install langchain streamlit

import streamlit as st
from langchain_community.llms import OpenAI

# HTML을 사용하여 제목을 꾸미기
st.markdown("""
    <style>
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    </style>
    <div class="title">🍎🍐🍊 나의 AI Chat 🥝🍅🍆</div>
    """, unsafe_allow_html=True)

# 사이드바에 API 키 입력 필드 추가
openai_api_key = st.sidebar.text_input('OpenAI API Key')

# 응답 생성 함수
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, max_tokens=1000)  # max_tokens 값을 늘려 더 긴 응답을 받도록 설정
    st.info(llm(input_text))

# 사용자 입력 폼
with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)

# 추가 그림 (예: 헤더 이미지)
st.image("https://example.com/path-to-your-image.jpg", use_column_width=True)
