from setuptools import setup, find_packages

setup(
    name='Blue Channel CMS',
    version='0.1',
    description='A content management system developed in Django, jQuery and 960.',
    long_description='',
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Dave Merwin',
    author_email='dave@davemerwin.com',
    url='http://github.com/davemerwin/blue-channel/tree/master',
    download_url='http://github.com/davemerwin/blue-channel/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
