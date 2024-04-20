# Gemini Invoice Extractor

The Gemini Invoice Extractor is an AI-powered tool designed to extract information from invoice images. It utilizes the Gemini AI model to analyze uploaded invoice images and respond to user queries based on the extracted information.

![invoice extractor demo](https://github.com/Yusra-Zafar/gemini-invoice-extractor/assets/141744510/64aeeddf-9e84-4ce9-aa4e-f7932cb08ee7)


## Features

- Extracts minute details from invoice images
- Provides precise and to-the-point responses to user queries
- Handles only queries relevant to the invoice image

## Usage

1. Obtain a Gemini API key.
2. Enter the key in the sidebar input field.
3. Upload an invoice image using the file uploader.
4. Input your query related to the invoice in the text input box.
5. Click "Process" to extract information and get a response from the Gemini Invoice Extractor.

## Dependencies

- `os`: Provides a way to interact with the operating system.
- `google.generativeai`: Library for accessing the Gemini AI model.
- `streamlit`: Python library for building web applications.
- `dotenv`: Python library for managing environment variables.
- `PIL`: Python Imaging Library for image processing.

## How to Run

1. Clone the repository.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Run the application using `streamlit run gemini_invoice_extractor.py`.
4. Enter your Gemini API key in the provided input field.
5. Upload an invoice image and start querying the Gemini Invoice Extractor.

