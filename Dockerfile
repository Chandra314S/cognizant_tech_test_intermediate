FROM python:latest
COPY . .
RUN pip install flask
CMD [ "python", "/app.py"]
#  CMD [ "python", "/Unittests.py"]
EXPOSE 5000