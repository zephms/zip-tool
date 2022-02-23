

from pkg_resources import EntryPoint
from setuptools import setup

setup(
    name='zephms_tools',
    version='0.0.1',
    author='xlzd',
    author_email='zephms@163.com',
    url='https://www.acbs.top',
    description=u'',
    packages=['zip'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'zip=zip.zipper:bszip',
            'unzip=zip.zipper:bsunzip',
        ]
    }
)