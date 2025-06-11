# LLM Powered API Tester

## Overview / Description
DocuTest AI is a full-stack application that parses OpenAPI (Swagger) specs or Postman collections, uses GPT-4 to automatically generate API test cases and readable documentation, and provides a web UI to interactively test endpoints.

## Features
- Upload OpenAPI (Swagger) or Postman v2 JSON files  
- Use GPT-4 to generate Python test stubs with sample requests and asserts  
- Generate clear natural language documentation for endpoints  
- Run test calls interactively via the web UI  
- Download generated test code or copy documentation snippets  

## Architecture
Backend: Python FastAPI app with endpoints for file upload, parsing, and GPT-based test generation  
Parsing: Custom JSON parser for OpenAPI and Postman formats  
LLM: OpenAI GPT-4 API for generating test code and documentation  
Frontend: React + Tailwind CSS + Monaco Editor for file upload, viewing, and testing  
Storage: Temporary in-memory or filesystem storage for uploaded specs and generated content  

## Tech Stack
Frontend: React, Tailwind CSS, Axios, Monaco Editor  
Backend: Python, FastAPI, OpenAI API  
Parsing: JSON parsing for OpenAPI and Postman collections  
