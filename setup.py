from distutils.core import setup

setup(
    name='bn',
    version='0.1.4',
    description='Lightweight profiling tool to detect performance BottleNecks in Python code.',
    long_description='''
Hence the name: bn - BottleNeck.  
And you know keys B and N are very comfortable to type quickly in a row.

Usage::

    bn('iteration')

    for item in generator:

        bn('step 1')
        # code of step 1

        bn('step 2')
        # code of step 2

        bn('iteration')

    bn() # Stop tracking.

    if bn.total > 1.0:
        logging.info(bn)

Result::

    22.2632    TOTAL
    20.6403    step 2
     1.6209    step 1
     0.0020    iteration

Scope::

    pip install bn
    from bn import bn

    # OR:

    from bn import Bn
    def action():
        bn = Bn()

Config::

    bn.total_key = 'TOTAL'
    bn.format = '{seconds:>10.4f}    {key}'

See also: `bn.py:test() <https://github.com/denis-ryzhkov/bn/blob/master/bn.py#L58>`_.

''',
    url='https://github.com/denis-ryzhkov/bn',
    author='Denis Ryzhkov',
    author_email='denisr@denisr.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['bn'],
)
