from __future__ import absolute_import, unicode_literals

import warnings
from unittest import TestCase

from immutable import Immutable, ImmutableFactory

warnings.filterwarnings("ignore")


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


class TestImmutable(TestCase):

    def setUp(self):
        self.unordered_immutable = Immutable(black='black', white='white',
                                             red='red', blue='blue')
        self.ordered_immutable = Immutable(
            ('zero', 0), ('one', 1), ('two', 2), ('three', 3)
        )

    def test_create_empty(self):

        # should be able to instantiate without args.

        obj = Immutable()
        self.assertEqual(obj.__class__.__name__, 'Immutable')

    def test_instantiation(self):

        # you can create via a tuple, an unpacked dict, or both.

        tup_instantiation = Immutable(('blah', 10))
        self.assertEqual(tup_instantiation.blah, 10)

        dict_instantiation = Immutable(**{'okie': 'dokie'})
        self.assertEqual(dict_instantiation.okie, 'dokie')

        both_instantiation = Immutable(('blah', 10), **{'okie': 'dokie'})
        self.assertEqual(list(both_instantiation.items()),
                         [('blah', 10), ('okie', 'dokie')])

    def test_keys(self):

        # the keys() api should be preserved

        self.assertEqual(set(self.unordered_immutable.keys()),
                         {'black', 'white', 'red', 'blue'})

        # if given as a tuple, they should keep the given order
        self.assertEqual(list(self.ordered_immutable.keys()),
                         ['zero', 'one', 'two', 'three'])

    def test_values(self):

        # the values() api should be preserved

        self.assertEqual(set(self.unordered_immutable.values()),
                         {'black', 'white', 'red', 'blue'})

        # if given as a tuple, they should keep the given order
        self.assertEqual(list(self.ordered_immutable.values()), [0, 1, 2, 3])

    def test_items(self):

        # the items() api should be preserved

        self.assertEqual(set(self.unordered_immutable.items()),
                         {('black', 'black'), ('white', 'white'),
                          ('red', 'red'), ('blue', 'blue')})

        # if given as a tuple, they should keep the given order
        self.assertEqual(list(self.ordered_immutable.items()),
                         [('zero', 0), ('one', 1), ('two', 2), ('three', 3)])

    def test_index(self):

        # the index() api should be preserved (it acts on the values).

        self.assertEqual(self.ordered_immutable.index(0), 0)
        self.assertEqual(self.ordered_immutable.index(1), 1)

    def test_count(self):

        # the count() api should be preserved (it acts on the values).

        obj = Immutable(**{k: 'blah' for k in 'abcdefg'})
        self.assertEqual(obj.count('blah'), 7)
        self.assertEqual(obj.count('nope'), 0)

    def test_containment(self):

        # we don't support containment because it's ambiguous

        regex = 'Containment not implemented.'
        with self.assertRaisesRegexp(Immutable.ImmutableError, regex):
            'white' in self.unordered_immutable

    def test_reversal(self):

        # we don't support reversal because it's ambiguous

        regex = 'Reversal not implemented.'
        with self.assertRaisesRegexp(Immutable.ImmutableError, regex):
            reversed(self.unordered_immutable)

    def test_equality(self):

        # equality works by hashing two immutable instances

        self.assertFalse(self.ordered_immutable == self.unordered_immutable)

        args = [('a', 1), ('b', 2)]
        imm_0 = Immutable(*args)
        imm_1 = Immutable(*args)
        self.assertFalse(imm_0 == args)
        self.assertTrue(imm_0 == imm_1)


    def test_non_equality_comparisons(self):

        # equality works by hashing two immutable instances

        self.assertTrue(self.ordered_immutable != self.unordered_immutable)

        args = [('a', 1), ('b', 2)]
        imm_0 = Immutable(*args)
        imm_1 = Immutable(*args)
        self.assertTrue(imm_0 != args)
        self.assertFalse(imm_0 != imm_1)

    def test_attribute_access(self):

        # You should be able to access via both getitem or getattr with indices
        # or keys.

        self.assertEqual(self.ordered_immutable.zero, 0)
        self.assertEqual(self.ordered_immutable['zero'], 0)
        self.assertEqual(self.ordered_immutable[0], 0)
        self.assertEqual(self.ordered_immutable[-4], 0)

    def test_change_attribute(self):

        # you can't!

        # should not be able to change with key
        with self.assertRaisesRegexp(Immutable.ImmutableError,
                                     'Cannot set items on Immutable.'):
            self.ordered_immutable['zero'] = 10

        # should not be able to change with index
        with self.assertRaisesRegexp(Immutable.ImmutableError,
                                     'Cannot set items on Immutable.'):
            self.ordered_immutable[0] = 10

        # should not be able to change with negative index
        with self.assertRaisesRegexp(Immutable.ImmutableError,
                                     'Cannot set items on Immutable.'):
            self.ordered_immutable[-4] = 10

        # should not be able to change with '.' access
        with self.assertRaisesRegexp(Immutable.ImmutableError,
                                     'Cannot set attributes on Immutable.'):
            self.ordered_immutable.zero = 10

        # finally, show how we *can* change it! NEVER DO THIS!
        self.ordered_immutable._ordered_dict['zero'] = 10
        self.assertEqual(self.ordered_immutable['zero'], 10)

    def test___dir__(self):

        # __dir__ should return a list of the keys.

        dir_list = self.ordered_immutable.__dir__()
        expected_dir_list = ['zero', 'one', 'two', 'three']
        self.assertEqual(dir_list, expected_dir_list)
