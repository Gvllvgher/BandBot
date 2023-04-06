FROM python:latest

LABEL org.opencontainers.image.source=https://github.com/Gvllvgher/bandbot

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
