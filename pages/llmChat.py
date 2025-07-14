import streamlit as st
from src.llm_utils import get_llm, tts_speak

llm = get_llm()

eq = st.session_state.get("selected_equipment")
if not eq:
    st.warning("No equipment selected.")
    st.button("Back to Dashboard", on_click=lambda: st.switch_page("app.py"))
    st.stop()

ask = "Ask Phi-2 llm model your questons"
st.markdown(f"<h1 style='text-align: center;'>{ask}</h1>", unsafe_allow_html=True)
made = "This llm is fine-tuned on small data, it might not give an accurate answers , training on large data is in process."
st.markdown(
        f"<div style='text-align: center; font-size: 1.0em; margin-bottom: 30px;'>{made}</div>",
        unsafe_allow_html=True
    )

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "chat_input" not in st.session_state:
    st.session_state["chat_input"] = ""
if "clear_input" not in st.session_state:
    st.session_state["clear_input"] = False


if st.session_state["clear_input"]:
    st.session_state["chat_input"] = ""
    st.session_state["clear_input"] = False

col1, col2 = st.columns([8, 1])

with col1:
    user_q = st.text_input(
        "Type your question or use the mic...",
        key="chat_input",
        label_visibility="collapsed",
        placeholder="e.g. what is an otoscope and what is it used for?"
    )

with col2:
    send_clicked = st.button("Send ➡️", key="send_button")

if send_clicked and user_q.strip():
    prompt = f"Q: {user_q.strip()}, explain?\nA:"
    print("Prompt being sent:", repr(prompt))
    with st.spinner("Generating..."):
        output = llm(
            prompt,
            max_tokens=300,
            temperature=0.7,
            top_p=0.95,
            echo=False
        )
        print("Raw model output:", output)
        answer = output["choices"][0]["text"].strip()
    st.session_state["chat_history"].append(("user", user_q))
    st.session_state["chat_history"].append(("model", answer))
    st.session_state["clear_input"] = True 
    st.rerun()


for i, (speaker, msg) in enumerate(st.session_state["chat_history"]):
    if speaker == "user":
        st.markdown(
            f"<div style='text-align:left; color:#00bfff; margin-bottom:8px;'><b>You:</b> {msg}</div>",
            unsafe_allow_html=True
        )
    else:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(
                f"<div style='text-align:left; color:#00ff00; margin-bottom:8px;'><b>Model:</b> {msg}</div>",
                unsafe_allow_html=True
             )
        with col2:
             if st.button(f"🔊", key=f"tts_{i}"):
                 tts_speak(msg)

# st.markdown("---")
# col1, col2 = st.columns(2)
# with col1:
#     st.button("Back to Dashboard", on_click=lambda: st.switch_page("app.py"))
# with col2:
#     st.button("Back to Details", on_click=lambda: st.switch_page("pages/Detail.py"))

# Example prompts for users
example_prompts = [
    "What is a sphygmomanometer and how is it used?",
    "What is an otoscope and what is it used for?",
    "How do you operate a defibrillator?",
    "What are the safety precautions for using an infusion pump?",
    "Describe the working of a pulse oximeter.",
    "What maintenance is required for an ultrasound machine?",
    "How does a ventilator assist patients?",
    "What is the difference between a CT and MRI scanner?"
]

st.markdown("---")
with st.expander("💡 **Try these example prompts:**", expanded=True):
    for prompt in example_prompts:
        st.markdown(f"- {prompt}")
