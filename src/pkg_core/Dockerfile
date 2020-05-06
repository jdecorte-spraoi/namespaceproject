FROM python:3.8.2

RUN pip install git+https://jdecorte-spraoi:6tbH4^AXuHuz7qKe@github.com/jdecorte-spraoi/namespaceproject.git@master#subdirectory=src/pkg_core

CMD [ "python", "-c", "from scatpack.core import main; main.run(3, 4)" ]
