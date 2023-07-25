from setuptools import setup, find_packages

setup(
    name='mcqgen',
    version='0.1.0',
    packages=find_packages(),
    author='Abhilash Mhaisne',
    description='Generate Multiple Choice Questions, Choices and Correct Answer in JSON Format',
    install_requires=['openai']
)
