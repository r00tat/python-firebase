from setuptools import setup
from firebase import __version__ as lib_version

setup(
    name='zirrus-firebase',
    version=lib_version,
    author='Paul Woelfel',
    author_email='paul.woelfel@zirrus.eu',
    license='private',
    description='Python Firebase client',
    py_modules=[
        "firebase",
        "firebase.client"
    ],
    install_requires=[
        "firebase-token-generator"
    ])
