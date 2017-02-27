try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='InQRy',
      version='0.0.3',
      license='MIT',
      description='Gets machine specs and generates a QR code containing them',
      author='Eric Hanko',
      author_email='v-erhank@microsoft.com',
      packages=['inqry'],
      long_description=open('README.md').read(),
      install_requires=[
          "qrcode",
          "pyyaml",
          "pytest-runner",
          "pytest",
          "Pillow",
          "wmi"],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )
