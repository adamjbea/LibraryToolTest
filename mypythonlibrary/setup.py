from setuptools import find_packages, setup

setup(
    name='ThunderBirdTools',
    packages=find_packages(include=['ThunderBirdTools']),
    version='0.1.0',
    description="ThunderBirdTools Test",
    author="Adam Bea",
    install_requires=[
        'glob',
        'pandas',
        'numpy',
        'streamlit',
        'matplotlib',
        'opencv-python',
        'Pillow'
    ],
)