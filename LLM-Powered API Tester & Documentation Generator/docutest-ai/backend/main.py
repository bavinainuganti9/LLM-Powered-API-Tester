from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from parser import parse_openapi_spec
from gpt_generator import generate_tests

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/upload/")
async def upload_openapi(file: UploadFile = File(...)):
    content = await file.read()
    endpoints = parse_openapi_spec(content)
    tests = generate_tests(endpoints)
    return {"endpoints": endpoints, "test_code": tests}
