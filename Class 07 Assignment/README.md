
# 📄 Advanced Image to PDF Converter

A powerful and flexible Streamlit-based web application that allows users to convert multiple images into a single PDF file with advanced customization options such as borders, page layouts, image enhancement, and compression.

## 🚀 Features

- 📂 **Multi-image Upload**: Supports JPG, PNG, BMP, TIFF, and WebP.
- 📐 **Custom PDF Settings**:
  - Page size (A4 / Letter)
  - Orientation (Portrait / Landscape)
  - Margins
- 🎨 **Borders**:
  - Optional borders with customizable width and color
- 📖 **Spread Mode**:
  - Place two images side by side in a single PDF page
- ✨ **Image Enhancements**:
  - Brightness, Contrast, and Sharpness adjustments
- 📦 **Compression**:
  - Compress images with adjustable quality
- 📥 **PDF Download**:
  - Download final PDF with timestamped filename
- 🖼️ **Preview Thumbnails and PDF Viewer**

> Upload images → Customize settings → Convert to PDF → Download or Preview it directly in the app!

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pillow (PIL)](https://python-pillow.org/)
- [FPDF](https://py-pdf.github.io/fpdf2/)

## 📦 Installation

```
git clone https://github.com/your-username/image-to-pdf-converter.git
```
```
cd app.py
```
```
pip install -r requirements.txt
```

## ▶ Usage
Run the app locally using:
```
streamlit run app.py
```
## 💡 How It Works
Upload one or more images via the sidebar.

Customize PDF settings: page size, orientation, margin, borders, etc.

Optionally enable image enhancements or compression.

Click "Convert to PDF".

Download the PDF or preview it directly in the app.

## Author
Developed by Bisma Arshad
Inspired by the need for a user-friendly, advanced image-to-PDF tool.

## 📃 License
This project is licensed under the MIT Licen
