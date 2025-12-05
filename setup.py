from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="arbitbot",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="加密貨幣跨交易所套利機器人",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/arbitbot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
    install_requires=[
        "ccxt>=2.0",
        "python-telegram-bot>=13.0",
        "pyyaml>=5.0",
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "arbitbot=main:main",
        ],
    },
)
