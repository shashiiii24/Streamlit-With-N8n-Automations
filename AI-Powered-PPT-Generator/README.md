# 🎨 AI-Powered PowerPoint Presentation Generator

A smart and fully automated PowerPoint generator built using **Python, Streamlit, python-pptx, and n8n**.  
This tool converts plain text into professionally designed presentation slides with clean layouts, styled titles, bullet formatting, background colors, and consistent theme — all generated with AI.

---

## 🚀 Features

- 🧠 **AI-Generated Slide Structure**  
  Converts raw input text into well-organized slides.

- 🎨 **Automatic Slide Design**  
  Adds clean background colors, professional fonts, titles, and bullet styles.

- 📝 **Smart Text Splitting**  
  Prevents overflow by splitting long content into multiple slides.

- 📌 **AI-Formatted Bullet Points**  
  Each sentence becomes a meaningful bullet (with emojis when helpful).

- 📥 **One-Click PPT Download**  
  Instantly downloads a fully generated `new_ppt.pptx` file.

- 🔗 **Automation Powered by n8n**  
  LLM-generated Python code runs dynamically inside Streamlit.

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit**
- **python-pptx**
- **n8n Automations**
- **LLM (AI Model)**
- **REST API Integration**

---

## 📌 Architecture Overview
User Input ➜ Streamlit UI
➜ n8n Webhook
➜ AI Agent Generates python-pptx Code
➜ Streamlit Executes Code
➜ new_ppt.pptx Generated
➜ User Downloads PPT


---

## 📂 Project Structure

│── app.py # Streamlit frontend
│── generated_code.py # AI-generated PPT code (runtime)
│── new_ppt.pptx # Final generated presentation
│── requirements.txt # Dependencies


---

## ▶️ How to Run Locally

1. **Clone the repository**
## Initialise an empty local repo
```bash
git clone --no-checkout https://github.com/shashiiii24/Streamlit-With-N8n-Automations.git
cd Streamlit-With-N8n-Automations
```

## Turn on sparse checkout
```bash
git sparse-checkout init --cone
```

## Specify the subfolder you want (AI-Powered-Web-Chat-Bot)
```bash
git sparse-checkout set AI-Powered-PPT-Generator
```

## Checkout the files
```bash
git checkout main
```
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```

---

🧠 How It Works

You enter slide titles/content.

Streamlit sends input to n8n workflow.

n8n uses an AI Agent to generate Python code for python-pptx.

Streamlit executes that code to build the PPT automatically.

The final PowerPoint file is served for download.


---
## 🤖 Example Input Format

title: AGENTIC AI
slide1: Introduction to Agentic AI
slide2: Gen AI vs Agentic AI
slide3: Benefits of Agentic AI
slide4: What Are LLMs?
slide5: Thank You

---
## 🔥 Future Enhancements

Add images inside slides

Support templates & themes

Add option to export PDF

Multi-slide preview in UI

Drag-and-drop content builder


----
## 💬 About This Project

This project was built to simplify presentation creation using AI automation.
It speeds up content design, ensures professional formatting, and reduces manual work.

---
## 🎥 Demo Video

Click below to watch the full walkthrough & demo:

[![Watch the video](https://img.youtube.com/vi/p7ov_E0SQaY/maxresdefault.jpg)](https://www.youtube.com/watch?v=p7ov_E0SQaY)



---
# 🧑‍💻 Author

## SHASHI KIRAN TINKU
AI | Automation | Python | Streamlit | n8n | EDA | OpenCV |
Feel free to connect and collaborate!

----

## ⭐ Support

If you like this project, please ⭐ the repository and share it!
Your support motivates more amazing builds ❤

️
---

If you want, I can also:

🔥 Auto-generate a **project banner image**  
🔥 Create **badges** (stars, forks, python version)  
🔥 Make a **minimal version** of the README  
🔥 Create GitHub **repository description + tags**

Just say the word 😎





















