from setuptools import setup

setup(
    name = 'seam_social_labs',
    version = '0.1.0',
    packages = ['seam_social_labs'],
    entry_points = {
        'console_scripts': [
            'seam_social_labs = seam_social_labs.__main__:main'
        ]
    })
