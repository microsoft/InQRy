import sys

try:
    from setuptools import setup
except ModuleNotFoundError:
    from distutils.core import setup

APP = ['InQRy.py']
OPTIONS = {}

if sys.platform == 'darwin':
    extra_options = dict(
            setup_requires=['py2app'],
            install_requires=['PyYAML'],
    )
elif sys.platform == 'win32':
    extra_options = dict(
            install_requires=['wmi', 'pypiwin32'],
    )

setup(app=APP,
      author=['Apex Lab'],
      author_email='apxlab@microsoft.com',
      description='A cross-platform utility used to generate a QR code containing hardware specs',
      license='MIT',
      long_description=open('README.md').read(),
      name='InQRy',
      options={'py2app': OPTIONS},
      packages=['inqry', "inqry.system_specs", "tests"],
      install_requires=['qrcode', 'Pillow'],
      tests_require=['pytest'],
      url='https://github.com/Microsoft/InQRy',
      version='1.2.1',
      classifiers=[
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6']
      )
