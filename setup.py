from setuptools import setup, find_packages


with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="mkdocs-generator",
    version="0.1.0",
    description="Generate mkdocs documentation from README.md files",
    long_description="Generate mkdocs documentation from README.md files but searching for README.md files in subdirectories and copying them to .mkdocs/docs",
    author="Alexey Gumirov",
    author_email="agumirov@amazon.de",
    license="MIT",
    packages=find_packages(include=["mkdocs_generator"]),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "mkdocs-generator=mkdocs_generator.__main__:main",
        ]
    },
    python_requires=">=3.8",
)
