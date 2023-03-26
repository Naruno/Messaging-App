from setuptools import setup


setup(name='messaging_app',
version='0.1.1',
description="""Messaging App""",
long_description_content_type="text/markdown",
long_description="".join(open("README.md", encoding="utf-8").readlines()),
url='https://github.com/Naruno/Messaging-App',
author="Naruno Developers",
author_email='onur.atakan.ulusoy@naruno.org',
license='MIT',
packages=["messaging_app"],
include_package_data=True,
entry_points = {
    'console_scripts': ['messagingapp=messaging_app.messaging_app:main'],
},
python_requires=">= 3",
zip_safe=False)