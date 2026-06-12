import streamlit as st
import pdfplumber
import plotly.express as px
import google.generativeai as genai
from fpdf import FPDF
import os

# --------------------------
# PAGE CONFIG
# --------------------------

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="🚀",
    layout="wide"
)

# --------------------------
# GEMINI CONFIG
# --------------------------

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.5-flash")
    gemini_available = True
except:
    gemini_available = False

# --------------------------
# CUSTOM CSS
# --------------------------

st.markdown("""
<style>

.stApp{
background-color:#0E1117;
}

.card{
background:#1E293B;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0px 4px 15px rgba(0,229,255,0.2);
}

.big{
font-size:30px;
font-weight:bold;
color:#00E5FF;
}

h1,h2,h3{
color:#00E5FF;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# TITLE
# --------------------------

st.title("🚀 AI Resume Analyzer Pro")
st.write("Upload your Resume and compare it with a Job Description.")

# --------------------------
# INPUTS
# --------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# --------------------------
# MAIN PROCESS
# --------------------------

if uploaded_file:

    text = ""

    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + " "

    except Exception as e:
        st.error(f"PDF Error: {e}")
        st.stop()

    skills = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "SQL",
        "Data Science",
        "Java",
        "Power BI",
        "Excel",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "PyTorch",
        "Tableau",
        "AWS",
        "Docker",
        "Git",
        "Flask",
        "Streamlit",
        "Statistics",
        "NLP",
        "Computer Vision"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    missing_skills = [
        skill for skill in skills
        if skill not in found_skills
    ]

    resume_score = min(len(found_skills) * 5, 100)

    ats_score = int(
        (len(found_skills) / len(skills)) * 100
    )

    # --------------------------
    # JOB MATCH
    # --------------------------

    match_score = 0
    missing_keywords = []

    if job_description.strip():

        jd_words = set(job_description.lower().split())
        resume_words = set(text.lower().split())

        if len(jd_words) > 0:

            matched_words = jd_words.intersection(
                resume_words
            )

            match_score = int(
                len(matched_words)
                / len(jd_words)
                * 100
            )

            missing_keywords = list(
                jd_words - resume_words
            )

    # --------------------------
    # DASHBOARD CARDS
    # --------------------------

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class='card'>
            <h3>Resume Score</h3>
            <div class='big'>{resume_score}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class='card'>
            <h3>ATS Score</h3>
            <div class='big'>{ats_score}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class='card'>
            <h3>Job Match</h3>
            <div class='big'>{match_score}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # --------------------------
    # TABS
    # --------------------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Dashboard",
            "Skills",
            "Job Match",
            "AI Feedback"
        ]
    )

    # --------------------------
    # DASHBOARD TAB
    # --------------------------

    with tab1:

        st.subheader("Resume Strength")

        st.progress(resume_score)

        st.write(
            f"Resume contains {len(found_skills)} recognised skills."
        )

        chart_data = {
            "Category": [
                "Detected Skills",
                "Missing Skills"
            ],
            "Count": [
                len(found_skills),
                len(missing_skills)
            ]
        }

        fig = px.pie(
            chart_data,
            names="Category",
            values="Count",
            hole=0.5,
            title="Skill Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------
    # SKILLS TAB
    # --------------------------

    with tab2:

        st.subheader("Detected Skills")

        for skill in found_skills:
            st.success(skill)

        st.subheader("Recommended Skills")

        for skill in missing_skills:
            st.info(skill)

    # --------------------------
    # JOB MATCH TAB
    # --------------------------

    with tab3:

        st.subheader("Job Description Match")

        st.progress(match_score)

        st.write(
            f"Match Score: {match_score}%"
        )

        st.subheader(
            "Missing Keywords"
        )

        if missing_keywords:

            for keyword in missing_keywords[:20]:
                st.warning(keyword)

        else:
            st.success(
                "No major keywords missing."
            )

    # --------------------------
    # AI FEEDBACK TAB
    # --------------------------

    with tab4:

        st.subheader(
            "AI Resume Review"
        )

        if gemini_available:

            if st.button(
                "Generate AI Feedback"
            ):

                prompt = f"""
                Analyze this resume.

                Resume:
                {text}

                Give:

                1. Strengths
                2. Weaknesses
                3. Missing Skills
                4. ATS Improvements
                5. Career Suggestions
                """

                with st.spinner(
                    "Analyzing..."
                ):

                    response = model.generate_content(
                        prompt
                    )

                    st.write(
                        response.text
                    )

        else:
            st.warning(
                "Gemini API key not configured."
            )

    # --------------------------
    # PDF REPORT
    # --------------------------

    if st.button(
        "Generate PDF Report"
    ):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=12
        )

        pdf.cell(
            200,
            10,
            "Resume Analysis Report",
            ln=True
        )

        pdf.cell(
            200,
            10,
            f"Resume Score: {resume_score}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            f"ATS Score: {ats_score}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            f"Job Match: {match_score}",
            ln=True
        )

        pdf.output(
            "resume_report.pdf"
        )

        with open(
            "resume_report.pdf",
            "rb"
        ) as file:

            st.download_button(
                "Download Report",
                file,
                file_name="resume_report.pdf"
            )

else:

    st.info(
        "Upload a PDF Resume to begin."
    )