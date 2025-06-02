import streamlit as st
import time

progress_bar = st.progress(0)

for percent in range(0, 101, 10):
    time.sleep(0.5)
    progress_bar.progress(percent)

with st.spinner('로딩중...'):
    time.sleep(5)
st.success('로딩완료!')

st.balloons()

st.snow()

st.success('로딩완료!')

st.error('에러 발생!')

st.warning('경고 발생!')

st.info('정보 발생!')

st.exception('에러 발생!')
