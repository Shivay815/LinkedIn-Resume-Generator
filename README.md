# LinkedIn-Resume-Generator
# Resume API

This is a REST API built with Flask that takes an OpenAI key and a PDF file as input and generates a resume based on the content of the PDF. The API is designed to be deployed on Vercel.

## Project Structure
/resume_api
  |-- /core
    |-- init.py
    |-- resume_generator.py
  |-- /config
    |-- config.py
  |-- /routes
    |-- api_routes.py
  |-- app.py
  |-- requirements.txt
  |-- vercel.json

## Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/resume_api.git
    cd resume_api
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

- **`app.py`**: Entry point for the Flask application.
- **`core/resume_generator.py`**: Contains the logic to extract text from the PDF and generate a resume using OpenAI's API.
- **`routes/api_routes.py`**: Defines the API routes.
- **`config/config.py`**: Configuration settings.
- **`vercel.json`**: Configuration for deploying the app on Vercel.

## Running Locally

1. **Run the Application**

    ```bash
    python app.py
    ```

    The API will be available at `http://127.0.0.1:5000`.

2. **Test the API**

    - **Generate Resume**

      Use the following `cURL` command to test the `/generate_resume` endpoint:

      ```bash
      curl -X POST http://127.0.0.1:5000/api/generate_resume \
        -F "open_ai_key=YOUR_OPENAI_KEY" \
        -F "pdf_file=@path/to/your/file.pdf"
      ```

      Alternatively, you can use Postman to make a POST request with form-data containing `open_ai_key` and `pdf_file`.

## Deployment

To deploy this API on Vercel:

1. **Install Vercel CLI**

    ```bash
    npm install -g vercel
    ```

2. **Deploy**

    ```bash
    vercel
    ```

    Follow the prompts to complete the deployment.

## Dependencies

- Flask
- flask_cors
- requests
- openai
- PyPDF2
