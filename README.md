
# OCR Text Extractor

A **FastAPI-based OCR service** that extracts text from images using Tesseract OCR. The application handles file uploads, validates images, and returns extracted text with authentication support, ready for deployment on DigitalOcean.

---

## Tech Stack

* **FastAPI** – REST API framework
* **Tesseract / pytesseract** – OCR engine
* **Pillow** – Image processing
* **Jinja2** – Template rendering
* **PyTest** – Testing framework
* **Docker** – Containerization
* **DigitalOcean** – Cloud deployment

---

## Features

* **Image Text Extraction** – Upload images and extract text using Tesseract OCR
* **File Upload Handling** – Validates image formats and sizes
* **Authentication** – API key-based authorization headers
* **Web Interface** – Jinja templates for easy testing
* **Automated Testing** – Comprehensive PyTest suite for file uploads and auth
* **Docker Support** – Ready for containerized deployment
* **One-Click Deploy** – Deploy to DigitalOcean App Platform

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Madhusanka-slc/ocr-text-extractor.git
cd ocr-text-extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Tesseract OCR (on Ubuntu/Debian):

```bash
sudo apt-get install tesseract-ocr
```

Set up environment variables:

```bash
cp .env.sample .env
# Edit .env with your settings
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```

---

This README captures the OCR extraction capabilities and production-ready features from your course. Let me know if you'd like to adjust any details!
