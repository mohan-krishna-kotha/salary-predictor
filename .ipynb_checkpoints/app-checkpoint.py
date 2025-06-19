import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/salary_model.pkl')

# Define encoding maps (must match training notebook)
experience_map = {'EN': 0, 'MI': 1, 'SE': 2, 'EX': 3}
employment_map = {'FT': 0, 'PT': 1, 'CT': 2, 'FL': 3}
company_size_map = {'S': 0, 'M': 1, 'L': 2}

# ----------------------------
# Manual Input Prediction
# ----------------------------
st.title("💼 Salary Prediction App")

st.header("📍 Predict from Manual Input")

experience_level = st.selectbox("Experience Level", list(experience_map.keys()))
employment_type = st.selectbox("Employment Type", list(employment_map.keys()))
remote_ratio = st.slider("Remote Work Ratio", 0, 100, 100)
company_size = st.selectbox("Company Size", list(company_size_map.keys()))
work_year = st.selectbox("Work Year", [2020, 2021, 2022, 2023, 2024])

# These are numerical inputs (user must provide encoded numbers)
job_title = st.number_input("Job Title (encoded number)", min_value=0, max_value=100)
employee_residence = st.number_input("Employee Residence (encoded number)", min_value=0, max_value=100)
company_location = st.number_input("Company Location (encoded number)", min_value=0, max_value=100)

if st.button("🔮 Predict Salary"):
    try:
        input_data = pd.DataFrame([[
            int(work_year),
            experience_map[experience_level],
            employment_map[employment_type],
            int(job_title),
            int(employee_residence),
            int(remote_ratio),
            int(company_location),
            company_size_map[company_size]
        ]], columns=['work_year', 'experience_level', 'employment_type',
                     'job_title', 'employee_residence', 'remote_ratio',
                     'company_location', 'company_size'])

        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Salary (USD): ${prediction:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")

# ----------------------------
# CSV Upload Prediction
# ----------------------------
st.markdown("---")
st.header("📁 Predict from Uploaded CSV")

uploaded_file = st.file_uploader("Upload a CSV with the same column structure", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Apply same encoding as during training
        df['experience_level'] = df['experience_level'].map(experience_map)
        df['employment_type'] = df['employment_type'].map(employment_map)
        df['company_size'] = df['company_size'].map(company_size_map)

        # Make predictions
        predictions = model.predict(df)
        df['Predicted_Salary(USD)'] = predictions

        st.success("✅ Predictions completed!")
        st.dataframe(df)

        # Allow download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Prediction Results", data=csv,
                           file_name="predicted_salaries.csv", mime="text/csv")

    except Exception as e:
        st.error(f"⚠️ File processing failed: {e}")
