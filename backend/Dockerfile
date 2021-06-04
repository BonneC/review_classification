FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./ .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_lg