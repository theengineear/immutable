# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [0.0.2] - 2015-11-15
### Added
- `Immutable` factory, adheres to Python Sequence and Mapping APIs.
- `Immutable` may be nested while maintaining full immutability.

### Changed
- `ImmutableFactory` is deprecated in favor of new `Immutable` class.

## [0.0.1] - 2015-06-04
### Added
- `ImmutableFactory`, Usage: `Immutable.factory.create(**kwargs)`
- Tests for `ImmutableFactory`
