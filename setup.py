from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="shyam",
    author_email="shshyam96@gmail.com",
    description="DVC Machine Learning demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyam1326/DVC_ML_AI-ops",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "pandas",
        "scikit-learn"
    ],

)