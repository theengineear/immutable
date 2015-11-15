from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from immutable.factories import ImmutableFactory


class TestImmutableObjectFactory(TestCase):

    def test_create_empty(self):

        # unlike a namedtuple, you don't even need a name for this (simpler)

        obj = ImmutableFactory.create()
        self.assertEqual(obj.__class__.__name__, 'Immutable')

    def test_instantiation(self):

        # you can create via a tuple, an unpacked dict, or both.

        factory = ImmutableFactory()

        tup_instantiation = factory.create((('blah', 10),))
        self.assertEqual(tup_instantiation.blah, 10)

        dict_instantiation = factory.create(**{'okie': 'dokie'})
        self.assertEqual(dict_instantiation.okie, 'dokie')

        both_instantiation = factory.create((('blah', 10),),
                                            **{'okie': 'dokie'})
        self.assertEqual(both_instantiation.items,
                         (('blah', 10), ('okie', 'dokie')))

    def test_keys(self):

        # the keys attr should be included by default.

        factory = ImmutableFactory()

        attributes = {'one': 1, 'two': 2}
        obj = factory.create(**attributes)
        self.assertEqual(set(obj.keys), {'one', 'two'})

        # if given as a tuple, they should keep the given order
        attributes = (('one', 1), ('two', 2))
        obj = factory.create(attributes)
        self.assertEqual(obj.keys, ('one', 'two'))

        attributes = {'one': 1, 'two': 2}
        obj = factory.create(keys=False, **attributes)
        with self.assertRaises(AttributeError):
            obj.keys

    def test_values(self):

        # the keys attr should be included by default.

        factory = ImmutableFactory()

        attributes = {'one': 1, 'two': 2}
        obj = factory.create(**attributes)
        self.assertEqual(set(obj.values), {1, 2})

        # if given as a tuple, they should keep the given order
        attributes = (('one', 1), ('two', 2))
        obj = factory.create(attributes)
        self.assertEqual(obj.values, (1, 2))

        attributes = {'one': 1, 'two': 2}
        obj = factory.create(values=False, **attributes)
        with self.assertRaises(AttributeError):
            obj.values

    def test_items(self):

        # the keys attr should be included by default.

        factory = ImmutableFactory()

        attributes = {'one': 1, 'two': 2}
        obj = factory.create(**attributes)
        self.assertEqual(set(obj.items), {('one', 1), ('two', 2)})

        # if given as a tuple, they should keep the given order
        attributes = (('one', 1), ('two', 2))
        obj = factory.create(attributes)
        self.assertEqual(obj.items, (('one', 1), ('two', 2)))

        attributes = {'one': 1, 'two': 2}
        obj = factory.create(items=False, **attributes)
        with self.assertRaises(AttributeError):
            obj.items

    def test_attribute_access(self):

        # you should be able to access via the dot-operator, or via index
        # note that keys, values, and items are [-3], [-2], and [-1]

        factory = ImmutableFactory()

        attributes = {'hi': 'there'}
        obj = factory.create(**attributes)
        self.assertEqual(obj.hi, 'there')
        self.assertEqual(obj[0], 'there')
        self.assertEqual(obj[-3], ('hi',))
        self.assertEqual(obj[-2], ('there',))
        self.assertEqual(obj[-1], (('hi', 'there'),))

    def test_change_attribute(self):

        # you can't!

        factory = ImmutableFactory()

        obj = factory.create(**{'change': 'me'})
        with self.assertRaisesRegexp(AttributeError, "can't set attribute"):
            obj.change = 'to this'

        with self.assertRaisesRegexp(TypeError,
                                     "does not support item assignment"):
            obj[0] = 'to this'
