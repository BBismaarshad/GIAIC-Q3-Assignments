import streamlit as st
from fpdf import FPDF 
from io import BytesIO
import os

# OOP Class for PDF Generation
class PDFGenerator:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def create_pdf(self) -> BytesIO:
        pdf = FPDF()
        pdf.add_page()
        
        # Add a Unicode-compatible font
        try:
            pdf.add_font('ArialUnicode', '', 'arialuni.ttf', uni=True)
            pdf.set_font('ArialUnicode', size=14)
        except:
            try:
                pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
                pdf.set_font('DejaVu', size=14)
            except:
                pdf.set_font("Arial", size=14)
        
        # Title in blue
        pdf.set_text_color(0, 0, 128)
        pdf.cell(200, 10, txt=self.title, ln=True, align='C')
        pdf.ln(10)

        # Content in black
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 10, txt=self.content)

        # Save to in-memory buffer
        buffer = BytesIO()
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        buffer.write(pdf_bytes)
        buffer.seek(0)
        return buffer

# Streamlit App
def main():
    st.set_page_config(page_title="PDF Generator", page_icon="📄")
    st.title("📄 Simple PDF Generator")
    
    title = st.text_input("Enter PDF Title", "My Document")
    content = st.text_area("Enter PDF Content", "Type your content here...", height=200)
    
    if st.button("Generate PDF"):
        if title and content:
            generator = PDFGenerator(title, content)
            pdf_file = generator.create_pdf()
            
            st.success("✅ PDF generated successfully!")
            st.download_button(
                label="📥 Download PDF",
                data=pdf_file,
                file_name=f"{title}.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("⚠️ Please enter both title and content.")

if __name__ == "__main__":
    main()