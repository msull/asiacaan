from setuptools import setup

__VERSION__ = '0.0.1'

setup(
    name='acaan',
    packages=['acaan'],
    py_modules=['acaan'],
    description='Asi ACAAN trainer',
    author='Sully Sullenberger',
    author_email='sully@sadburger.com',
    url='https://github.com/msull/asiacaan',
    keywords=['acaan'],
    classifiers=[],
    version=__VERSION__,
    install_requires=[
    ],
    entry_points="""
        [console_scripts]
        acaan=acaan.main:main
    """,
)
