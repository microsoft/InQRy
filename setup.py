try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='inqry',
    author=['Apex Lab'],
    author_email='apxlab@microsoft.com',
    description='A cross-platform utility used to generate a QR code containing hardware specs',
    license='MIT',
    long_description=open('README.md').read(),
    packages=['inqry', 'inqry.system_specs'],
    install_requires=['Pillow',
                      'pytest',
                      'PyYAML',
                      'wmi;platform_system=="Windows"',
                      'pypiwin32;platform_system=="Windows"'],
    tests_require=['pytest'],
    url='https://github.com/Microsoft/InQRy',
    version='1.2.1',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only']
)
