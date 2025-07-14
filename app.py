import streamlit as st
import json
import os


with open(os.path.join("data", "equipment.json"), "r", encoding="utf-8") as f:
    equipment_list = json.load(f)

st.set_page_config(page_title="Medical Equipment LLM", layout="wide")

Project = "On-Device Medical Equipment Description Using LLMs"
st.markdown(f"<h1 style='text-align: center;'>{Project}</h1>", unsafe_allow_html=True)

title = "🏥 Medical Equipment Dashboard"
st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)


search = st.text_input("Search equipment...")
categories = sorted(set(eq["category"] for eq in equipment_list))
selected_category = st.selectbox("Filter by category", ["All"] + categories)

filtered = [
    eq for eq in equipment_list
    if (search.lower() in eq["name"].lower())
    and (selected_category == "All" or eq["category"] == selected_category)
]

st.subheader("Equipment List")
cols = st.columns(3)
for i, eq in enumerate(filtered):
    with cols[i % 3]:
        if st.button(eq["name"], key=eq["name"]):
            st.session_state["selected_equipment"] = eq
            st.switch_page("pages/Detail.py")

st.markdown("---")
made = "Made by Devansh Kapadia"
st.markdown(
        f"<div style='text-align: center; font-size: 1.0em; margin-bottom: 30px;'>{made}</div>",
        unsafe_allow_html=True
    )

note = "This is an online preview, main product will work offline."
st.markdown(
        f"<div style='text-align: center; font-size: 1.0em; margin-bottom: 30px;'>{note}</div>",
        unsafe_allow_html=True
    )