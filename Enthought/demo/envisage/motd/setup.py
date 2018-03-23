from setuptools import setup, find_packages

setup(
    name='Message of the day',
    version='1.0',
    packages=find_packages(),
    description='Message of the day example',
    author='Enthought Inc.',
    author_email='info@enthought.com',
    license='PSF',
    keywords='message of the day, quotes, messages, motd',
    url='http://www.enthought.com',
    entry_points={
        'console_scripts': [
            'motd_simple = motd.__main__:main',
        ],
    }
)
