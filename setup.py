try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='PyBar',
      version='0.0.2',
      license='MIT',
      description='Generates QRCodes for a physical inventory',
      author='Eric Hanko',
      author_email='v-erhank@microsoft.com',
      packages=['pybar'],
      long_description=open('README.md').read(),
      install_requires=[
          "qrcode",
          "pyyaml",
          "pytest-runner",
          "pytest"],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )
