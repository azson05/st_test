import streamlit as st

st.image("https://docs.streamlit.io/logo.svg")

st.header("OpenAI API Key를 적어주세요.")
api = st.text_input("API Key?")

if st.button("확인"):
  from openai import OpenAI
  client = OpenAI(api_key=f"{api}")
  
st.divider()

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")
if st.button("실행하기"):
  from openai import OpenAI
  client = OpenAI(api_key=f"{api}")
  response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()

    st.markdown(f"질문: {prompt}")
    st.markdown(f"답변: {answer}")
  st.markdown(f"질문: {prompt}")

st.divider()
