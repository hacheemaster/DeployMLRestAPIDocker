FROM python:3.7
 
WORKDIR /app/
 
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt
 
COPY app.py __init__.py /app/
COPY model.joblib /app/
 
EXPOSE 5000

ENTRYPOINT python ./app.py
