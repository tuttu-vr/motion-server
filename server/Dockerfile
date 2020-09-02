FROM python:3.8.5-alpine3.12

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app.py ./

CMD [ "python", "app.py" ]
