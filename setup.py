import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hk80",
    version="1.0.1",
    author="Macro Yau",
    author_email="macroyau.development@gmail.com",
    description="Hong Kong 1980 Grid coordinates conversion library in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MacroYau/PyHK80",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        "pyproj==2.1.3",
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
