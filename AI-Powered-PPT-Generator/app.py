import streamlit as st
import requests
import subprocess

st.set_page_config(page_title="Presentora AI",page_icon="📝")

# step 1:Title of the web app
st.title(":rainbow[Presentora AI]📝")
st.subheader(":red[Where ideas become presentations.]")

st.sidebar.title("About")
st.sidebar.write("This tool generates clean, professional PowerPoint presentations from your text. " \
"Built with python-pptx and AI-powered formatting, it creates structured slides, consistent design, and high-quality layouts automatically.")
#step 2:Input of the user
user_input = st.text_area("write your content here to generate ppt slides")

#step 3:button to generate ppt
if st.button("Click Here to Generate PPT"): # To generate ppt
    if user_input: #The user should enter some text
        response = requests.post(url="https://tinku824.app.n8n.cloud/webhook/9a44a9f8-051d-4f11-8294-93edaee81d83",
                                 json={"user_input":user_input})
        
        if response.status_code == 200: #The  request was successful
            st.write("success") #python-pptx code
            
            with open("generated_code.py", "w", encoding="utf-8") as f1:
                f1.write(response.json()["output"].strip("```python"))

                
            #step 4:run the presentation.py file to generate ppt
            subprocess.run(["python","generated_code.py"]) # The subprocess is process it can python file inside the python file

            with open(r"D:\power_point\ppt_gen\new_ppt.pptx", "rb") as f: #To read the ppt file
                st.download_button(label="Download PPT file", #To download the ppt file
                                   data=f,
                                   file_name="presentation.pptx"
                )