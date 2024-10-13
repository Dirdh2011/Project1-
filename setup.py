from setuptools import find_packages,setup
from typing import List
hypen_e='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    return the list of libraies from file path

    '''
    with open(file_path)as fileobj:
        libs=fileobj.readlines()
        libs=[name.replace("\n","")for name in libs]
        if hypen_e in libs:
            libs.remove(hypen_e)
        return libs

setup(
    name="PROJECT1",
    version='0.0.1',
    author='Dirdh2011',
    author_email='pdirdh2011@gmail.com',
    packages=find_packages(),
    install_requires= get_requirments('requirements.txt'))