bn
==

Lightweight profiling tool to detect performance BottleNecks in Python code.

Hence the name: bn - BottleNeck.  
And you know keys B and N are very comfortable to type quickly in a row.

Usage:

    bn('loop')
    for item in generator:

        bn('rabbit')
        # code of rabbit

        bn('turtle')
        # code of turtle

        bn('loop')

    if bn.total > 1.0:
        logging.info(bn)

Result:

    TOTAL=22.2632, turtle=20.6403, rabbit=1.6209, loop=0.0020
    #
    # This config is default in bn>=0.1.5:
    # Bn(total_key='TOTAL', format='{key}={seconds:.4f}', sep=', ')

    # OR:

    22.2632    TOTAL
    20.6403    turtle
     1.6209    rabbit
     0.0020    loop
    #
    # This config is default in bn<=0.1.4:
    # Bn(total_key='TOTAL', format='{seconds:>10.4f}    {key}', sep='\n')

Install:

    pip install bn

Scope:

    # Global "bn" is useful to profile cross-module without passing "bn" explicitly.
    from bn import bn
    bn.format = custom_format

    # Scoped "Bn" is useful to have multiple independent profilers.
    from bn import Bn
    def action():
        bn = Bn(format=custom_format)

bn version 0.1.5  
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
