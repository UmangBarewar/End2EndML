from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function is going to return list of requirement for a python project
    '''
    HYPHEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='End2EndML',
    version='0.0.1',
    author='Umang',
    author_email='umangbarewar28@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)