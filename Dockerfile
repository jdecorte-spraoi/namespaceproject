FROM python:3.8.2

RUN pip install git+https://github.com/jdecorte-spraoi/namespaceproject.git@master#subdirectory=src/pkg_core
RUN pip install git+https://github.com/jdecorte-spraoi/namespaceproject.git@master#subdirectory=src/pkg_plugin_a
RUN pip install git+https://github.com/jdecorte-spraoi/namespaceproject.git@master#subdirectory=src/pkg_plugin_b

CMD [ "python", "-c", "from scatpack.core import main; main.run(3, 4)" ]
