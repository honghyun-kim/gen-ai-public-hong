import streamlit as st

st.title('안녕하세요. 테스트 하고 있습니다. by khh')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')


title = st.text_input("주제를 정해봐")
st.write("The current movie title is", title)


if st.button("요청하기"):
    st.write("뭐임마")


if st.button("이것도 눌러봐"):
    st.write("ㅄ...")
