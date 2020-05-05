Examples
--------
::

    docker build -f src/pkg_core/Dockerfile -t scatpack_core .
    docker run scatpack_core:latest
    docker run -it scatpack_core:latest bash

    docker build -f src/pkg_plugin_a/Dockerfile -t scatpack_plugin_a .
    docker run scatpack_plugin_a:latest
    docker run -it scatpack_plugin_a:latest bash

    docker build -f src/pkg_plugin_b/Dockerfile -t scatpack_plugin_b .
    docker run scatpack_plugin_b:latest
    docker run -it scatpack_plugin_b:latest bash

    docker build -t scatpack .
    docker run scatpack:latest
    docker run -it scatpack:latest bash

