from io import BytesIO

import requests
import streamlit as st
import base64
import openai

openai.api_key = st.secrets["openai"]["api_key"]

prompts = [
    "a beautiful sunrise over a majestic mountain range with vibrant orange and pink hues lighting up the sky, and a serene lake reflecting the colors",
    "a bustling cityscape at night with glowing neon lights, towering skyscrapers, busy streets filled with cars, and a starry sky above",
    "a serene beach with crystal clear turquoise waters, soft white sand, gently swaying palm trees, and a stunning sunset painting the sky with shades of purple and gold"
]

def get_image_from_DALL_E_3_API(user_prompt,):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=user_prompt,
        size="1792x1024",
        quality="hd",
        n=1,
    )

    image_url = response.data[0].url
    return image_url


def get_image_base64_from_url(image_url):
    response = requests.get(image_url)
    image_data = BytesIO(response.content)
    return base64.b64encode(image_data.read()).decode()


def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


st.set_page_config(layout="wide")

st.markdown("""
<style>
.header {
    font-weight: bold;
    font-size: 3em;
    color: #4CAF50;    
    text-align: center;
}
.header_small {
    font-weight: bold;
    color: #4CAF50;    
    font-size: 2em;
    text-align: center;
}
.subheader {
    font-size: 2em;
    text-align: center;
}
.project {
    text-align: center;
    margin-top: 50px;
}
.social {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 20px 0;
}
.social img {
    width: 80px;
    height: 80px;
    transition: transform 0.3s;
}
.social img:hover {
    transform: scale(1.2);
}
.your-class {
    width: 500px;
    margin: auto;
}
.your-class img {
    width: 100%;
    max-width: 500px;
    height: auto;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.certifications {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
}
.certification {
    text-align: center;
    transition: transform 0.3s;
}
.certification img {
    width: 300px;
    height: auto;
    transition: transform 0.3s;
}
.certification img:hover {
    transform: scale(1.5);
}
.css-1cpxqw2 {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
header a {
    display: none !important;
}

/* Specific to h2 headers */
h2 a {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="header">David Harush</p>', unsafe_allow_html=True)
st.markdown('<p class="header_small">Android/Flutter Developer</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subheader">Welcome! I am a passionate developer with extensive experience in Android and Flutter '
    'development.</p>',
    unsafe_allow_html=True)
st.markdown('<p class="subheader">But in personal life I am a Mushroom Hunter 🍄 and Father of twins 💪.</p>',
            unsafe_allow_html=True)

linkedin_logo = get_image_base64('linkedin.png')
gmail_logo = get_image_base64('gmail.png')
whatsapp_logo = get_image_base64('whatsapp.png')

st.markdown(f"""
<div class="social">
    <a href="https://www.linkedin.com/in/dharush/"><img src="data:image/png;base64,{linkedin_logo}" alt="LinkedIn" style="width: 70px; height: 60px;"></a>
    <a href="mailto:david.harush1@gmail.com"><img src="data:image/png;base64,{gmail_logo}" alt="Gmail" style="width: 60px; height: 60px;"></a>
    <a href="https://wa.me/972543324523"><img src="data:image/png;base64,{whatsapp_logo}" alt="WhatsApp" style="width: 60px; height: 60px;"></a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="project">', unsafe_allow_html=True)

project1_image = get_image_base64('project1.jpg')
project2_image = get_image_base64('project2.jpg')
project3_image = get_image_base64('project3.jpg')

st.markdown('<div class="project">', unsafe_allow_html=True)
st.markdown('<h2>The Movie DB Lab Project</h2>', unsafe_allow_html=True)
st.markdown("""
<p>
    The Movie DB Lab is an amazing project that showcases the power of the TMDB API. 
    This project allows users to search for movies, view details, and explore different categories.
    It's built with modern web technologies and demonstrates a clean, user-friendly interface.
</p>
<p>
    Technologies used in this project include: TMDB API, modern web technologies, and Streamlit for building interactive web applications.
</p>
""", unsafe_allow_html=True)
if st.button('Go to GitHub Project'):
    js = "window.open('https://github.com/davidHarush/TheMovieDbLab')"  # Open new tab
    html = f"<script>{js}</script>"
    st.markdown(html, unsafe_allow_html=True)

st.markdown('<div class="your-class">', unsafe_allow_html=True)
st.markdown(f"""
<div class="social">
    <a><img src="data:image/png;base64,{project1_image}" style="width: 200px; height: 440px;"></a>
    <a><img src="data:image/png;base64,{project2_image}" style="width: 200px; height: 440px;"></a>
    <a><img src="data:image/png;base64,{project3_image}" style="width: 220px; height: 440px;"></a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="project">', unsafe_allow_html=True)
st.markdown('<h2>Education</h2>', unsafe_allow_html=True)
st.markdown("""
2011 – 2013: B.Sc. in Computer Science, HIT
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="project">', unsafe_allow_html=True)
st.markdown('<h2>Professional Experience</h2>', unsafe_allow_html=True)
st.markdown("""
**2023 – Present: Android/Flutter Developer at Zemingo**
- Specializes in Android, iOS, and Flutter development.
- Currently working on an application that captures video and performs facial recognition to compare faces against a database, sending alerts via Telegram (bot API) when a face is detected.
- Tools and technologies: Kotlin, Dart, GitHub, Bitbucket, Jira, Figma.

**2022 – 2023: Android Developer at NVIDIA**
- Worked as a single Android developer in collaboration with software and hardware developers from India and the US.
- Developed an app that displays video and data from a security camera, utilizing webRTC for the video feed.
- Tools and technologies: Kotlin, Gerrit, Redmine, Jira, Figma.

**2021 – 2022: Android Developer at Culture Trip**
- Developed a tourism app as part of a team of five developers based in Israel and London.
- Employed GitFlow, GitHub, and scrum methodology.
- Tools and technologies: Kotlin, Coroutines, GitHub, Jira, Figma.

**2018 – 2021: Android Developer at Ynet**
- Developed the Ynet news application, starting as a single developer and growing to lead a team of five.
- Rebuilt the app from scratch using pure Kotlin with MVVM architecture, Room library, Hilt, Firebase, and more.

**2015 – 2017: Android Developer at Chatway**
- Developed a chat application based on web socket as part of a two-person Android development team.
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="project">', unsafe_allow_html=True)
st.markdown('<h2>Python and AI Learning Journey</h2>', unsafe_allow_html=True)
st.markdown("""
<p>
    We are on the brink of an AI revolution, and Python is the gateway to this revolution. 
    Therefore, I am currently learning Python to be part of this exciting transformation. 
    This project involves building a web application using Streamlit, which showcases my ability to develop interactive and user-friendly interfaces.
</p>
<p>
    Through this project (the current landing page) and others, I learned a lot about Python programming, web development, and using APIs.
    It has been a great journey of learning and growth.
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="project">', unsafe_allow_html=True)

st.markdown('<div class="project">', unsafe_allow_html=True)
st.markdown('<h2>Certifications</h2>', unsafe_allow_html=True)
st.markdown("""
<p>
  this is some of me Certifications there is a lot more, i love to learn new staff.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="certifications">
    <div class="certification">
        <a href="https://www.udemy.com/certificate/UC-a31602cc-41ea-43ab-8578-74cf1c779515/" target="_blank">
            <img src="https://udemy-certificate.s3.amazonaws.com/image/UC-a31602cc-41ea-43ab-8578-74cf1c779515.jpg?v=1661934077000" alt="Udemy: Complete Python Bootcamp">
        </a>
        <p>Udemy: The Complete Flutter Bootcamp</p>
    </div>
    <div class="certification">
        <a href="https://www.udemy.com/certificate/UC-fa9cb366-9ea7-41dc-8f05-e3d666cb5017" target="_blank">
            <img src="https://udemy-certificate.s3.amazonaws.com/image/UC-fa9cb366-9ea7-41dc-8f05-e3d666cb5017.jpg?v=1715588632000" alt="Coursera: Machine Learning">
        </a>
        <p>Udemy: Kotlin Coroutines development</p>
    </div>
    <div class="certification">
        <a href="https://www.linkedin.com/learning/openai-api-for-python-developers/ai-integration-with-python" target="_blank">
            <img src="https://media.licdn.com/dms/image/D4D22AQEaRYte3hsauQ/feedshare-shrink_1280/0/1719349489955?e=1722470400&v=beta&t=b4q45J8_1hd9atWHQtrYKnKG9mCZCjKvSjOwpMPbNr4" alt="LinkedIn Learning: Advanced Android Development">
        </a>
        <p>LinkedIn Learning: OpenAI API for Python Developers</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.success("Now lets have some Fun!!")
selected_prompt = st.radio("Choose a prompt to generate an image:", prompts)

if st.button('Create Image'):
    with st.spinner('Creating image using DALL-E-3 API...'):
        image_url = get_image_from_DALL_E_3_API(selected_prompt)
        image_base64 = get_image_base64_from_url(image_url)
        st.session_state['image'] = image_base64


if 'image' in st.session_state:
    st.markdown(f'<div style="display: flex; justify-content: center;"><img id="dynamic-image" '
                f'src="data:image/png;base64,{st.session_state["image"]}" alt="Dynamic Image" style="max-width: 70%; '
                f'height: auto;"></div>',
                unsafe_allow_html=True)
