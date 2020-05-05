FROM scatpack_core:latest

WORKDIR /app

COPY src/pkg_plugin_a /app/pkg_plugin_a

RUN pip install /app/pkg_plugin_a/.

CMD [ "python", "-c", "from scatpack.core import main; main.run(3, 4)" ]
