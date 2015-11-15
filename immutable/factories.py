"""
Factories for creating `Immutable` objects.

"""
from __future__ import absolute_import, unicode_literals

import warnings
from collections import namedtuple


def warning_on_one_line(message, category, filename, lineno,
                        file=None, line=None):
    return '{}:{}: {}:\n\n{}\n\n'.format(filename, lineno, category.__name__,
                                         message)
warnings.formatwarning = warning_on_one_line


class ImmutableFactory(object):
    """
    Factory to create namedtuple objects, which are immutable.

    """
    @staticmethod
    def create(attributes=(), keys=True, values=True, items=True, **kwargs):
        """
        Thin wrapper around standard namedtuple to make creation simpler.

        You can dot-access the attributes, but you can't change them!

        You can instantiate with kwargs (like unpacking a dict, or key=value
        pairs). Additionally, you can instantiate as a normal namedtuple with
        a tuple

        >>> factory = ImmutableFactory()
        >>> # tuple instantiation --> Note that this method preserves order!
        >>> obj = factory.create((('val_0', 0), ('val_1', 1)))
        >>> # key=value pairs
        >>> obj = factory.create(val_0=0, val_1=1)
        >>> # same as above, but by upacking a dict
        >>> attribute_dict = {'val_0': 0, 'val_1': 1}
        >>> obj = factory.create(**attribute_dict)
        >>> # create is a static method, so you don't *need* an instance
        >>> obj = ImmutableFactory.create()

        :param (bool) values: Include .values attribute listing arg vals?
        :param (bool) keys: Include .keys attribute listing arg keys?
        :param (bool) items: Include .items attribute listing name-val pairs?
        :param (tuple) attributes: (<attr>, <val>,) pairs to add *in order*
        :param (dict) kwargs: Allows you to unpack a dict to create this.

        :return: (namedtuple) An instance of type Immutable.

        """
        warnings.warn('Deprecated: Use `from immutable import Immutable`. '
                      'Backwards incompatible changes exist. See CHANGELOG.md')
        attributes += tuple((k, v) for k, v in kwargs.items())
        keys_tup = tuple(e[0] for e in attributes)
        values_tup = tuple(e[1] for e in attributes)
        items_tup = tuple(tuple(e) for e in attributes)
        field_names, field_values = keys_tup, values_tup

        if set(field_names).intersection({'keys', 'values', 'items'}):
            raise ValueError("'keys', 'values', and 'items' are reserved. "
                             "They cannot be included as attribute names.")

        if keys:
            field_names += ('keys',)
            field_values += (keys_tup,)

        if values:
            field_names += ('values',)
            field_values += (values_tup,)

        if items:
            field_names += ('items',)
            field_values += (items_tup,)

        fields_dict = {k: v for k, v in zip(field_names, field_values)}
        return namedtuple('Immutable', field_names)(**fields_dict)
