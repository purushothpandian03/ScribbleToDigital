# 📝 Scribble to Digital

Messy Notes Image → Clean Text + To-Do List

## 🔧 Tech Stack

- **Python** – Core language
- **Streamlit** – UI framework
- **OpenCV** – Image enhancement
- **Pytesseract** – OCR text extraction
- **GenAI API** (OpenAI) – Context correction & task extraction

## 📂 Project Structure main files

```
utils/
│
├── ai_processor.py
├── file_export.py
├── ocr_processor.py
└── README.md
```

## 📦 Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

**Note:** You also need Tesseract OCR installed on your system:
- **Windows:** Download from [GitHub - UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- **Mac:** `brew install tesseract`
- **Linux:** `sudo apt-get install tesseract-ocr`

## 🔑 Set GenAI API Key

### Windows (PowerShell)
```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

### Mac/Linux
```bash
export OPENAI_API_KEY="your_api_key_here"
```

## 🧠 Functionalities Breakdown

### 1️⃣ OCR Enhancement (Brighten + Clean Image)
- Improves messy notes before OCR processing
- Uses OpenCV to enhance contrast and clarity
- Applies binary thresholding for optimal text extraction

### 2️⃣ Contextual Logic (GenAI)
- Fixes wrong words detected by OCR
- Repairs broken sentences
- Corrects spelling errors using context

### 3️⃣ To-Do Extraction
- Separates tasks from general notes
- Identifies action items
- Organizes output in a structured format

## ▶️ Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📝 How It Works

1.User uploads an image of handwritten notes, sketches, or to‑do lists via the Streamlit interface.

2.mage preprocessing – The app uses Pillow to read and optionally enhance the image (resize, convert to grayscale, etc.) for better text recognition.

3.Text extraction – The processed image is sent to Google’s Gemini AI model (via google-genai SDK), which can understand handwritten content and extract the raw text.

4.AI structuring – Gemini receives a prompt that asks it to convert the extracted text into a structured list of actionable to‑do items.

5.Display results – The structured to‑do list is shown in the Streamlit app, often with checkboxes or a clean list format for easy interaction.

6.User interaction – The user can review, edit, or mark items as done directly in the interface.

All of this is powered by your Google API key, securely loaded from the .env file using python-dotenv.



Made with ❤️ for cleaner notes!
