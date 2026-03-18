import streamlit as st
from PIL import Image
import os
from utils.ocr_processor import extract_text_from_image
from utils.ai_processor import correct_text, extract_todos
from utils.file_export import save_as_txt, save_as_pdf, save_as_docx, save_tasks_csv

st.set_page_config(page_title="Scribble to Digital", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Converter"])

if page == "Home":
    st.title("✍️ Transform Your Handwritten Notes into Smart Digital Content")
    st.markdown("""
    Convert messy notes into clean text and structured to-do lists using OCR and AI.

    ### Features
    - **Upload Notes** – JPG/PNG images
    - **Smart Correction** – Fix spelling & grammar with Gemini AI
    - **To-Do Extraction** – Automatically identify tasks
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("1. Upload")
        st.write("Take a photo of your handwritten notes and upload.")
    with col2:
        st.subheader("2. Enhance & OCR")
        st.write("We enhance the image and extract text.")
    with col3:
        st.subheader("3. AI Polish")
        st.write("Gemini corrects and extracts tasks.")

else:  # Converter page
    st.title("Handwritten Notes Converter")

    uploaded_file = st.file_uploader("Upload an image (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display original image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Convert"):
            with st.spinner("Processing..."):
                # Step 1: OCR
                raw_text = extract_text_from_image(image)
                st.subheader("Raw OCR Text")
                st.text_area("Raw output", raw_text, height=150)

                # Step 2: AI Correction
                corrected = correct_text(raw_text)
                st.subheader("Corrected Digital Notes")
                st.write(corrected)

                # Step 3: To-Do Extraction
                todos = extract_todos(raw_text)
                st.subheader("Extracted To-Do Tasks")
                st.write(todos)

                # Store in session state for export
                st.session_state['corrected'] = corrected
                st.session_state['todos'] = todos

    # Export buttons (appear after processing)
    if 'corrected' in st.session_state:
        st.markdown("---")
        st.subheader("Download Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            txt_data = st.session_state['corrected'].encode()
            st.download_button("Download Text (.txt)", txt_data, file_name="notes.txt")

        with col2:
            # For PDF we need to generate file first (simplified: use save_as_pdf and read back)
            pdf_path = save_as_pdf(st.session_state['corrected'], "temp_notes.pdf")
            with open(pdf_path, "rb") as f:
                st.download_button("Download PDF", f, file_name="notes.pdf")
            os.remove(pdf_path)

        with col3:
            docx_path = save_as_docx(st.session_state['corrected'], "temp_notes.docx")
            with open(docx_path, "rb") as f:
                st.download_button("Download Word", f, file_name="notes.docx")
            os.remove(docx_path)

        # Tasks CSV
        csv_path = save_tasks_csv(st.session_state['todos'], "temp_tasks.csv")
        with open(csv_path, "rb") as f:
            st.download_button("Download Tasks (CSV)", f, file_name="tasks.csv")
        os.remove(csv_path)