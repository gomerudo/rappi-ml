from setuptools import setup, find_packages

setup(
    # For installation
    name='rappiml',
    version='0.0.1',
    install_requires=['numpy', 'scikit-learn', 'flask'],
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    author="Jorge Gomez Robles",
    author_email="j.gomezrb@gmail.com",
    description="Rappi ML Challenge",
)
