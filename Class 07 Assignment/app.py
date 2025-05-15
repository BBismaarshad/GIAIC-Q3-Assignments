# Import necessary libraries
import os  # For file operations
import tempfile  # To create temporary files/folders
from PIL import Image, ImageOps, ImageEnhance  # For image processing
import streamlit as st  # For web app interface
from fpdf import FPDF  # For creating PDFs
from io import BytesIO  # For handling binary data
from datetime import datetime  # For timestamping files

class ImageToPDFConverter:
    def __init__(self):
        # Initialize variables to store uploaded files and PDF output
        self.uploaded_files = []  # List to store uploaded images
        self.output_pdf = None  # Will store the final PDF
        self.temp_dir = tempfile.mkdtemp()  # Create a temporary folder for processing
        
        # Default settings for PDF conversion
        self.default_settings = {
            'page_size': 'A4',  # Default paper size
            'orientation': 'portrait',  # Page orientation
            'margin': 10,  # Margin in mm
            'border': False,  # Whether to add borders
            'border_color': '#000000',  # Border color (black)
            'border_width': 5,  # Border width in pixels
            'spread': False,  # Show two images side-by-side
            'spread_gap': 10,  # Gap between images in spread mode
            'enhance': False,  # Enable image enhancement
            'brightness': 1.0,  # Brightness level
            'contrast': 1.0,  # Contrast level
            'sharpness': 1.0,  # Sharpness level
            'compression': False,  # Enable image compression
            'quality': 90,  # Image quality (if compression enabled)
            'output_name': 'converted'  # Default output filename
        }
        self.settings = self.default_settings.copy()  # Current settings
        
    def reset_settings(self):
        # Reset all settings to default values
        self.settings = self.default_settings.copy()
        
    def process_images(self):
        # Process all uploaded images with the current settings
        processed_images = []
        for uploaded_file in self.uploaded_files:
            try:
                # Open the image file
                image = Image.open(uploaded_file)
                
                # Apply image enhancements if enabled
                if self.settings['enhance']:
                    # Adjust brightness
                    enhancer = ImageEnhance.Brightness(image)
                    image = enhancer.enhance(self.settings['brightness'])
                    
                    # Adjust contrast
                    enhancer = ImageEnhance.Contrast(image)
                    image = enhancer.enhance(self.settings['contrast'])
                    
                    # Adjust sharpness
                    enhancer = ImageEnhance.Sharpness(image)
                    image = enhancer.enhance(self.settings['sharpness'])
                
                # Add border if enabled
                if self.settings['border']:
                    border_width = self.settings['border_width']
                    border_color = self.settings['border_color']
                    image = ImageOps.expand(image, border=border_width, fill=border_color)
                
                processed_images.append(image)
            except Exception as e:
                # Show error if image processing fails
                st.error(f"Error processing {uploaded_file.name}: {str(e)}")
                continue
                
        return processed_images
    
    def create_pdf(self, images):
        # Determine page size based on settings
        if self.settings['page_size'].lower() == 'a4':
            page_width, page_height = 210, 297  # A4 size in mm (portrait)
        else:
            page_width, page_height = 297, 210  # Letter size
            
        # Adjust for landscape orientation if needed
        if self.settings['orientation'] == 'landscape':
            page_width, page_height = page_height, page_width
            
        margin = self.settings['margin']  # Get margin setting
        
        # Create PDF object
        pdf = FPDF(unit="mm", format=(page_width, page_height))
        pdf.set_auto_page_break(False)  # Disable automatic page breaks
        
        # Process each image
        for i, image in enumerate(images):
            # Save image to temporary file
            img_path = os.path.join(self.temp_dir, f"temp_img_{i}.jpg")
            
            # Save with compression if enabled
            if self.settings['compression']:
                image.save(img_path, quality=self.settings['quality'], optimize=True)
            else:
                image.save(img_path)
            
            # Handle spread mode (two images per page)
            if self.settings['spread'] and i % 2 == 0 and i < len(images) - 1:
                # Add new page for the spread
                pdf.add_page()
                
                # Get first image details
                img1 = Image.open(img_path)
                img1_width, img1_height = img1.size
                aspect1 = img1_height / img1_width
                
                # Get second image details
                img2_path = os.path.join(self.temp_dir, f"temp_img_{i+1}.jpg")
                img2 = Image.open(img2_path)
                img2_width, img2_height = img2.size
                aspect2 = img2_height / img2_width
                
                # Calculate dimensions to fit both images with gap
                available_width = (page_width - 2 * margin - self.settings['spread_gap']) / 2
                img_width = available_width
                img1_height = img_width * aspect1
                img2_height = img_width * aspect2
                
                # Use the taller image's height for both
                max_height = max(img1_height, img2_height)
                
                # Center vertically
                y_pos = (page_height - max_height) / 2
                
                # Add first image to PDF
                pdf.image(img_path, x=margin, y=y_pos, w=img_width, h=img1_height)
                
                # Add second image to PDF with gap
                pdf.image(img2_path, x=margin + img_width + self.settings['spread_gap'], 
                         y=y_pos, w=img_width, h=img2_height)
                
            else:
                # Skip if in spread mode and this is the second image
                if not self.settings['spread'] or (self.settings['spread'] and i % 2 != 0):
                    continue
                    
                # Single image per page mode
                pdf.add_page()
                img_width, img_height = image.size
                aspect = img_height / img_width  # Calculate aspect ratio
                
                # Calculate maximum available space
                max_width = page_width - 2 * margin
                max_height = page_height - 2 * margin
                
                # Calculate dimensions to fit the page
                img_width_pdf = max_width
                img_height_pdf = img_width_pdf * aspect
                
                # Adjust if too tall
                if img_height_pdf > max_height:
                    img_height_pdf = max_height
                    img_width_pdf = img_height_pdf / aspect
                
                # Center the image on the page
                x_pos = (page_width - img_width_pdf) / 2
                y_pos = (page_height - img_height_pdf) / 2
                
                # Add image to PDF
                pdf.image(img_path, x=x_pos, y=y_pos, w=img_width_pdf, h=img_height_pdf)
        
        # Save PDF to memory (not disk)
        pdf_bytes = BytesIO()
        pdf.output(pdf_bytes)
        pdf_bytes.seek(0)  # Rewind to start of file
        
        return pdf_bytes
    
    def convert(self):
        # Main conversion function
        if not self.uploaded_files:
            st.warning("Please upload at least one image file.")
            return None
            
        # Process all images
        processed_images = self.process_images()
        if not processed_images:
            st.error("No valid images to process.")
            return None
            
        # Create PDF from processed images
        self.output_pdf = self.create_pdf(processed_images)
        return self.output_pdf

def main():
    # Set up the Streamlit web page
    st.set_page_config(page_title="Advanced Image to PDF Converter", page_icon="📄", layout="wide")
    
    # Create converter instance
    converter = ImageToPDFConverter()
    
    # Display title and description
    st.title("📄 Advanced Image to PDF Converter")
    st.markdown("Convert your images to PDF with advanced customization options")
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Upload images section
        st.subheader("Upload Images")
        uploaded_files = st.file_uploader(
            "Choose images to convert", 
            type=["jpg", "jpeg", "png", "bmp", "tiff", "webp"],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            # Store uploaded files and show success message
            converter.uploaded_files = uploaded_files
            st.success(f"{len(uploaded_files)} image(s) uploaded successfully!")
            
            # Show thumbnail previews
            st.subheader("Image Preview")
            cols = st.columns(4)  # Create 4 columns for thumbnails
            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    # Display each image thumbnail
                    image = Image.open(uploaded_file)
                    cols[i % 4].image(image, caption=uploaded_file.name, use_column_width=True)
                except:
                    # Show error if image can't be displayed
                    cols[i % 4].error(f"Couldn't display {uploaded_file.name}")
    
    with col2:
        # PDF settings section
        st.subheader("PDF Settings")
        
        # Basic settings expandable section
        with st.expander("Basic Settings"):
            converter.settings['page_size'] = st.selectbox(
                "Page Size", 
                ["A4", "Letter"], 
                index=0
            )
            converter.settings['orientation'] = st.radio(
                "Orientation", 
                ["portrait", "landscape"], 
                horizontal=True
            )
            converter.settings['margin'] = st.slider(
                "Margin (mm)", 
                min_value=0, 
                max_value=50, 
                value=10
            )
            converter.settings['output_name'] = st.text_input(
                "Output PDF Name", 
                value="converted"
            )
        
        # Border options section
        with st.expander("Border Options"):
            converter.settings['border'] = st.checkbox("Add Border", value=False)
            if converter.settings['border']:
                converter.settings['border_color'] = st.color_picker(
                    "Border Color", 
                    value="#000000"
                )
                converter.settings['border_width'] = st.slider(
                    "Border Width (pixels)", 
                    min_value=1, 
                    max_value=50, 
                    value=5
                )
        
        # Spread mode options
        with st.expander("Spread Options"):
            converter.settings['spread'] = st.checkbox(
                "Create Spreads (2 images per page)", 
                value=False
            )
            if converter.settings['spread']:
                converter.settings['spread_gap'] = st.slider(
                    "Gap between images (mm)", 
                    min_value=0, 
                    max_value=50, 
                    value=10
                )
        
        # Image enhancement options
        with st.expander("Image Enhancement"):
            converter.settings['enhance'] = st.checkbox(
                "Enhance Images", 
                value=False
            )
            if converter.settings['enhance']:
                converter.settings['brightness'] = st.slider(
                    "Brightness", 
                    min_value=0.1, 
                    max_value=2.0, 
                    value=1.0, 
                    step=0.1
                )
                converter.settings['contrast'] = st.slider(
                    "Contrast", 
                    min_value=0.1, 
                    max_value=2.0, 
                    value=1.0, 
                    step=0.1
                )
                converter.settings['sharpness'] = st.slider(
                    "Sharpness", 
                    min_value=0.1, 
                    max_value=2.0, 
                    value=1.0, 
                    step=0.1
                )
        
        # Compression options
        with st.expander("Compression Options"):
            converter.settings['compression'] = st.checkbox(
                "Enable Compression", 
                value=False
            )
            if converter.settings['compression']:
                converter.settings['quality'] = st.slider(
                    "Image Quality", 
                    min_value=1, 
                    max_value=100, 
                    value=90
                )
        
        # Reset button
        if st.button("Reset to Default Settings"):
            converter.reset_settings()
            st.success("Settings reset to default values!")
    
    # Horizontal line separator
    st.markdown("---")
    
    # Convert button
    if st.button("✨ Convert to PDF", type="primary"):
        with st.spinner("Processing images and generating PDF..."):
            # Perform conversion
            pdf_bytes = converter.convert()
            
            if pdf_bytes:
                # Create filename with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_filename = f"{converter.settings['output_name']}_{timestamp}.pdf"
                
                # Show success message
                st.success("PDF generated successfully!")
                
                # Download button
                st.download_button(
                    label="⬇️ Download PDF",
                    data=pdf_bytes,
                    file_name=output_filename,
                    mime="application/pdf"
                )
                
                # PDF preview section
                st.subheader("PDF Preview")
                st.warning("Note: This is just a preview. Download the PDF for full quality.")
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    # Save PDF to temporary file for preview
                    tmp.write(pdf_bytes.getvalue())
                    # Show PDF in iframe
                    st.components.v1.iframe(tmp.name, width=700, height=500)

# Run the app when script is executed
if __name__ == "__main__":
    main()