from setuptools import setup

setup(
    name='nanodb_driver',
    version='0.1',
    author='Pierre-Marie Dartus',
    author_email='dartus.pierremarie@gmail.com',
    packages=['nanodb_driver'],
    license='LICENSE.txt',
    description='NanoDB driver for python',
    long_description=open('README.rst').read(),
    install_requires=[
        "pyzmq>=14.4.1"
    ],
)
