# PrintLog

A Python library that captures print statements and saves them with timestamps in various formats (TXT, CSV, PDF).

## Features

- Automatically captures all print statements
- Adds timestamps to each log entry
- Supports multiple export formats (TXT, CSV, PDF)
- Context manager support
- Clean and organized log format

## Installation

```bash
pip install printlog
```

## Usage

### Basic Usage

```python
from printlog import PrintLogger

# Create a logger instance
logger = PrintLogger()

# Your print statements will now be logged
print("Hello, World!")
print("This is a test message")

# Save logs to a file
logger.save_logs()  # Saves as TXT by default
```

### Using Different Export Formats

```python
from printlog import PrintLogger

logger = PrintLogger()

print("First message")
print("Second message")

# Save as different formats
logger.save_logs(format="txt", output_file="output.txt")
logger.save_logs(format="csv", output_file="output.csv")
logger.save_logs(format="pdf", output_file="output.pdf")
```

### Using as Context Manager

```python
from printlog import PrintLogger

with PrintLogger() as logger:
    print("This message will be logged")
    print("And this one too")

# Logs are automatically saved when the context manager exits
```

### Accessing Logs Programmatically

```python
from printlog import PrintLogger

logger = PrintLogger()

print("Test message 1")
print("Test message 2")

# Get all logs
logs = logger.get_logs()
for timestamp, message in logs:
    print(f"{timestamp}: {message}")

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
A nicely formatted PDF document with timestamps and messages.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 