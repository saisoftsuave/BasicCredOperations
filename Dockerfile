FROM python:latest
WORKDIR /myapp
ADD . .
RUN pip install -r requirement.txt
CMD ["uvicorn", "app.main:app","--reload","--port=8000","--host=0.0.0.0"]