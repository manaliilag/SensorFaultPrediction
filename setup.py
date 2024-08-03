# setup.py file use to create package 
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements



# setup is used to show information of auther and versions of package 
# information about package
setup(
    name='SensorFaultDetection',
    version='0.0.1',
    author='Manali_Ilag',
    author_email='manaliilag@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
