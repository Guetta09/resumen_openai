import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
from fpdf import FPDF
import os

st.title("Resumidor de PDFs con IA")

uploaded_file = st.file_uploader("Sube tu archivo PDF", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    st.subheader("Texto extraído:")
    st.text_area("Contenido del PDF", value=full_text, height=300)

    if st.button("Generar resumen"):
        with st.spinner("Generando resumen..."):
            summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
            summary = summarizer(full_text, max_length=300, min_length=60, do_sample=False)[0]['summary_text']
            st.success("Resumen generado con éxito.")
            st.subheader("Resumen:")
            st.write(summary)

            # Crear PDF del resumen
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, summary)

            output_filename = "resumen_generado.pdf"
            pdf.output(output_filename)
            with open(output_filename, "rb") as f:
                st.download_button("Descargar resumen en PDF", f, file_name=output_filename)

            os.remove(output_filename)
