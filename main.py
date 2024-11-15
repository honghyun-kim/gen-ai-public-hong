import streamlit as st

st.title('This is a title')
st.title('This 한글도 됨? 수정')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')



title = st.text_input("주제를 정해봐")
st.write("The current movie title is", title)


if st.button("요청하기"):
    st.write("뭐임마")
