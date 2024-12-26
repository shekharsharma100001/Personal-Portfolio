import streamlit as st
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Email configuration (replace with your own email and password)
EMAIL_ADDRESS = "experiment.dummy.acc@gmail.com"
EMAIL_PASSWORD = "vima pabg sryq xkxy"
RECEIVER_EMAIL = "sk262406s@gmail.com"

def send_email(subject, message, sender_email):
    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

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

# Load an image from local file
image_path = os.path.join("C:\\Users\\shekh\\OneDrive\\Desktop\\Portfolio\\images", "pic.png")
image = Image.open(image_path)

# Display the image at the top of the sidebar with various parameters
st.sidebar.image(
    image,
    width=150,  # Adjust the width as needed
    use_column_width=False,
    clamp=True,
    channels="auto",
    output_format="PNG"
)

# You can add other elements to the sidebar below the image
st.sidebar.title("Shekhar Sharma")

# Define a function to manage navigation
def navigate(page):
    st.session_state["page"] = page

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Create sidebar buttons for navigation
if st.sidebar.button("Home"):
    navigate("Home")
if st.sidebar.button("About"):
    navigate("About")
if st.sidebar.button("Skills"):
    navigate("Skills")
if st.sidebar.button("Education"):
    navigate("Education")
if st.sidebar.button("Experience"):
    navigate("Experience")
if st.sidebar.button("Work"):
    navigate("Work")
if st.sidebar.button("Contact"):
    navigate("Contact")

# Display content based on the selected page
page = st.session_state["page"]

if page == "Home":
    st.title("Home")
    col1, col2 = st.columns(2)
    col1.header("Hello, This is Shekhar Sharma.")
    col1.header("Python Developer")
    col1.header("Machine Learning, Artificial Intelligence and Data Science enthusiast")
    home_image_path = os.path.join("C:\\Users\\shekh\\OneDrive\\Desktop\\Portfolio\\images", "home.png")
    col2.image(home_image_path)
elif page == "About":
    st.title("About")
    st.header('Hi, This is Shekhar Sharma')
    st.write('''
🚀 As a B.Tech student majoring in Information Technology 
with a keen interest in Data Science, Machine Learning, and Competitive Programming, I am driven by the power of data to revolutionize industries and solve complex problems. 💡

🔍 With a solid foundation in Python programming and SQL, I am inclined towards extracting insights from data and crafting innovative solutions. My ongoing coursework has equipped me with a comprehensive understanding of algorithms, statistical analysis, and machine learning techniques, empowering me to tackle real-world challenges head-on. 📊

I am passionate about staying abreast of the latest advancements in Data Science and Machine Learning, continuously upgrading my skills to stay at the forefront of this dynamic field. 📚

🤝 I am eager to connect with like-minded professionals, collaborate on exciting projects, and contribute to meaningful endeavours where data-driven innovation drives success. Please feel free to reach out me at shekharsharma100001@gmail.com''')
elif page == "Skills":
    st.title("Skills")
    st.header('Languages and Databases')
    a,b,c,d,e = st.columns(5)
    a.write("Pyhton")
    b.write("R")
    c.write("C++")
    d.write("C")
    e.write("SQL")

    st.header('Languages and Databases')
    a1,b1,c1,d1,e1 = st.columns(5)
    a1.image(r"portfoio_img\python-logo-1.png",caption="Python", use_column_width=True)
    b1.image(r'portfoio_img\matplotlib-logo-1-500x500.jpg',caption="R", use_column_width=True)
    c1.write(r"portfoio_img\numpy-logo-1.png",caption="C++", use_column_width=True)
    d1.image(r"portfoio_img\sk-learn-logo-1.png",caption="C", use_column_width=True)
    e1.image(r"portfoio_img\git.png",caption="SQL", use_column_width=True)


    st.header('Languages and Databases')
    a,b,c,d,e = st.columns(5)
    a.write("Pyhton")
    b.write("R")
    c.write("C++")
    d.write("C")
    e.write("SQL")

    st.header('Languages and Databases')
    a,b,c,d,e = st.columns(5)
    a.write("Pyhton")
    b.write("R")
    c.write("C++")
    d.write("C")
    e.write("SQL")
elif page == "Education":
    st.title("Education")
    st.header('Kamla Nehru Institute of Technology, Sultanpur')
    st.subheader('B.Tech (Information Technology)')
    st.subheader("2022-2026")

    st.header('Kendriya Vidyalaya, Indian Veterinary Research Institute, Bareilly')
    st.subheader('Intermediate (2022)')
    st.subheader('PCM with Computer Science')
    st.subheader("Percentage : 97%")
    
elif page == "Experience":
    st.title("Experience")
    st.write("This is the experience page.")
elif page == "Work":
    st.title("Work")
    st.write("This is the work page.")
elif page == "Contact":
    st.title("Contact")
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
