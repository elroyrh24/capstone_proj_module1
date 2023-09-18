from setuptools import setup, find_packages

setup(
    name='X Company DataApp',
    version='v.0.1.0',
    author='Elroy Renzo Haryadi',
    author_email='elroyharyadi@gmail.com',
    description='Database application for managing employees',
    packages=find_packages(where='src'),
    python_requires='>=3.9, <4',
    url='https://github.com/elroyrh24/capstone_proj_module1.git',
)