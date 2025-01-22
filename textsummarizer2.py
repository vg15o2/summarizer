import PyPDF2
from transformers import pipeline
import textwrap
import logging
from transformers import logging as hf_logging

# Suppress unnecessary Hugging Face logs
hf_logging.set_verbosity_error()  # Only show errors from Hugging Face
logging.basicConfig(level=logging.ERROR)  # General logging level for your script

# Step 1: Extract text from PDF
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):  # Loop through each page
            text += reader.pages[page].extract_text()  # Extract text from each page
    return text

# Step 2: Summarize extracted text using Hugging Face transformers
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)  # Forcing to use CPU
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

# Step 3: Break the text into chunks and summarize each chunk
def chunk_and_summarize(text, chunk_size=1000):
    # Use textwrap to break the text into manageable chunks based on word count (approximately)
    text_chunks = textwrap.wrap(text, chunk_size)
    summaries = []
    
    # Summarize each chunk
    for chunk in text_chunks:
        summaries.append(summarize_text(chunk))
    
    # Combine the chunk summaries into one
    full_summary = " ".join(summaries)
    
    # Summarize the combined summary if it's still too long
    if len(full_summary.split()) > chunk_size:
        full_summary = summarize_text(full_summary)
    
    return full_summary

# Main execution
if __name__ == "__main__":
    file_path = r"C:\Users\Vaishnavi G\OneDrive\Desktop\textsummarizer\attentionisalluneed.pdf"  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(file_path)
    
    if len(extracted_text.strip()) > 0:
        # Print the first 2000 characters of the extracted text (adjust as needed)
        print("\nExtracted Text (First 2000 characters):")
        print(extracted_text[:2000])  # Print the first 2000 characters of the extracted text

        # Summarize the entire extracted text
        summary = chunk_and_summarize(extracted_text)
        print("\nSummary of Extracted Text:")
        print(summary)
    else:
        print("No text extracted from the PDF.")