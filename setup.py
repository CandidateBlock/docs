from setuptools import setup

my_package = 'docs'

setup(
    name=my_package,
    version='1.0.0',
    description='Public Documents for Bitcoin Related Information',
    url='https://github.com/CandidateBlock/docs',
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
