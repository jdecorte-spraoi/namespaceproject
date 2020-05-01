FROM python:3.8.2

WORKDIR /app

COPY . /app/.

RUN pip install /app/.

CMD [ "python", "-c", "from spcore import main; main.run(3, 4)" ]
