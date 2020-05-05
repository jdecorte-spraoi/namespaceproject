FROM scatpack_core:latest

WORKDIR /app

COPY src/pkg_plugin_b /app/pkg_plugin_b

RUN pip install /app/pkg_plugin_b/.

CMD [ "python", "-c", "from scatpack.core import main; main.run(3, 4)" ]
