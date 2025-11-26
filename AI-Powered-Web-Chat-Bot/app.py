import streamlit as st
import requests

st.set_page_config(
    page_title="ChatWithMe",
    page_icon="🤖",
)
st.title(":rainbow[ChatWithMe]🤖")
st.write(":red[Crafted For Curious Minds]💎")

add_selectbox = st.sidebar.title("About")
text = st.sidebar.write("Welcome to ChatWithMe 🤖  " \
" an interactive AI-powered chatbot that helps you get instant answers, regenerate responses, and share feedback e ffortlessly. " \
"Built with Streamlit and connected to an n8n workflow, this app provides real-time chat, smart message analysis, and feedback-driven improvements. " \
"Enjoy a smooth and responsive chat experience powered by modern AI.")
st.sidebar.markdown("Developed By ShashiKiran")


# Track feedback & for regenerate visibility
if "show_feedback" not in st.session_state:
    st.session_state["show_feedback"] = False

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

prompt = st.chat_input("Ask me anything:")
url = 'https://tinku824.app.n8n.cloud/webhook/b7c68abb-207e-48ec-91e2-e88af427a923'

# Send user prompt to the n8n webhook 
if prompt:
    st.session_state["conversation"].append({"role": "user", "data": prompt})
    st.session_state["show_feedback"] = True   # Show buttons after next assistant reply

    # Spinner for user prompt
    with st.spinner("🤖 Analyzing your message..."):
        response = requests.post(url, json={"prompt": prompt})

    if response.status_code == 200:
        output = response.json().get("output")
        st.session_state["conversation"].append({"role": "assistant", "data": output})
    else:
        st.session_state["conversation"].append({"role": "assistant", "data":f"Error from server : { response.status_code }"})


# --- Render Conversation ---
for i, con in enumerate(st.session_state["conversation"]):

    role = con["role"]
    text = con["data"]

    left, right = st.columns([3, 1])

    # ------------------- ASSISTANT MESSAGE --------------------
    if role == "assistant":
        with left:
            with st.chat_message("assistant"):
                st.write(text)

            # ================================
            # FEEDBACK + REGENERATE BUTTONS
            # Show ONLY if allowed
            # ================================
            if st.session_state["show_feedback"]:

                # 👍 GOOD RESPONSE
                if st.button("👍 Good Response", key=f"good_{i}"):

                    last_user_prompt = st.session_state["conversation"][i-1]["data"]

                    payload = {
                        "prompt": last_user_prompt,
                        "feedback": "good"
                    }

                    # Spinner for feedback sending
                    with st.spinner("✨ Sending feedback..."):
                        fb = requests.post(url, json=payload)

                    if fb.status_code == 200:
                        reply = fb.json().get("output")
                        st.session_state["conversation"].append(
                            {"role": "assistant", "data": reply}
                        )
                        st.session_state["show_feedback"] = False  # Hide all buttons after feedback
                        st.rerun()

                # 👎 BAD RESPONSE
                if st.button("👎 Bad Response", key=f"bad_{i}"):

                    last_user_prompt = st.session_state["conversation"][i-1]["data"]

                    payload = {
                        "prompt": last_user_prompt,
                        "feedback": "bad"
                    }

                    # Spinner for feedback sending
                    with st.spinner("✨ Sending feedback..."):
                        fb = requests.post(url, json=payload)

                    if fb.status_code == 200:
                        reply = fb.json().get("output")
                        st.session_state["conversation"].append(
                            {"role": "assistant", "data": reply}
                        )
                        st.session_state["show_feedback"] = False
                        st.rerun()

                # 🔄 REGENERATE BUTTON (Only visible before feedback)
                if st.button("🔄 Regenerate", key=f"regen_{i}"):

                    last_user_prompt = st.session_state["conversation"][i-1]["data"]

                    # Spinner for regeneration
                    with st.spinner("🔄 Regenerating response..."):
                        regen = requests.post(url, json={"prompt": last_user_prompt})

                    if regen.status_code == 200:
                        new_output = regen.json().get("output")
                        st.session_state["conversation"][i]["data"] = new_output
                        st.rerun()

    # -------------------- USER MESSAGE --------------------
    else:
        with right:
            with st.chat_message("user"):
                st.write(text)
