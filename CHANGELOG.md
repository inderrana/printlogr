# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2024-04-03

### Fixed
- Fixed file saving issue by adding automatic directory creation
- Added proper error handling for file operations
- Improved robustness of file saving operations

## [0.3.0] - 2024-04-03

### Changed
- Completely redesigned logging mechanism to use `plog()` method instead of print interception
- Removed print statement interception for cleaner, more reliable logging
- Updated documentation to reflect new logging approach

### Added
- New `plog()` method that works like print() but with logging capabilities
- Comprehensive API documentation in README
- Added CHANGELOG.md for version tracking

## [0.2.9] - 2024-04-03

### Fixed
- Fixed issue with print statements in Jupyter notebooks appearing in wrong cells
- Improved handling of print context in Jupyter environment

## [0.2.8] and earlier

- Initial implementation with print statement interception
- Basic logging functionality
- Multiple export formats (TXT, CSV, PDF)
- Context manager support 