from setuptools import setup, find_packages

setup(
    name='my_password_manager',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography'
    ],
    entry_points={
        'console_scripts': [
            'my_password_manager = my_password_manager.main:main'
        ]
    }
)
