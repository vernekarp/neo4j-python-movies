"""A setuptools based setup module."""
from setuptools import setup, find_packages
from setuptools.command.install import install


VERSION = '1.0.0'
DEPENDENCIES = ['Flask>=0.8', 'neo4j-driver>=1.6.1', 'neo4j==1.7.2']


class PostInstallSetup(install):
    """Post Installation setup to create neo4j movie nodes."""
    def run(self):
        install.run(self)
        from create_neo4j_db import main as post_install
        post_install()


setup(
    name='neo4jmovieapi',
    version=VERSION,
    packages=find_packages(),
    scripts=['movies.py'],
    data_files=[('etc', ['etc/neo4jnode.secrets'])],
    author='Prashanth Vernekar',
    author_email='Prashanth.Vernekar@gmail.com',
    description='Simple Python Flask API interacting with Neo4j DB nodes.',
    setup_requires=['wheel', 'neo4j==1.7.2'],
    install_requires=DEPENDENCIES,
    python_requires='~=3.5',
    cmdclass={
        'install': PostInstallSetup
    },
    entry_points={
        'console_scripts': [
            'neo4jmovies = movies:main',
        ]
    },
)
