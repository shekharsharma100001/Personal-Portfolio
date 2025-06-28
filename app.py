import streamlit as st
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from exp import social_icons
import base64

st.set_page_config(layout="wide", initial_sidebar_state="expanded",)
# Email configuration (replace with your own email and password)
EMAIL_ADDRESS = st.secrets["email"]
EMAIL_PASSWORD = st.secrets["pass"]
RECEIVER_EMAIL = st.secrets["email"]

def send_email(subject, message, sender_email):
    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain",'utf-8'))

    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg.as_string())
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False


ribbon_html = """
    <div class="ribbon">Programming Languages</div>
    <style>
    .ribbon {
        position: relative;
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        color: white;
        padding: 10px 20px;
        font-size: 20px;
        font-weight: bold;
        width: 100%
        text-align: center;
        display: inline-block;
        margin: 20px;
        border-radius: 5px;
    }

    </style>
    """



# Load an image from local file
image_path = os.path.join(r"images/profile.png")
image = Image.open(image_path)

# Display the image at the top of the sidebar with various parameters
st.sidebar.image(
    image,
    width=None,
    use_container_width=True,
    clamp=True,
    channels="auto",
    output_format="PNG",
)

text = '''
<h1 style="text-align: center;">
    <span style="color:#39FF14">Shekhar Sharma</span> 
</h1>
'''
st.sidebar.markdown(text, unsafe_allow_html=True,)

# Define a function to manage navigation
def navigate(page):
    st.session_state["page"] = page

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Create sidebar buttons for navigation
if st.sidebar.button("Home",use_container_width=True):
    navigate("Home")
if st.sidebar.button("About",use_container_width=True):
    navigate("About")
if st.sidebar.button("Skills",use_container_width=True):
    navigate("Skills")
if st.sidebar.button("Education",use_container_width=True):
    navigate("Education")
if st.sidebar.button("Certifications",use_container_width=True):
    navigate("Certifications")
if st.sidebar.button("Experience",use_container_width=True):
    navigate("Experience")
if st.sidebar.button("Projects",use_container_width=True):
    navigate("Projects")
if st.sidebar.button("Contact",use_container_width=True):
    navigate("Contact")
st.sidebar.markdown(social_icons,unsafe_allow_html=True)


# Display content based on the selected page
page = st.session_state["page"]

if page == "Home":
    def get_base64_file(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    # Convert the GIF to Base64
    gif_data = get_base64_file(r"images/github_banner.gif")
    # Embed the GIF in HTML
    st.markdown(
    f'<img src="data:image/gif;base64,{gif_data}" alt="Animated GIF" style="width:100%;">',
    unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.header('')
    col1.header("Hello, This is :green[Shekhar Sharma].")
    col1.header("Python Developer")
    col1.header("Machine Learning, Artificial Intelligence and Data Science enthusiast")
    col2.image(r"images/home.png",use_container_width=True)



elif page == "Certifications":
    st.title(":orange[Certifications]")
    with st.container(border = True):
        cert1, img1 = st.columns(2)
        cert1.header("Principles of Generative AI")
        cert1.subheader("Infosys SpringBoard")
        cert1.write("Gained foundational understanding of generative models, including applications like text and image generation.")
        img1.image(r'images/GenAI.png',use_container_width=True)
    with st.container(border = True):
        cert2, img2 = st.columns(2)
        cert2.header("Artificial Intelligence Primer Certification")
        cert2.subheader("Infosys SpringBoard")
        cert2.write("Covered AI concepts, algorithms, and real-world use cases across multiple domains and industries.")
        img2.image(r'images/AI.png',use_container_width=True)
    with st.container(border = True):
        cert3, img3 = st.columns(2)
        cert3.header("Natural Language Processing")
        cert3.subheader("Infosys SpringBoard")
        cert3.write("Learned techniques to analyze, process, and generate human language using NLP libraries and models.")
        img3.image(r'images/NLP.png',use_container_width=True)
    with st.container(border = True):
        cert4, img4 = st.columns(2)
        cert4.header("Computer Vision")
        cert4.subheader("Infosys SpringBoard")
        cert4.write("Learned image processing techniques and object detection using deep learning and OpenCV tools.")
        img4.image(r'images/CV.png',use_container_width=True)
    with st.container(border = True):
        cert5, img5 = st.columns(2)
        cert5.header("Deep Learning for Developers")
        cert5.subheader("Infosys SpringBoard")
        cert5.write("Built and trained deep neural networks using frameworks like TensorFlow and Keras for practical tasks.")
        img5.image(r'images/DL.png',use_container_width=True)
    with st.container(border = True):
        cert6, img6 = st.columns(2)
        cert6.header("Data Science")
        cert6.subheader("Infosys SpringBoard")
        cert6.write("Explored data handling, visualization, and statistical methods using Python and real-world datasets.")
        img6.image(r'images/DS.png',use_container_width=True)
    with st.container(border = True):
        cert7, img7 = st.columns(2)
        cert7.header("Tableau")
        cert7.subheader("Itronix Solutions")
        cert7.write("Mastered data visualization and analytical storytelling using Tableau.")
        img7.image(r'images/itronix.jpg',use_container_width=True)
    with st.container(border = True):
        cert8, img8 = st.columns(2)
        cert8.header("Industrial Training on Coding Skills")
        cert8.subheader("Java T Point")
        cert8.write("Mastered the concepts of Object Oriented Programming and various data structures through the 2 months industrial training program conducted by TPoint Tech.")
        img8.image(r'images/JavaTPoint.png',use_container_width=True)




elif page == "About":
    st.title(":orange[About]")
    con = st.container(border=True)
    con.header('Hi, This is Shekhar Sharma')
    con.write('''
🚀 As a B.Tech student majoring in Information Technology 
with a keen interest in Data Science, Machine Learning, and Competitive Programming, I am driven by the power of data to revolutionize industries and solve complex problems. 💡

🔍 With a solid foundation in Python programming and SQL, I am inclined towards extracting insights from data and crafting innovative solutions. My ongoing coursework has equipped me with a comprehensive understanding of algorithms, statistical analysis, and machine learning techniques, empowering me to tackle real-world challenges head-on. 📊

I am passionate about staying abreast of the latest advancements in Data Science and Machine Learning, continuously upgrading my skills to stay at the forefront of this dynamic field. 📚

🤝 I am eager to connect with like-minded professionals, collaborate on exciting projects, and contribute to meaningful endeavours where data-driven innovation drives success. Please feel free to reach out me at shekharsharma100001@gmail.com''')
    


elif page == "Skills":
    st.title(":orange[Skills]")

    st.header('Programming Languages')
    con = st.container(border=True)
    p1,p2,p3,p4,p5 = con.columns(5)
    p1.image(r"images/portfolio_img/py_logo.png",caption="Python", use_container_width=True)
    p2.image(r'images/portfolio_img/R.png',caption="R", use_container_width=True)
    p3.image(r"images/portfolio_img/cpp.png",caption="C++", use_container_width=True)
    p4.image(r"images/portfolio_img/c.png",caption="C", use_container_width=True)
    p5.image(r"images/portfolio_img/java.png",caption="Java", use_container_width=True)
    p6,p7,p8,p9,p10 = con.columns(5)
    p6.image(r"images/portfolio_img/js.png",caption="Java Script", use_container_width=True)


    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)

    st.header('Libraries')
    con2 = st.container(border=True)
    l1,l2,l3,l4,l5 = con2.columns(5)
    l1.image(r"images/portfolio_img/numpy.png",caption="Numpy", use_container_width=True)
    l2.image(r'images/portfolio_img/Pandas.png',caption="Pandas", use_container_width=True)
    l3.image(r"images/portfolio_img/mat.png",caption="Matplotlib", use_container_width=True)
    l4.image(r"images/portfolio_img/scikit.png",caption="Scikit Learn", use_container_width=True)
    l5.image(r"images/portfolio_img/seaborn.png",caption="Seaborn", use_container_width=True)
    l6,l7,l8,l9,l10 = con2.columns(5)
    l6.image(r"images/portfolio_img/tkinter.png",caption="Tkinter", use_container_width=True)
    l7.image(r"images/portfolio_img/selenium.1024x993.png",caption="Selenium", use_container_width=True)
    l8.image(r"images/portfolio_img/soup.png",caption="Beautiful Soup", use_container_width=True)
    l9.image(r"images/portfolio_img/cv2.png",caption="Open CV", use_container_width=True)
    l10.image(r"images/portfolio_img/Keras.png",caption="Keras", use_container_width=True)
    l11,l12,l13,l14,l15 = con2.columns(5)
    l11.image(r"images/portfolio_img/TensorFlow.png",caption="TensorFlow", use_container_width=True)
    l12.image(r"images/portfolio_img/PyTorch.png",caption="PyTorch", use_container_width=True)
    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)

    
    st.header('Frameworks')
    con3 = st.container(border=True)
    f1,f2,f3,f4,f5 = con3.columns(5)
    f1.image(r"images/portfolio_img/streamlt.png",caption="Streamlit", use_container_width=True)
    f2.image(r"images/portfolio_img/flask.png",caption="Flask", use_container_width=True)
    f3.image(r"images/portfolio_img/FastAPI.png",caption="FastAPI", use_container_width=True)
    f4.image(r"images/portfolio_img/langchain.png",caption="LangChain", use_container_width=True)
    f5.image(r"images/portfolio_img/langgraph-color.png",caption="LangGraph", use_container_width=True)
    f6,f7,f8,f9,f10 = con3.columns(5)
    f6.image(r"images/portfolio_img/llama.png",caption="LlamaIndex", use_container_width=True)
    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)
    
    st.header('Databases & Vector Stores')
    con4 = st.container(border=True)
    a3,b3,c3,d3,e3 = con4.columns(5)
    a3.image(r"images/portfolio_img/sql.png",caption="MySQL", use_container_width=True)
    b3.image(r"images/portfolio_img/mongo.png",caption="MongoDB", use_container_width=True)
    c3.image(r"images/portfolio_img/chromaDB.png",caption="ChromaDB", use_container_width=True)
    d3.image(r"images/portfolio_img/faiss.png",caption="FAISS", use_container_width=True)
    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)
    
    st.header('Data Analysis Tools')
    con4 = st.container(border=True)
    d1,d2,d3,d4,d5 = con4.columns(5)
    d1.image(r"images/portfolio_img/tableu.png",caption="Tableu", use_container_width=True)
    d2.image(r"images/portfolio_img/powerbi.png",caption="Power BI", use_container_width=True)
    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)

    
    st.header('Developer Tools')
    con5 = st.container(border=True)
    t1,t2,t3,t4,t5 = con5.columns(5)
    t1.image(r"images/portfolio_img/git.png",caption="Git", use_container_width=True)
    t2.image(r"images/portfolio_img/anaconda.png",caption="Anaconda Navigator", use_container_width=True)
    t3.image(r"images/portfolio_img/colab.png",caption="Google Colab", use_container_width=True)
    t4.image(r"images/portfolio_img/Docker.png",caption="Docker", use_container_width=True)
    t5.image(r"images/portfolio_img/AWS.png",caption="AWS", use_container_width=True)
    st.markdown("<hr style='border: none; height: 10px; background-color: ##74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)



elif page == "Education":
    st.title(":orange[Education]")
    des1, des_img1 = st.columns(2)
    c1 = des1.container(border= True)
    c1.header(":blue[Kamla Nehru Institute of Technology, Sultanpur]")
    c1.subheader('B.Tech (2022-2026)')
    c1.subheader('Information Technology')
    c1.subheader("CGPA: 9.23")
    des_img1.image(r"images/knit.gif", use_container_width=True)

    des2, des_img2 = st.columns(2)
    c2 = des2.container(border= True)
    c2.header(":blue[Kendriya Vidyalaya, Indian Veterinary Research Institute, Bareilly]")
    c2.subheader('Intermediate (2022)')
    c2.subheader('PCM with Computer Science')
    c2.subheader("Percentage : 97%")
    des_img2.image(r"images/ivri.gif", use_container_width=True)
    pic1,pic2,pic3 = st.columns(3)
    pic1.image(r"images/ivri1.jpg",use_container_width=True)
    pic2.image(r"images/ivri2.jpg",use_container_width=True)
    pic3.image(r"images/knit.jpg",use_container_width=True)
    


elif page == "Experience":
    st.title(":orange[Experience]")
    with st.container(border = True):
        des,pic = st.columns(2)
        pic.image(r'images/exp.png',use_container_width=True)
        des.header("AI: Transformative Learning with TechSaksham")
        pic.subheader("Edunet Foundation")
        pic.write("Worked as an Intern  with TechSaksham - A joint CSR initiative of Microsoft & SAP, focusing on AI Technologies")
        des.subheader("Worked on project: Human Pose Estimation using Machine Learning")
        des.write("Developed a system for detecting and analyzing human body poses using advanced machine learning techniques. Gained hands-on experience with OpenCV, MediaPipe, and deep learning frameworks for keypoint detection. Enhanced skills in computer vision, data preprocessing, and model optimization. The project emphasized real-time applications in motion tracking and human-computer interaction.")
    with st.container(border = True):
        des,pic = st.columns(2)
        pic.image(r'images/exp.png',use_container_width=True)
        des.header("AI: Transformative Learning with TechSaksham")
        pic.subheader("Edunet Foundation")
        pic.write("Worked as an Intern  with TechSaksham - A joint CSR initiative of Microsoft & SAP, focusing on AI Technologies")
        des.subheader("Worked on project: Human Pose Estimation using Machine Learning")
        des.write("Developed a system for detecting and analyzing human body poses using advanced machine learning techniques. Gained hands-on experience with OpenCV, MediaPipe, and deep learning frameworks for keypoint detection. Enhanced skills in computer vision, data preprocessing, and model optimization. The project emphasized real-time applications in motion tracking and human-computer interaction.")



elif page == "Projects":
    st.title(":orange[Personal Projects]")
    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)

    st.header('StreamDigest')
    p1, p2 = st.columns(2)
    p1.image(r"images/portfolio_img/summarizer.png", use_container_width=True)
    p2.write('### Project Description:')
    p2.write('Created a web application that geneartes summary of given Yt video. It fetches the trascript of video and summarizes that transcript in English. The summary can be imported as pdf file.')
    tech_stack = [
    "Python - Programming Language",
    "Streamlit - Frontend Framework for Web Applications",
    "Google Generative AI - For generating summaries using advanced AI models",
    "YouTube Transcript API - For extracting transcripts from YouTube videos"
]
    # Display the tech stack as a bulleted list
    p2.write("### Tech Stack:")
    for tech in tech_stack:
        p2.write(f"- {tech}")
    p2.markdown("👉 [**Project Link**](https://stream-digest.streamlit.app/)")
    p2.markdown("👉 [**Github Repository**](https://github.com/shekharsharma100001/Stream-Digest.git)")


    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)
    st.header('Endorse- Telegram Bot')
    p3,p4 = st.columns(2)
    p3.image(r"images/portfolio_img/endorse.png", use_container_width=True)
    p4.write('### Project Description:')
    p4.write('Crafted a Telegram bot named **Endorse** to assist college students. This Bot allows students to access curated study materials for all subjects, including lecture notes, textbooks, and other additional resources with an intuitive interface, find resources quickly anytime, anywhere via Telegram.')
    tech_stack2 = [
    "Python - Programming Language",
    "Telebot API - For interacting with users, send messages, and receive commands.",
    "Hugging Face API - For Chat Bot functionality",
]

    # Display the tech stack as a bulleted list
    p4.write("### Tech Stack:")
    for tech in tech_stack2:
        p4.write(f"- {tech}")
    p4.markdown("👉 [**Project Link**](https://www.linkedin.com/posts/shekhar100001_ai-ml-python-activity-7213944868753063936-gMCz?utm_source=share&utm_medium=member_desktop)")

    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)
    st.header('Computer Vision with IOT')
    p5,p6 = st.columns(2)
    p5.image(r"images/portfolio_img/computer_vision.png", use_container_width=True)
    p6.write('### Project Description:')
    p6.write('This project is basically the Convergence of Computer Vision and IoT: A New Era of Intelligent Systems. Using OpenCV, MediaPipe and Microcontroller ESP8266, developed a system where simple hand gestures control the lamp, making it more intuitive and user-friendly.')
    tech_stack3 = [
    "Python - Programming Language",
    "Open CV - For Detecting hand gesture",
    "Blynk Cloud - For controlling devices from anywhere over the network",
]
    # Display the tech stack as a bulleted list
    p6.write("### Tech Stack:")
    for tech in tech_stack3:
        p6.write(f"- {tech}")
    p6.markdown("👉 [**Project Link**](https://www.linkedin.com/posts/shekhar100001_machinelearning-ai-computervision-activity-7230566695545806850-ZOax?utm_source=share&utm_medium=member_desktop)")
    p6.markdown("👉 [**Github Repository**](https://github.com/shekharsharma100001/ComputerVision)")

    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)

    st.header('Word Guess')
    p7,p8 = st.columns(2)
    p7.image(r"images/portfolio_img/word_guess.png", use_container_width=True)
    p8.write('### Project Description:')
    p8.write('The Word Guess Game is a software project that provides interactive GUI and sound effects. User is asked with some hints and the Game accurately guesses the word that player thinks of.')
    tech_stack4 = [
    "Python - Programming Language",
    "Tkinter Library - For creating GUI of game",
    "Pygame Libray - For adding sound effects in game",
]
    # Display the tech stack as a bulleted list
    p8.write("### Tech Stack:")
    for tech in tech_stack4:
        p8.write(f"- {tech}")
    p8.markdown("👉 [**Github Repository**](https://github.com/shekharsharma100001/word-guess)")

    st.markdown("<hr style='border: none; height: 10px; background-color: #74cc08; width: 100%; margin: 20px left;' />", unsafe_allow_html=True)

    st.header('Rock-Paper-Scissors')
    p9,p10 = st.columns(2)
    p9.image(r"images/portfolio_img/rsp.png", use_container_width=True)
    p10.write('### Project Description:')
    p10.write('The "Rock-Paper-Scissors Game with Tkinter" project aims to bring the classic hand game to life through an interactive and visually engaging graphical user interface (GUI)')
    tech_stack4 = [
    "Python - Programming Language",
    "Tkinter Library - For creating GUI of game",
    "Pygame Libray - For adding sound effects in game",
]
    # Display the tech stack as a bulleted list
    p10.write("### Tech Stack:")
    for tech in tech_stack4:
        p10.write(f"- {tech}")
    p10.markdown("👉 [**Github Repository**](https://github.com/shekharsharma100001/Rock-paper-scissors)")



elif page == "Contact":
    st.title(":orange[Contact]")
    first, last = st.columns(2)
    fname = first.text_input('First Name')
    lname = last.text_input('Last Name')
    email, mob = st.columns([3, 1])
    sender_email = email.text_input('E-mail')
    phone = mob.text_input('Contact Number')
    message1 = st.text_area("Message")
    message = f"{fname} {lname}\n{sender_email}\n{phone}\n{message1}"
    subject = 'Message from Portfolio'
    sub = st.button("Submit")
    if sub:
        if fname and lname and sender_email and phone and message1:
            success = send_email(subject, message, sender_email)
            if success:
                st.success("Your message has been sent successfully!")
        else:
            st.error("Please fill out all fields.")
    st.markdown(social_icons,unsafe_allow_html=True)
