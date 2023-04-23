from setuptools import find_packages, setup
from typing import List 

def get_requirements(file_path: str)->List[str]:
    '''
        This function will return the list of requirements
    '''
    h = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if h in requirements:
            requirements.remove(h)
        
    return requirements 

setup(
    name = 'mlproj',
    version = '0.0',
    author = "Sneh Bhandari",
    author_email="snehbhandari123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)