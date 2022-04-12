FROM  python:3.8
WORKDIR /app/flask_api
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3001
CMD python main.py