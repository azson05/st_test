import streamlit as st
from openai import OpenAI
from PIL import Image
from streamlit_chat import message

def app():
    st.set_page_config(layout="wide")
    img = Image.open("백경이.png")
    img = img.resize((171,230))
    st.image(img)
    st.title("우리 학교의 영원한 친구 백경이")
    st.subheader("백경이는 부경대의 모든 건물들을 다 알아! 학식당 메뉴도 알고 있지, 뭐든지 물어봐!")
app()

with st.sidebar:
    if user_api_key := st.text_input("OpenAI API키를 입력해주세요.", key = "openai_api_key", type="password"):
        if 'user_api_key' not in st.session_state:
            st.session_state.key = user_api_key
            
if st.button('Assistant 새롭게 생성하기'):

if prompt := st.chat_input("메시지를 입력하세요."):
    if st.session_state.client:
        st.session_state.messages.append({"content": prompt, "role": True}) # user의 prompt를 messages로 저장
        for msg in st.session_state.messages: # re-run 후 대화 내역 출력 및 user의 prompt를 출력
            message(msg["content"], is_user=msg["role"])
        client = st.session_state.client # session_state에 저장된 client id를 불러오기
        assistant = st.session_state.assistant
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )
        st.session_state.thread_id = thread.id
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        thread_messages = client.beta.threads.messages.list(thread.id, run_id=run.id)
        answer = thread_messages.data[0].content[0].text.value # assistant의 응답에서 text를 추출
        message(answer)
        st.session_state.messages.append({"content": answer, "role": False})
if st.button("대화 내역 지우기"):
    if st.session_state.thread_id:
        if st.session_state.client:
            client = st.session_state.client
            response = client.beta.thread.delete(st.session_state.thread_id)
            del st.session_state.messages
            st.rerun()
