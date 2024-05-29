import streamlit as st

st.image("https://docs.streamlit.io/logo.svg")

st.header("OpenAI API Key를 적어주세요.")
api = st.text_input(label, type="password")

if st.button("확인"):
  from openai import OpenAI
  client = OpenAI(api_key=f"{api}")

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")
if st.button("실행하기"):
   assistant = client.beta.assistants.create(
      instructions = "You are a helpful assistant.",
      model='gpt-3.5-turbo'
  )
  )
  run = client.beta.threads.runs.create(
      thread_id=thread.id,
      assistant_id=assistant.id,
  )
  st.markdown(f"응답: {prompt}")

st.divider()
