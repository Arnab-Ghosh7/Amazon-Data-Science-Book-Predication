import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Amazon-Data-Science-Book"
AUTHOR_USER_NAME = "Arnab-Ghosh7"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "arnabghosh010203@gmail.com"

setuptools.setup(
    name=SRC_REPO,                     # package name
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text classification package using TF-IDF and Logistic Regression",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},           # VERY IMPORTANT
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
