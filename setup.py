import os

from setuptools import setup, find_packages

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="fib-python-payment-sdk",
    version='0.1.10',
    description="SDK for integrating with the FIB payment system, enabling user authentication and payment "
                "transactions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://the-gw.com/",
    author="Gateway ICT",
    author_email="info@the-gw.com",
    license="MIT",
    keywords=["sdk", "fib", "payment", "integration"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "httpx>=0.27.0,<1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0"
        ]
    },
    python_requires=">=3.7, <4",
    include_package_data=True,
)
