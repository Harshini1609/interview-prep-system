import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Smart Interview Prep", layout="wide")

# -------- CLEAN LIGHT UI CSS --------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #f8fafc;
    color: #1e293b;
}

/* Title */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #0ea5e9;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #475569;
    margin-bottom: 30px;
}

/* Card */
.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    margin-top: 25px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

/* Button */
.stButton>button {
    background: #0ea5e9;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.stButton>button:hover {
    background: #0284c7;
}

</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown("<div class='title'>🚀 Smart Interview Preparation System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Prepare smarter. Crack interviews faster 💼</div>", unsafe_allow_html=True)

st.write("")

# -------- INPUT --------
col1, col2 = st.columns(2)

with col1:
    role = st.selectbox("💼 Select Job Role", [
        "Software Engineer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Web Developer"
    ])

with col2:
    level = st.selectbox("📊 Skill Level", [
        "Beginner",
        "Intermediate",
        "Advanced"
    ])

st.write("")

# -------- SESSION STATE --------
if "generated" not in st.session_state:
    st.session_state.generated = False

# -------- BUTTON --------
if st.button("🚀 Generate Preparation Plan"):
    st.session_state.generated = True

# -------- OUTPUT --------
if st.session_state.generated:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # -------- LOGIC --------
    if role == "Software Engineer":
        topics = ["DSA", "OOP", "DBMS", "OS", "System Design"]
        questions = ["Explain OOP", "What is deadlock?", "What is normalization?"]

    elif role == "Data Analyst":
        topics = ["SQL", "Python", "Pandas", "Statistics", "Visualization"]
        questions = ["Explain joins", "Mean vs Median?", "What is data cleaning?"]

    elif role == "Machine Learning Engineer":
        topics = ["ML Algorithms", "Statistics", "Python", "Model Evaluation"]
        questions = ["What is overfitting?", "Explain regression", "Bias vs Variance"]

    else:
        topics = ["HTML", "CSS", "JavaScript", "React", "Backend"]
        questions = ["What is DOM?", "Flexbox?", "REST API?"]

    # -------- LEVEL TIP --------
    if level == "Beginner":
        tip = "Focus on basics + practice daily"
    elif level == "Intermediate":
        tip = "Build projects + solve medium problems"
    else:
        tip = "Focus on system design + mock interviews"

    # -------- DISPLAY --------
    col1, col2 = st.columns(2)

    progress = []

    with col1:
        st.subheader("📚 Topics to Study")
        for t in topics:
            done = st.checkbox(t, key=f"{role}_{t}")
            progress.append(done)

    with col2:
        st.subheader("❓ Interview Questions")
        for q in questions:
            st.write("👉", q)

    # -------- PROGRESS --------
    completed = sum(progress)
    total = len(progress)

    if total > 0:
        st.progress(completed / total)
        st.write(f"Progress: {completed}/{total} topics completed")

    # -------- GRAPH --------
    df = pd.DataFrame({
        "Topics": topics,
        "Completed": [int(p) for p in progress]
    })

    fig, ax = plt.subplots()
    ax.bar(df["Topics"], df["Completed"])
    ax.set_title("Progress Chart")

    st.pyplot(fig)

    # -------- FOCUS AREA --------
    st.subheader("⚠️ Focus Area")
    st.success(tip)

    st.markdown("</div>", unsafe_allow_html=True)