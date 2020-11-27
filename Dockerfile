FROM python:3.9
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn && \
    pip install requests
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400" ]