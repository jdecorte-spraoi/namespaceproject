FROM python:3.7-slim
#FROM python:3.8.2

WORKDIR /app

COPY src/pkg_core /app

RUN pip install .

CMD [ "python", "-c", "from scatpack.core import main; main.run(3, 4)" ]
