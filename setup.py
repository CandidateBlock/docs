from setuptools import setup

# Install Instrucitions
# $ python setup.py install
# $ pip install -e .

my_package = 'docs'

setup(
    name=my_package,
    version='1.0.0',
    description='A useful module',
    url='http://github.com/canddidateblock/candidateblock_bitcoin_library',
    author='CandidateBlock',
    author_email='candidateblock@canddidateblock.com',
    license='MIT',
    # packages=find_packages(where="candidateblock_bitcoin_library"),
    # package_dir={"": "candidateblock_bitcoin_library"},
    packages=[my_package],  # same as name
    # install_requires=[
    #     "ecdsa"
    # ],
    # scripts=['scripts/main'],
)
