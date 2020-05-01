FROM python:3.8.2

WORKDIR /app

COPY spcore /app/spcore
COPY sp_plugin_b /app/sp_plugin_b
COPY ./deployment/core_b/pyproject.toml /app/.

RUN pip install .

CMD [ "python", "-c", "from spcore import main; main.run(3, 4)" ]
