import streamlit as st

st.image("https://docs.streamlit.io/logo.svg")

st.header("OpenAI API Key를 적어주세요.")
api = st.text_input("API Key?")

if st.button("확인"):
  from openai import OpenAI
  client = OpenAI(api_key=f"{api}")
  assistant = client.beta.assistants.create(
    instructions = "You are a helpful assistant.",
    model='gpt-3.5-turbo'
  )
  
st.divider()

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")
if st.button("실행하기"):
  from openai import OpenAI
  client = OpenAI(api_key=f"{api}")
  assistant = client.beta.assistants.create(
    instructions = "You are a helpful assistant.",
    model='gpt-3.5-turbo'
  )
  thread = client.beta.threads.create(
    messages=[
      {
          "role":"user",
          "content": f"{prompt}"
      }
    ]
  )
  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
  )
  st.markdown(f"질문: {prompt}")

st.divider()
