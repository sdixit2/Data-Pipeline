FROM python:3.7
WORKDIR /app
COPY requirements.txt /app
COPY ./ /app
RUN pip install -r requirements.txt
CMD ["python","app.py","dev"]
