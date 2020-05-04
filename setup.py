from setuptools import setup, find_namespace_packages

setup(
    name='scatpack',

    version='0.1.0',

    description='This is the entire monolithic repository package',
    long_description='Here is a very very very very very long description.',

    author='Jason',
    author_email='jason@spraoi.ai',

    namespace_packages=['scatpack'],
    packages=find_namespace_packages(),
)
