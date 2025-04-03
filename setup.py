from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="printlogr",
    version="0.3.1",
    author="Inder Rana",
    description="A Python library for logging print statements with timestamps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inderrana/printlogr",
    project_urls={
        "Bug Tracker": "https://github.com/inderrana/printlogr/issues",
        "Documentation": "https://github.com/inderrana/printlogr#readme",
    },
    packages=find_packages(),
    package_data={
        "printlogr": ["py.typed"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
    ],
    keywords="logging, print, timestamp, pdf, csv, txt",
    python_requires=">=3.7",
    install_requires=[
        "reportlab>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=4.0.0",
            "twine>=4.0.0",
            "build>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "printlogr=printlogr.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 