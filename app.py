import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------------------------------
# Load sample data (you can replace with your dataset)
# -----------------------------------------------------
DATA_PATH = Path("sample_data/agriculture.csv")
DF = pd.read_csv(DATA_PATH)

# -----------------------------------------------------
# Baseline pipeline (replace with RAG pipeline later)
# -----------------------------------------------------
def process_query(question: str):
    q = question.lower()

    # Example hardcoded logic (will be replaced with RAG)
    if "telangana" in q and "andhra" in q:
        df23 = DF[DF["Year"] == 2023]
        sel = df23[df23["State"].isin(["Telangana", "Andhra Pradesh"])]

        # Summary
        summary = f"Found {len(sel)} matching records for Telangana vs Andhra (2023)."

        # Table
        table = sel

        # Chart
        chart_df = sel.groupby("Crop")["Yield"].mean().reset_index()

        return summary, table, chart_df

    # Default
    sample = DF.head()
    return "Showing a sample of the dataset.", sample, sample


# ---------------------------
# STREAMLIT UI STARTS HERE
# ---------------------------
st.set_page_config(page_title="SMARTXL - Multi RAG Assistant", layout="wide")

st.title("SMARTXL – Multi Entity RAG Assistant")
st.markdown("### Ask questions about your dataset using Natural Language")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        summary, table, chart = process_query(query)

        # Display summary
        st.subheader("📌 Summary")
        st.info(summary)

        # Display table
        st.subheader("📊 Table Result")
        st.dataframe(table)

        # Display chart
        st.subheader("📈 Chart Visualization")
        fig, ax = plt.subplots(figsize=(6,4))
        ax.bar(chart["Crop"], chart["Yield"])
        ax.set_xlabel("Crop")
        ax.set_ylabel("Yield")
        ax.set_title("Yield Comparison")
        st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("SMARTXL – AI Powered Data Analysis Assistant")
