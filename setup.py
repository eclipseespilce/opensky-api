import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opensky",
    version="0.0.2",
    author="Alexander Kireev",
    author_email="eclipseespilce@mail.ru",
    description="Airplanes monitoring by OpenSky api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eclipseespilce/opensky-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
