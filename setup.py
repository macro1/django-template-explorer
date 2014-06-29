import os
from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(
    name='django-template-explorer',
    version='0.0.1',
    install_requires=[
        "Django>=1.4,<1.8",
    ],
    packages=["template_explorer", "template_explorer.management", "template_explorer.management.commands"],
    include_package_data=True,
    test_suite='runtests.runtests',
    license='MIT License',
    description="Analyze a Django project's template hierarchy.",
    long_description=README,
    url='http://macro1.github.io/django-template-explorer/',
    author='macro1',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
