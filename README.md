# 🚀 AI Resume Analyzer Pro

An AI-powered Resume Analyzer built using Python, Streamlit, Plotly, PDFPlumber, and Google Gemini AI.

This application helps job seekers analyze their resumes, calculate ATS scores, compare resumes with job descriptions, identify missing skills, and receive AI-powered improvement suggestions.

---

## 📌 Features

### 📄 Resume Analysis

* Upload PDF resumes
* Extract resume text automatically
* Calculate Resume Score
* Calculate ATS Score
* Analyze resume strength

### 🛠 Skills Analysis

* Detect technical skills from resume
* Display identified skills
* Recommend missing skills
* Interactive Skill Distribution Pie Chart

### 💼 Job Description Matching

* Paste a Job Description
* Calculate Job Match Percentage
* Identify missing keywords
* Improve resume-job alignment

### 🤖 AI Feedback

* Powered by Google Gemini AI
* Resume strengths analysis
* Resume weaknesses analysis
* Missing skill recommendations
* ATS optimization suggestions
* Career improvement guidance

### 📊 Dashboard

* Professional dark-themed UI
* Interactive analytics
* Dashboard cards
* Multi-tab navigation

### 📥 PDF Report Generation

* Generate downloadable resume analysis reports
* Share analysis results easily

---

## 🖥️ Application Preview

### Dashboard

Shows:

* Resume Score
* ATS Score
* Job Match Score
* Resume Strength

### Skills Analysis

Shows:

* Detected Skills
* Missing Skills
* Skill Distribution Chart

### Job Match Analysis

Shows:

* Job Match Percentage
* Missing Keywords
* ATS Optimization Suggestions

### AI Feedback

Provides:

* Resume Review
* Skill Gap Analysis
* Career Suggestions
* Resume Improvement Recommendations

---

## 🛠️ Technologies Used

* Python
* Streamlit
* PDFPlumber
* Plotly
* Google Gemini AI
* FPDF2
* Pandas

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_resume.pdf
├── .gitignore
│
├── images/
│   ├── dashboard.png
│   ├── skills.png
│   └── feedback.png
│
└── .streamlit/
    └── secrets_example.toml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Nandinikanchi006/AI-Resume-Analyzer.git
```

```bash
cd AI-Resume-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Setup

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

Get a free Gemini API key from Google AI Studio.

---

## ▶️ Run Application

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

---

## 📈 Future Enhancements

* Resume Section Analysis
* AI Resume Builder
* Resume Ranking System
* LinkedIn Profile Analyzer
* AI Mock Interview Assistant
* Job Recommendation Engine
* Multi-Resume Comparison
* User Authentication & History

---

## 🎯 Use Cases

* Students preparing for placements
* Internship applicants
* Job seekers
* Career switchers
* Professionals optimizing ATS scores

---

## 👨‍💻 Author

### Nandini Kanchi

Computer Science Engineering Student

Aspiring:

* AI Engineer
* Machine Learning Engineer
* Data Scientist
* Software Engineer

GitHub:
https://github.com/Nandinikanchi006

LinkedIn:
https://www.linkedin.com/in/nandini-kanchi-4416a7407

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🛠️ Contribute improvements

📢 Share feedback

---

## 📜 License

This project is open-source and available for educational and learning purposes.
