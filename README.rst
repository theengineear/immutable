The Immutable Package
=====================

This package is an *exceedingly* simple wrapper around the builtin
``namedtuple`` from the ``collections`` package.

It allows you to instantiate via a ``tuple`` or via ``kwargs``. It
simplifies the case where you know ahead of time what the values of an
``Immutable`` should be and you just need to instantiate it once.

Install
-------

``pip install immutable``

Details
-------

``namedtuple``
~~~~~~~~~~~~~~

The ``namedtuple`` is a Python ``builtin`` that allows you to
instantiate an object as follows:

.. code:: python

    from collections import namedtuple

    TupleFactory = namedtuple('ATuple', ['using', 'these', 'attrs'])
    ATuple = TupleFactory('first', these='second', attrs='third')
    ATuple  # ATuple(using='first', these='second', attrs='third')

    # dot-access attributes
    ATuple.using  # 'first'
    Atuple.these  # 'second'
    ATuple.attrs  # 'third'

    # index-access attributes
    ATuple[0]  # 'first'
    ATuple[1]  # 'second'
    ATuple[2]  # 'third'
    ATuple[-1]  # 'third'

    # the class name is as specified in creating the original factory
    ATuple.__class__.__name__  # 'ATuple'

``ImmutableFactory``
~~~~~~~~~~~~~~~~~~~~

Replicate ``namedtuple`` functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ImmutableFactory is just a thin wrapper that allows you to do this
in one step:

.. code:: python

    from immutable import ImmutableFactory

    attributes = (('using', 'first'), ('these', 'second'), ('attrs', 'third'))

    # don't worry about the extra kwargs for now :)
    ATuple = ImmutableFactory.create(attributes, keys=False, values=False, items=False)
    ATuple  # Immutable(using='first', these='second', attrs='third')

    # dot-access attributes
    ATuple.using  # 'first'
    Atuple.these  # 'second'
    ATuple.attrs  # 'third'

    # index-access attributes
    ATuple[0]  # 'first'
    ATuple[1]  # 'second'
    ATuple[2]  # 'third'
    ATuple[-1]  # 'third'

    # the class name is *always* `Immutable` now
    ATuple.__class__.__name__  # 'Immutable'

Some extra bells and whistles (don't get too excited)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most of the time, we don't care about the *order*. This allows us to
instantiate in a *much* cleaner style:

.. code:: python

    from immutable import ImmutableFactory

    ATuple = ImmutableFactory.create(using='first', these='second', attrs='third',
                                     keys=False, values=False, items=False)

    # note that there's no predictable order here
    ATuple  # Immutable(these='second', using='first', attrs='third')

    # dot-access attributes
    ATuple.using  # 'first'
    Atuple.these  # 'second'
    ATuple.attrs  # 'third'

    # doesn't really make sense to index-access attributes now, so don't.

    # the class name is *always* `Immutable` now
    ATuple.__class__.__name__  # 'Immutable'

Additionally, it's helpful to have dict-like ``keys``, ``values``, and
``items``. These

Notes
~~~~~

Note if you use a *mutable* as a value for an attribute of an
``Immutable`` object, you'll be able to change it. If this wasn't the
case, the ``ImmutableFactory`` would need to mutate your input data--not
nice.

.. code:: python

    from immutable import ImmutableFactory

    ATuple = ImmutableFactory.create(mutable=['a', 'list'])
    ATuple.mutable  # ['a', 'list']
    ATuple.mutable.append('can change!')
    ATuple.mutable  # ['a', 'list', 'can change!']

