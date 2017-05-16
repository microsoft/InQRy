import sys

from setuptools import setup

APP = ['InQRy.py']
DATA_FILES = []
OPTIONS = {}

if sys.platform == 'darwin':
    extra_options = dict(
            setup_requires=['py2app'],
            install_requires=['qrcode', 'PyYAML', 'Pillow'],
    )
elif sys.platform == 'win32':
    extra_options = dict(
            install_requires=['wmi', 'pypiwin32', 'qrcode', 'Pillow'],
    )

setup(app=APP,
      author=['Apex Lab'],
      author_email='apxlab@microsoft.com',
      data_files=DATA_FILES,
      description='Gets machine specs and generates a QR code containing them',
      license='MIT',
      long_description=open('README.md').read(),
      name='InQRy',
      options={'py2app': OPTIONS},
      packages=['inqry', "inqry.system_specs"],
      tests_require=['pytest'],
      url="https://office.visualstudio.com/APEX/Lab-Projects/_git/InQRy",
      version='1.2')
