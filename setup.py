from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='Ml_Project',
    version='0.0.1',
    author='Sivaganesh Selvam',
    author_email='sivaganesh.selvam.2324@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
