from setuptools import setup, find_packages


setup( 
        name='Neil', 
        description='A utility program to generate boilerplate code/text from templates.',
        version='1.0.3', 
        license='MIT',
        author='Juho Salli',
        author_email='juho@jsalli.com',
        url='https://github.com/juhosa/neil',
        packages=find_packages(), 
        include_package_data=True,
        install_requires=[ 'Click', 'Jinja2' ], 
        entry_points='''
            [console_scripts]         
            neil=neil.main:cli
        ''', 
        )
