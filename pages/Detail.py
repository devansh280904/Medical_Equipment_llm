import streamlit as st
import os

eq = st.session_state.get("selected_equipment")
if eq:
    st.markdown("<h1 style='text-align: center;'>{}</h1>".format(eq['name']), unsafe_allow_html=True)
    col_img = st.columns([1, 1, 1])
    with col_img[1]:
        st.image(f"assets/{eq['image']}", width=500)

    st.markdown(
        f"<div style='text-align: center; font-size: 1.2em; margin-bottom: 30px;'>{eq['description']}</div>",
        unsafe_allow_html=True
    )
 
    col_btn = st.columns([1, 1])
    with col_btn[1]: 
         if st.button("Learn More"):
              st.switch_page("pages/llmChat.py")
else:
    st.warning("No equipment selected.")
    st.button("Back to Dashboard", on_click=lambda: st.switch_page("app.py"))

st.markdown("---")

