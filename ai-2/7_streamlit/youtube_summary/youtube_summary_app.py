import my_yt_tran
import my_text_sum
import streamlit as st
import openai
import os
import tiktoken
import textwrap
import deepl
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api_errors import NoTranscriptFound, TranscriptDisabled

def cal_token_num(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    encoded_text = enc.encode(text)
    token_num = len(encoded_text)

    return token_num

def divide_text(text, token_num):
    req_max_token = 2000

    divided_num = int(token_num / req_max_token) + 1
    divided_char_num = int(len(text) / divided_num)
    divided_width = divied_char_num + 20

    divided_text_list = textwrap.wrap(text, width=divided_width)

    return divided_num, divided_text_list

def summary_youtube_video(video_url, selected_lang, trans_method):
    if selected_lang == '영어':
        lang = 'en'
    else:
        lang = 'ko'
    
    st.video (video_url, format="video/mp4")
    
    video_info = my_yt_tran.get_video_info(video_url)
    yt_title = video_info['title']
    yt_duration = video_info['duration']

    st.write(f'[제목] {yt_title}, [길이(분:초) {yt_duration}]')

    try:
        yt_transcript = my_yt_tran.get_transcript_from_youtube(video_url, lang)
    except NoTranscriptFound:
        st.error("자막을 찾을 수 없습니다. 다른 동영상을 시도해주세요.")
        return
    except TranscriptDisabled:
        st.error("이 동영상의 자막이 비활성화되어 있습니다.")
        return
    except Exception as e:
        st.error(f"자막을 가져오는 중 오류가 발생했습니다: {str(e)}")
        return

    token_num = cal_token_num(yt_transcript)

    div_num, divided_text_list = divide_text(yt_transcript, token_num)
    st.write('유튜브 동영상 내용 요약 중입니다. 잠시만 기다려 주세요...')

    summaries = []

    for divide_yt_transcript in divided_text_list:
        summary = my_text_sum.summarize_text(divide_yt_transcript, lang)
        summaries.append(summary)

    _, final_summary = my_text_sum.summariz_text_final(summaries, lang)

    if selected_lang == '영어':
        shorten_num == 200
    else:
        shorten_num == 120
    
    shorten_final_summary = textwrap.shorten(final_summary, shorten_num, placeholder=' [...이하 생략...]')
    st.write('- 최종 요약(축약) : ', shorten_final_summary)

    if selected_lang == '영어' 
        if trans_method == 'OpenAI':
            trans_result = my_text_sum.translate_english_to_korean_using_openAI(final_summary)
        elif trans_method == 'DeepL':
            trans_result = my_text_sum.translate_english_to_korean_using_DeepL(final_summary)
        shorten_final_summary = textwrap.shorten(trans_result, shorten_num, placeholder=' [...이하 생략...]')
        st.write('- 한국어 요약(축약) : ', shorten_final_summary)

# ----------------- Callback  함수 ----------------------- #

def button_callback():
    st.session_state['input'] = ''
    
# ----------------- sidebar 구성 ----------------------- #
st.sidebar.title('요약 설정')

url_text = st.sidebar.text_input('유튜브 동영상 URL을 입력하세요.', key='input')

clicked = st.sidebar.button('URL 입력 내용 지우기', on_click=button_callback)

yt_lang = st.sidebar.radio('유튜브 동영상 자막 언어 선택', ['한국어', '영어'], index=1, horizontal=True)

if yt_lang == '영어':
    trans_method = st.sidebar.radio('한국어 번역 방법 선택', ['OpenAI', 'DeepL'], index=0, horizontal=True)
else:
    trans_method = ''

clicked = st.sidebar.button('동영상 내용 요약')

# ----------------- Main View 구성----------------------- #
st.title('유튜브 동영상 내용 요약')

if url_text and clicked_for_sum:
    yt_video_url = url_text.strip()
    summary_youtube_video(yt_video_url, yt_lang, trans_method)  