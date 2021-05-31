import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loghandler",
    version="0.0.2",
    author="Hunter Allen",
    author_email="allenhm@gmail.com",
    description="Logging setup with stream and file handlers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hmallen/loghandler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
