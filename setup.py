from plistlib import Plist

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '1.3'
__author__ = "Microsoft Apex Lab"
__copyright__ = 'Copyright © 2017 Microsoft. All rights reserved.'
__credits__ = ["Eric Hanko", "Jacob Zaval", "Michael Brown", "Andre Shields", "Ryan Dominguez", "Eammon Hanlon"]
__license__ = 'MIT'
__email__ = 'apxlab@microsoft.com'

__description__ = '''
InQRy is a cross-platform application that generates a single QR code containing the machine's hardware specifications.
This application is designed primarily to be used during a physical inventory procedure.

The QR code contains detailed information about the client machine or device, which can then be scanned it quickly add
assets into a Snipe-IT database.
'''

plist = Plist.fromFile('Info.plist')
plist.update(dict(
        CFBundleVersion=__version__,
        CFBundleShortVersionString=__version__,
        CFBundleName='InQRy',
        NSHumanReadableCopyright=__copyright__)
)

setup(
        name='inqry',
        app=['inqry/__main__.py'],
        author=[__author__],
        author_email=__email__,
        description='A cross-platform utility used to generate a QR code containing hardware specs',
        license=__license__,
        long_description=__description__,
        packages=['inqry', 'inqry.system_specs'],
        install_requires=['Pillow',
                          'pytest',
                          'PyYAML',
                          'qrcode',
                          'wmi;platform_system=="Windows"',
                          'pypiwin32;platform_system=="Windows"'],
        tests_require=['pytest'],
        url='https://github.com/Microsoft/InQRy',
        version=__version__,
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Intended Audience :: Information Technology',
            'Intended Audience :: System Administrators',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only'],
        options=dict(
                py2app=dict(
                        plist=plist)))
