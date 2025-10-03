from setuptools import find_packages, setup

from typing import List

hypen_dot_e = '-e .'

def get_requirements(file:str)->List[str]:

    requirements = []

    with open(file) as path:

        requirements = path.readlines()
        requirements = [req.replace('\n', " ") for req in requirements]

        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)

    return requirements


setup(

    name = 'mlproject',
    version = '0.0.1',
    author = 'Kushal',
    author_email = 'kushal.y009@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)