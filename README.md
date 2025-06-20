# 💼 MedSalaryPredict - Data Scientist Salary Prediction App

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)](https://salarypredict-yourusername.streamlit.app)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/mohan-krishna-kotha/salary-predictor)](https://github.com/mohan-krishna-kotha/salary-predictor/commits/main)
[![Open Issues](https://img.shields.io/github/issues/mohan-krishna-kotha/salary-predictor)](https://github.com/mohan-krishna-kotha/salary-predictor/issues)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/mohan-krishna-kotha/salary-predictor)

MedSalaryPredict is a machine learning web application that predicts the annual salary (in USD) of data science professionals based on their job, experience level, company type, and remote work status. The app supports both manual inputs and bulk predictions via CSV upload.

🔗 **Live App**: [https://salarypredict-yourusername.streamlit.app](https://salary-predictor-oetf6qdcf2vbcu9aui3qtg.streamlit.app/)

---

## 🚀 Features

- 🧠 Predict salary using trained regression models
- 🧾 Input details manually or upload `.csv` for multiple predictions
- 📊 View real-time prediction results
- ⬇️ Download predictions as CSV
- 📈 Accurate model trained on real salary datasets
- 🎨 Streamlit UI with logo placeholder, sidebar, and footer

---

## 📂 Sample CSV Format


---

## 📁 Project Structure


---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Joblib
- Jupyter Notebook

---

## 📈 Model Used

This project uses a **Linear Regression model** trained on encoded features such as:
- Experience Level (`EN`, `MI`, `SE`, `EX`)
- Company Size (`S`, `M`, `L`)
- Employment Type (`FT`, `PT`, `CT`, `FL`)
- Job title, location (numerical encoding)

---

## 👨‍💻 Developed By

**Kotha Mohan Krishna**  
📧 [alwaysmohankrishnan@gmail.com](mailto:alwaysmohankrishnan@gmail.com)

---

## 📌 Run Locally

```bash
# Clone the repo
git clone https://github.com/mohan-krishna-kotha/salary-predictor.git
cd salary-predictor

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

## 📸 Screenshot

![App Screenshot 1](screenshot1.png)  
![App Screenshot 2](screenshot2.png)


---

### ✅ Final To-Do Before Committing:
- Replace `https://salarypredict-yourusername.streamlit.app` with your actual **Streamlit Cloud app URL**.
- Make sure both `screenshot1.png` and `screenshot2.png` are already committed in your GitHub repo root directory.

Let me know if you’d like a PDF version, a LinkedIn post, or help generating a `CONTRIBUTING.md` or `.gitignore`!
