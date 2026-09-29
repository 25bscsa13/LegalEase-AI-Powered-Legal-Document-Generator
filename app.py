import streamlit as st
import requests

st.set_page_config(
    page_title="LegalEase",
    page_icon="📄",
    layout="wide"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

document_type = st.text_input(
    "Document Type",
    placeholder="Example: Rental Agreement"
)

parties = st.text_area(
    "Parties Involved",
    placeholder="Enter the names of the parties"
)

terms = st.text_area(
    "Terms & Conditions",
    placeholder="Enter the terms and conditions"
)

dates = st.text_input(
    "Effective Date",
    placeholder="DD-MM-YYYY"
)


if st.button("Generate Document"):

    if not document_type or not parties or not terms or not dates:
        st.warning("Please fill in all the fields.")

    else:
        try:
    …