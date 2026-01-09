FROM python:3.11-slim
LABEL author="NBH-BD"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "nbhxss.py"]

