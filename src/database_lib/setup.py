from setuptools import setup, find_packages


setup(
    name='database_lib',
    version='0.0.4',
    description='KCSpotifyAnalyzer\'s SQLAlchemy database',
    url='https://github.com/Zancmok/KCSpotifyAnalyzer',
    author='Zancmok',
    packages=find_packages(),
    install_requires=[
        'pymysql',
        'sqlalchemy'
    ]
)
