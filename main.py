import shutil
from markitdown import MarkItDown
from fastapi import FastAPI, UploadFile, HTTPException
from uuid import uuid4
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1')
)
md = MarkItDown(llm_client=client, llm_model="gpt-4o-2024-11-20")
app = FastAPI()

# Define supported file extensions
supported_extensions = ('.txt', '.doc', '.docx', '.pdf', '.mp3', '.pptx', '.jpg', '.jpeg', '.png', 
                      '.xlsx', '.xls', '.csv', '.json')

@app.post("/convert")
async def convert_markdown(file: UploadFile):
    if file.filename.endswith('.md'):
        raise HTTPException(status_code=400, detail="Markdown files are not accepted as input - they're already in markdown format")
    
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in supported_extensions:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file format. Allowed formats: {', '.join(supported_extensions)}"
        )
    
    unique_id = uuid4()
    temp_dir = f"./temp/{unique_id}"

    try:
        os.makedirs(temp_dir, exist_ok=True)
        file_path = f"{temp_dir}/{file.filename}"
        
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        
        result = md.convert(file_path)
        content = result.text_content
        
        return {"result": content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv('API_PORT', '8001'))
    uvicorn.run(app, host="0.0.0.0", port=port)