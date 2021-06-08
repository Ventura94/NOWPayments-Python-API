import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nowpayments",
    version="0.0.7",
    author="Arian Ventura Rodríguez",
    author_email="arianventura94@gmail.com",
    description="NOWPayments python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ventura94/NOWPayments-Python-API",
    project_urls={
        "Bug Tracker": "https://github.com/Ventura94/NOWPayments-Python-API/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)