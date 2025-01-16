# MarkItDown API Project

This project uses the MarkItDown library to convert various file formats (PPTX, DOCX, PDF, JPG, JPEG, PNG) to Markdown format using OpenAI's GPT-4 model.

## Prerequisites

- Python 3.11 (for local development) or Docker
- OpenAI API key

## Local Development Setup

This project uses Python 3.11. If you're using pyenv, first install Python 3.11:
```bash
pyenv install 3.11.0
```
The `.python-version` file will automatically switch to Python 3.11 in the project directory after installation.

1. Clone this repository:
```bash
git clone <repository-url>
cd markitdown-api
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and set your OpenAI API key and preferred ports
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `API_PORT`: Port for the FastAPI server (default: 8001)
- `STREAMLIT_PORT`: Port for the Streamlit interface (default: 8501)

## Usage

Start the API server:
```bash
python main.py
```

In a new terminal, start the Streamlit interface:
```bash
streamlit run streamlit_app.py --server.port $STREAMLIT_PORT
```

The services will be available at:
- API: http://localhost:8001 (or your configured API_PORT)
- Streamlit Interface: http://localhost:8501 (or your configured STREAMLIT_PORT)
- API Documentation: http://localhost:8001/docs

## Running with Docker

You can also run this application using Docker:

1. Make sure you have Docker and Docker Compose installed on your system.

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and set your OpenAI API key and preferred ports
```

3. Build and start the containers:
```bash
docker-compose up --build
```

This will start both the API server and Streamlit interface. You can access:
- API server at: http://localhost:8001
- Streamlit interface at: http://localhost:8501

To stop the services:
```bash
docker-compose down
```

## Supported File Types

- PowerPoint (.pptx)
- Word Documents (.docx)
- PDF (.pdf)
- Images (.jpg, .jpeg, .png)
- Text files (.txt)
- Excel files (.xlsx, .xls)
- CSV files (.csv)
- JSON files (.json)
- Audio files (.mp3)

## Notes

- Make sure you have sufficient OpenAI API credits
- Large files may take longer to process
- Keep your API key secure and never commit it to version control
- Use different ports if the defaults are already in use
