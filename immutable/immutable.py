from __future__ import absolute_import, unicode_literals

from collections import OrderedDict


class Immutable(object):
    """
    Immutable object which adheres to the Mapping and the Sequence protocols.

    * Attributes are kept in `self._ordered_dict`. NEVER MUTATE THIS!
    * Instantiate with kwargs or args. Instantiating with args preserves order.
    * Mapping methods get(), items(), keys(), and values() are also included.
    * Sequence methods index() and count() are also included.

    """

    class ImmutableError(Exception):
        pass

    def __init__(self, *args, **kwargs):
        """
        Instantiate an Immutable instance.

        >>> # tuple instantiation --> Note that this method preserves order!
        >>> obj = Immutable((('val_0', 0), ('val_1', 1)))
        >>> # key=value pairs
        >>> obj = Immutable(val_0=0, val_1=1)
        >>> # same as above, but by upacking a dict
        >>> attribute_dict = {'val_0': 0, 'val_1': 1}
        >>> obj = Immutable(**attribute_dict)
        >>> # access via '.' or '[]'
        >>> obj.val_0
        >>> obj['val_0']

        :param args: (<attr>, <val>,) pairs to add *in order*
        :param kwargs: Allows you to unpack a dict to create this.

        """
        reserved_keys = ('get', 'keys', 'values', 'items', 'count', 'index',
                         '_ordered_dict', '_tuple')
        ordered_dict = OrderedDict()
        for key, val in args:
            if key in kwargs:
                raise self.ImmutableError('Key in args duplicated in kwargs.')
            ordered_dict[key] = val
        ordered_dict.update(kwargs)
        for key, val in ordered_dict.items():
            try:
                hash(key)
                hash(val)
            except TypeError:
                raise self.ImmutableError('Keys and vals must be hashable.')
            if isinstance(key, int):
                raise self.ImmutableError('Keys cannot be integers.')
            if key in reserved_keys:
                raise self.ImmutableError('Keys cannot be any of these: {}.'
                                          .format(reserved_keys))
        self.__dict__['_ordered_dict'] = ordered_dict
        self.__dict__['_tuple'] = tuple(ordered_dict.values())

    def __contains__(self, item):
        raise self.ImmutableError('Containment not implemented. Try with '
                                  'keys(), values(), or items().')

    def __reversed__(self):
        raise self.ImmutableError('Reversal not implemented. Try with '
                                  'keys(), values(), or items().')

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__dict__['_tuple'][key]
        else:
            return self.__dict__['_ordered_dict'][key]

    def __setitem__(self, key, value):
        raise self.ImmutableError('Cannot set items on Immutable.')

    def __getattr__(self, key):
        if key == 'items':
            return self.__dict__['_ordered_dict'].items
        elif key == 'keys':
            return self.__dict__['_ordered_dict'].keys
        elif key == 'values':
            return self.__dict__['_ordered_dict'].values
        elif key == 'index':
            return self.__dict__['_tuple'].index
        elif key == 'count':
            return self.__dict__['_tuple'].count
        else:
            return self.__getitem__(key)

    def __setattr__(self, key, value):
        raise self.ImmutableError('Cannot set attributes on Immutable.')

    def __cmp__(self, other):
        raise self.ImmutableError('Only equality comparisons implemented.')

    def __eq__(self, other):
        if not isinstance(other, Immutable):
            return False
        return hash(self) == hash(other)

    def __ne__(self, other):
        if not isinstance(other, Immutable):
            return True
        return hash(self) != hash(other)

    def __len__(self):
        return len(self.__dict__['_tuple'])

    def __iter__(self):
        raise self.ImmutableError('Iteration not implemented. Try with '
                                  'keys(), values(), or items().')

    def __hash__(self):
        return hash(tuple(self._ordered_dict.items()))

    def __str__(self):
        return bytes('{}'.format(self.__repr__()))

    def __unicode__(self):
        return '{}'.format(self.__repr__())

    def __repr__(self):
        keys_repr = ', '.join('{}={}'.format(key, repr(val))
                              for key, val in self.items())
        return 'Immutable({})'.format(keys_repr)

    def __dir__(self):
        return list(self.keys())
