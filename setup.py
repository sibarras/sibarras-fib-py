from setuptools import find_packages, setup

setup(
    name="sibarras-fib-py",
    version="0.0.1",
    author="Samuel Ibarra",
    author_email="ing.samuelibarra@gmail.com",
    description="Calculates a fibonacci number",
    long_description="A basic library that \
        calculates fibonacci numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/sibarras/sibarras-fib-py.git",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operationg System :: OS Independent",
    ],
    python_requires='>=3',
    test_require=['pytest'],
)