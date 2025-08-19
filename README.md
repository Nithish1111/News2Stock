Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
pip install fastapi uvicorn cohere python-dotenv requests
uvicorn api_server:app --reload
Open index.html
