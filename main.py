import streamlit as st

st.title("โปรแกรมทำนายเลขนำโชค")
name = st.text_input("คุณชื่ออะไรครับ?")
number = st.number_input("ขอเลขนำโชค 1 ตัว:", step=1)

if st.button("คำนวณ"):
    result = number * 10
    st.write(f"สวัสดีคุณ {name} เลขนำโชคของคุณคูณสิบแล้วได้: {result}")
