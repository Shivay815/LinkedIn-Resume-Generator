import fitz  # PyMuPDF for reading the PDF
import openai
import logging
import time

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_pdf(pdf_path):
    """Extracts text from the PDF file."""
    text = ""
    logging.info(f"Opening PDF file: {pdf_path}")
    try:
        with fitz.open(pdf_path) as doc:
            logging.info(f"PDF file contains {doc.page_count} pages.")
            for page_num in range(doc.page_count):
                logging.debug(f"Extracting text from page {page_num + 1}")
                page = doc.load_page(page_num)
                text += page.get_text("text")
        logging.info("Text extraction from PDF completed.")
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {str(e)}")
        raise e  # Re-raise the exception after logging it
    return text

def generate_resume(open_ai_key, pdf_path):
    """Generate the resume using OpenAI key and PDF input."""
    logging.info("Starting resume generation process.")

    # Step 1: Extract text from the LinkedIn PDF
    try:
        logging.debug("Extracting text from the provided PDF.")
        extracted_text = extract_text_from_pdf(pdf_path)
        logging.info("Text extraction successful.")
    except Exception as e:
        logging.error(f"Failed to extract text from PDF: {str(e)}")
        return {
            "error": str(e),
            "message": "Failed to extract text from the provided PDF file."
        }

    # Step 2: Set up OpenAI API credentials
    openai.api_key = open_ai_key
    logging.debug("OpenAI API key set successfully.")

    # Step 3: Generate a resume using the extracted text
    retries = 3
    while retries > 0:
        try:
            logging.info("Sending request to OpenAI to generate resume.")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Updated model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Generate a professional resume from the following LinkedIn data:\n\n{extracted_text}"}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            
            logging.info("OpenAI response received successfully.")
            
            # Step 4: Extract the generated resume from the response
            resume = response['choices'][0]['message']['content'].strip()
            logging.info("Resume generated successfully.")
            
            return {
                "generated_resume": resume,
                "message": "Resume generated successfully!"
            }

        except openai.error.RateLimitError as e:
            logging.warning(f"Rate limit exceeded: {str(e)}. Retrying in 30 seconds.")
            time.sleep(30)  # Retry after a delay
            retries -= 1
        
        except openai.error.OpenAIError as e:
            logging.error(f"Error generating resume using OpenAI: {str(e)}")
            return {
                "error": str(e),
                "message": "Failed to generate resume from the provided LinkedIn data."
            }
    
    return {
        "error": "Quota exceeded and retry attempts failed.",
        "message": "Failed to generate resume after multiple attempts due to quota issues."
    }
