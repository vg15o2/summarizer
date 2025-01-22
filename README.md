# Text Summarizer

This repository contains a Python script that extracts text from a PDF file and generates a summarized version of the text using the Hugging Face Transformers library. It leverages the `facebook/bart-large-cnn` model for text summarization. The script is designed to handle larger PDFs by chunking the text and summarizing each chunk separately.

## Features

- **Extracts text from PDF files**: Uses the `PyPDF2` library to extract text content from each page of the PDF.
- **Summarizes text**: Utilizes Hugging Face's `facebook/bart-large-cnn` model to summarize the extracted text into a concise version.
- **Handles large PDFs**: Breaks large PDFs into smaller chunks to avoid memory issues and to summarize efficiently.
- **Customizable parameters**: Allows adjustment of chunk size and summary length.

## Requirements

To run the script, you need to have Python installed along with the required dependencies. You can install them using `pip`:

```bash
pip install PyPDF2 transformers textwrap
```
Additionally, you should have the `torch` library installed to use Hugging Face models:

```bash
pip install torch
```
## How to Use

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/vg15o2/summarizer.git
   cd summarizer
   ```
2. **Replace the `file_path`** variable in the script with the path to your PDF file:

   ```python
   file_path = r"your_pdf_file_path.pdf"  # Replace with your PDF file path
3. **Run the script**:

   ```bash
   python textsummarizer2.py
4. The script will output:
   - The first 2000 characters of the extracted text (for preview).
   - A summary of the extracted text.

## Customization

- **Chunk Size**: You can change the `chunk_size` parameter in the `chunk_and_summarize` function to adjust the size of each text chunk that is processed.
- **Summary Length**: You can adjust the `max_length` and `min_length` in the `summarizer` pipeline to control the length of the summary.
   

   
