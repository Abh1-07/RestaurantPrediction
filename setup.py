from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This Function returns the list of all the required packages in requirements.txt
    :param file_path: The File_path for the requirements.txt
    :return: The list of Packages to be used
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    # whenever this is executed, \n from file will also be recorded.
    # using list comprehension to replace \n with blanks
    requirement = [req.replace('\n', '') for req in requirements]
    if HYPHEN_E_DOT in requirement:
        requirement.remove(HYPHEN_E_DOT)
    return requirement


setup(
    name='RestaurantRatingPredict',
    version='0.0.1',
    author='Abhishek Tiwari',
    author_email='vedanshtiwari.07@gmail.com',
    packages=find_packages(),  # To find the packages, whichever folder has __init__.py, consider as package
    install_requires=get_requirements('requirements.txt')  # from this will install all the required packages
)
