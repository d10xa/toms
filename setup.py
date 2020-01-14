import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="toms",
    version="0.3.0",
    description="Convert date to milliseconds and back",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/d10xa/toms",
    author="d10xa",
    author_email="d10xa@mail.ru",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    packages=["toms"],
    include_package_data=True,
    install_requires=[
        "python-dateutil>=2.7.1"
    ],
    entry_points={"console_scripts": ["toms=toms.__main__:main"]},
)
