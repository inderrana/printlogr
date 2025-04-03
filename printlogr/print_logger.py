"""
Main logger implementation for PrintLog.
"""

import sys
import time
from datetime import datetime
from typing import Optional, List, Union, Any
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

class PrintLogger:
    """
    A logger that saves messages with timestamps in various formats (TXT, CSV, PDF).
    Use the plog() method to log and display messages.
    """
    
    def __init__(self, log_file: str = "print_log.txt"):
        """
        Initialize the PrintLogger.
        
        Args:
            log_file (str): Default log file path
        """
        self.log_file = log_file
        self.logs: List[tuple] = []
    
    def plog(self, *args: Any, sep: str = ' ', end: str = '\n', file: Optional[Any] = None) -> None:
        """
        Log and display a message.
        
        Args:
            *args: Values to log and display
            sep (str): Separator between values (default: space)
            end (str): String to append at the end (default: newline)
            file: Optional file object to write to (default: sys.stdout)
        """
        # Get the message
        message = sep.join(str(arg) for arg in args)
        
        # Log the message
        if message.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.logs.append((timestamp, message.strip()))
        
        # Display the message
        if file is None:
            file = sys.stdout
        print(message, end=end, file=file)
    
    def save_logs(self, format: str = "txt", output_file: Optional[str] = None) -> None:
        """
        Save logs in the specified format.
        
        Args:
            format (str): Output format ('txt', 'csv', or 'pdf')
            output_file (str, optional): Output file path. If None, uses default log_file
        """
        if not output_file:
            output_file = self.log_file
            
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
        
        if format.lower() == "txt":
            self._save_as_txt(output_file)
        elif format.lower() == "csv":
            self._save_as_csv(output_file)
        elif format.lower() == "pdf":
            self._save_as_pdf(output_file)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _save_as_txt(self, output_file: str) -> None:
        """Save logs as a text file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for timestamp, message in self.logs:
                    f.write(f"[{timestamp}] {message}\n")
        except IOError as e:
            print(f"Error saving to {output_file}: {e}")
    
    def _save_as_csv(self, output_file: str) -> None:
        """Save logs as a CSV file."""
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'Message'])
                for timestamp, message in self.logs:
                    writer.writerow([timestamp, message])
        except IOError as e:
            print(f"Error saving to {output_file}: {e}")
    
    def _save_as_pdf(self, output_file: str) -> None:
        """Save logs as a PDF file."""
        try:
            doc = SimpleDocTemplate(output_file, pagesize=letter)
            elements = []
            
            # Add title
            styles = getSampleStyleSheet()
            title = Paragraph("Print Log", styles['Title'])
            elements.append(title)
            elements.append(Paragraph("<br/><br/>", styles['Normal']))
            
            # Create table data
            data = [["Timestamp", "Message"]]
            for timestamp, message in self.logs:
                data.append([timestamp, message])
            
            # Create table
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(table)
            
            # Build PDF
            doc.build(elements)
        except Exception as e:
            print(f"Error saving to {output_file}: {e}")
    
    def get_logs(self) -> List[tuple]:
        """
        Get all logged messages with their timestamps.
            
        Returns:
            List[tuple]: List of (timestamp, message) tuples
        """
        return self.logs
    
    def clear_logs(self) -> None:
        """Clear all stored logs."""
        self.logs = []
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.save_logs()
    
    def display_logs(self) -> str:
        """
        Get all logs as a formatted string.
        
        Returns:
            str: Formatted logs as a string.
        """
        result = []
        for timestamp, message in self.logs:
            result.append(f"[{timestamp}] {message}")
        return "\n".join(result) 