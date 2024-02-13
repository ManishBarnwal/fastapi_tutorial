## Install FastAPI package
pip install fastapi

pip install uvicorn  -- will allow us to run our project in the web server


## Basic command to run an app in the server: 
	uvicorn <file_name_without.py>:<app variable name defined in the file> -- reload
	uvicorn myapi:app --reload

## Server
http://127.0.0.1:8000  -- local server
http://127.0.0.1:8000/docs -- allows you to try out the API endpoints and test if the endpoints are working fine.
