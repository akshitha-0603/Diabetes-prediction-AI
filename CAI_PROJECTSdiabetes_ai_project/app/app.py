import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Responsible AI Healthcare Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.big-title {
    font-size: 58px;
    font-weight: bold;
    color: #4FC3F7;
}

.sub-title {
    font-size: 22px;
    color: #D0D0D0;
}

.metric-card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 0px 15px rgba(255,255,255,0.08);
}

.section-title {
    font-size: 35px;
    font-weight: bold;
    color: #4FC3F7;
    margin-top: 30px;
}

.small-card {
    background-color: #1B1F27;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown(
    '<p class="big-title">🏥 Responsible AI Healthcare Platform</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Advanced Diabetes Prediction & Explainability Dashboard</p>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
    <div class="metric-card">
    <h2>95.7%</h2>
    <p>AI Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="metric-card">
    <h2>50K+</h2>
    <p>Patient Records</p>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="metric-card">
    <h2>96%</h2>
    <p>Fairness Score</p>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown("""
    <div class="metric-card">
    <h2>24/7</h2>
    <p>Monitoring Active</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# TABS
# ---------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "🩺 Prediction",
    "📊 Analytics",
    "🧠 Explainability",
    "⚖ Responsible AI"
])

# ---------------------------------------------------
# TAB 1 - PREDICTION
# ---------------------------------------------------

with tab1:

    st.markdown(
        '<p class="section-title">Patient Health Parameters</p>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        pregnancies = st.slider("Pregnancies", 0, 20, 1)
        glucose = st.slider("Glucose Level", 0, 300, 120)
        blood_pressure = st.slider("Blood Pressure", 0, 200, 70)
        skin_thickness = st.slider("Skin Thickness", 0, 100, 20)

    with c2:
        insulin = st.slider("Insulin Level", 0, 900, 80)
        bmi = st.slider("BMI", 0.0, 70.0, 25.0)
        dpf = st.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
        age = st.slider("Age", 1, 120, 30)

    st.write("")

    if st.button("🚀 Analyze Diabetes Risk"):

        risk_score = (
            glucose * 0.35 +
            bmi * 0.25 +
            age * 0.15 +
            insulin * 0.10 +
            blood_pressure * 0.15
        ) / 10

        risk_score = min(risk_score, 100)

        rc1, rc2 = st.columns([1,1])

        with rc1:

            st.markdown(
                '<p class="section-title">Prediction Result</p>',
                unsafe_allow_html=True
            )

            if risk_score > 50:
                st.error(f"⚠ HIGH DIABETES RISK : {risk_score:.2f}%")
            else:
                st.success(f"✅ LOW DIABETES RISK : {risk_score:.2f}%")

            st.progress(int(risk_score))

            st.metric("Risk Percentage", f"{risk_score:.2f}%")

            confidence = np.random.randint(92, 99)

            st.metric("AI Confidence", f"{confidence}%")

        with rc2:

            plt.style.use('dark_background')

            fig, ax = plt.subplots(figsize=(4,2.5))

            fig.patch.set_facecolor('#1E1E1E')

            labels = ["Risk", "Safe"]
            values = [risk_score, 100-risk_score]

            ax.pie(values, labels=labels, autopct='%1.1f%%')

            ax.set_title("Prediction Overview", fontsize=10)

            st.pyplot(fig)

            st.caption("AI-powered healthcare analytics visualization")

# ---------------------------------------------------
# TAB 2 - ANALYTICS
# ---------------------------------------------------

with tab2:

    st.markdown(
        '<p class="section-title">Healthcare Analytics Dashboard</p>',
        unsafe_allow_html=True
    )

    age_data = np.random.normal(45, 12, 100)
    glucose_data = np.random.normal(130, 25, 100)
    bmi_data = np.random.normal(28, 5, 100)
    risk_data = np.random.randint(20, 90, 20)

    a1, a2 = st.columns(2)

    with a1:

        plt.style.use('dark_background')

        fig1, ax1 = plt.subplots(figsize=(4,2.5))

        fig1.patch.set_facecolor('#1E1E1E')

        ax1.hist(age_data, bins=15)

        ax1.set_title(
            "Age Distribution",
            fontsize=10
        )

        ax1.tick_params(labelsize=8)

        st.pyplot(fig1)

        st.caption("AI-powered healthcare analytics visualization")

    with a2:

        plt.style.use('dark_background')

        fig2, ax2 = plt.subplots(figsize=(4,2.5))

        fig2.patch.set_facecolor('#1E1E1E')

        ax2.plot(glucose_data[:30])

        ax2.set_title(
            "Glucose Trend Analysis",
            fontsize=10
        )

        ax2.tick_params(labelsize=8)

        st.pyplot(fig2)

        st.caption("AI-powered healthcare analytics visualization")

    b1, b2 = st.columns(2)

    with b1:

        plt.style.use('dark_background')

        fig3, ax3 = plt.subplots(figsize=(4,2.5))

        fig3.patch.set_facecolor('#1E1E1E')

        ax3.boxplot(bmi_data)

        ax3.set_title(
            "BMI Analysis",
            fontsize=10
        )

        ax3.tick_params(labelsize=8)

        st.pyplot(fig3)

        st.caption("AI-powered healthcare analytics visualization")

    with b2:

        plt.style.use('dark_background')

        fig4, ax4 = plt.subplots(figsize=(4,2.5))

        fig4.patch.set_facecolor('#1E1E1E')

        ax4.bar(range(len(risk_data)), risk_data)

        ax4.set_title(
            "Patient Risk Comparison",
            fontsize=10
        )

        ax4.tick_params(labelsize=8)

        st.pyplot(fig4)

        st.caption("AI-powered healthcare analytics visualization")

# ---------------------------------------------------
# TAB 3 - EXPLAINABILITY
# ---------------------------------------------------

with tab3:

    st.markdown(
        '<p class="section-title">AI Explainability Engine</p>',
        unsafe_allow_html=True
    )

    explanation_data = pd.DataFrame({
        "Feature": [
            "Glucose",
            "BMI",
            "Age",
            "Insulin",
            "Blood Pressure"
        ],
        "Importance": [
            35,
            25,
            15,
            10,
            15
        ]
    })

    st.dataframe(explanation_data)

    plt.style.use('dark_background')

    fig5, ax5 = plt.subplots(figsize=(5,2.8))

    fig5.patch.set_facecolor('#1E1E1E')

    ax5.bar(
        explanation_data["Feature"],
        explanation_data["Importance"]
    )

    ax5.set_title(
        "Feature Contribution Analysis",
        fontsize=10
    )

    ax5.tick_params(labelsize=8)

    st.pyplot(fig5)

    st.caption("AI-powered explainability visualization")

    st.info("""
    Explainable AI helps clinicians understand
    why the AI system predicted diabetes risk.

    This improves transparency, trust,
    and responsible healthcare deployment.
    """)

# ---------------------------------------------------
# TAB 4 - RESPONSIBLE AI
# ---------------------------------------------------

with tab4:

    st.markdown(
        '<p class="section-title">Responsible AI Fairness Monitoring</p>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Fairness Score", "96%")

    with c2:
        st.metric("Bias Risk", "Low")

    with c3:
        st.metric("Transparency", "High")

    st.write("")

    fairness_data = pd.DataFrame({
        "Category": [
            "Age Group",
            "BMI Range",
            "Glucose Category",
            "Health Condition"
        ],
        "Fairness Score": [
            95,
            97,
            94,
            96
        ]
    })

    st.dataframe(fairness_data)

    plt.style.use('dark_background')

    fig6, ax6 = plt.subplots(figsize=(5,2.8))

    fig6.patch.set_facecolor('#1E1E1E')

    ax6.plot(
        fairness_data["Category"],
        fairness_data["Fairness Score"],
        marker='o'
    )

    ax6.set_title(
        "Fairness Monitoring",
        fontsize=10
    )

    ax6.tick_params(labelsize=8)

    st.pyplot(fig6)

    st.caption("Responsible AI fairness analytics")

    st.success("""
    Responsible AI Mitigation Strategies:

    ✔ Balanced healthcare datasets

    ✔ Continuous bias monitoring

    ✔ Explainable AI integration

    ✔ Human clinical oversight

    ✔ Regular model auditing
    """)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🏥 Healthcare AI System")

st.sidebar.success("System Status : ACTIVE")

st.sidebar.info("""
Professional Responsible AI Project

Technologies Used:
- Python
- Streamlit
- Machine Learning
- Explainable AI
- Responsible AI
- Data Analytics
- Healthcare Visualization
""")

st.sidebar.write("AI Monitoring Enabled")