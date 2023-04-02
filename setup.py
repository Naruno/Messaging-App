from setuptools import setup


setup(name='messaging_app',
version='0.1.5',
description="""Messaging App""",
long_description_content_type="text/markdown",
long_description="".join(open("README.md", encoding="utf-8").readlines()),
url='https://github.com/Naruno/Messaging-App',
author="Naruno Developers",
author_email='onur.atakan.ulusoy@naruno.org',
license='MIT',
packages=["messaging_app"],
include_package_data=True,
install_requires=[
    "naruno_remote_app",
],
entry_points = {
    'console_scripts': ['messagingapp=messaging_app.messaging_app:main'],
},
python_requires=">= 3",
zip_safe=False)
