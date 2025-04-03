# PrintLogr

A Python library for logging messages with timestamps in various formats (TXT, CSV, PDF).

## Features

- Simple logging with timestamps using `plog()` method
- Multiple export formats (TXT, CSV, PDF)
- Context manager support
- Clean and organized log format

## Installation

```bash
pip install printlogr
```

## Usage

### Basic Usage

```python
from printlogr import PrintLogger

# Create a logger instance
logger = PrintLogger()

# Log messages - they will be displayed and logged
logger.plog("Hello, World!")
logger.plog("This is a test message")

# Save logs to a file
logger.save_logs()  # Saves as TXT by default
```

### Using Different Export Formats

```python
from printlogr import PrintLogger

logger = PrintLogger()

logger.plog("First message")
logger.plog("Second message")

# Save as different formats
logger.save_logs(format="txt", output_file="output.txt")
logger.save_logs(format="csv", output_file="output.csv")
logger.save_logs(format="pdf", output_file="output.pdf")
```

### Using as Context Manager

```python
from printlogr import PrintLogger

with PrintLogger() as logger:
    logger.plog("This message will be logged")
    logger.plog("And this one too")
    # Logs are automatically saved when the context manager exits
```

### Advanced Usage

```python
from printlogr import PrintLogger

logger = PrintLogger()

# plog works like print - supports multiple arguments
logger.plog("Value:", 42, "Status:", True)

# Supports sep and end parameters like print
logger.plog("Hello", "World", sep="-", end="!\n")

# Get logs programmatically
logs = logger.get_logs()  # Returns list of (timestamp, message) tuples

# Get logs as formatted string
log_string = logger.display_logs()
print(log_string)

# Clear logs if needed
logger.clear_logs()
```

## Output Formats

### TXT Format
```
[2024-03-14 10:30:45] Hello, World!
[2024-03-14 10:30:46] This is a test message
```

### CSV Format
```csv
Timestamp,Message
2024-03-14 10:30:45,Hello, World!
2024-03-14 10:30:46,This is a test message
```

### PDF Format
A nicely formatted PDF document with timestamps and messages in a table format.

## API Reference

### PrintLogger Class

#### `__init__(log_file: str = "print_log.txt")`
Initialize the logger with optional log file path.

#### `plog(*args, sep=' ', end='\n', file=None)`
Log and display a message. Works like the built-in `print()` function.
- `*args`: Values to log and display
- `sep`: Separator between values (default: space)
- `end`: String to append at the end (default: newline)
- `file`: Optional file object to write to (default: sys.stdout)

#### `save_logs(format: str = "txt", output_file: Optional[str] = None)`
Save logs in the specified format.
- `format`: Output format ('txt', 'csv', or 'pdf')
- `output_file`: Output file path (optional)

#### `get_logs() -> List[tuple]`
Get all logged messages with their timestamps.

#### `clear_logs()`
Clear all stored logs.

#### `display_logs() -> str`
Get all logs as a formatted string.

## License

This project is licensed under the MIT License - see the LICENSE file for details.