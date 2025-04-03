"""
Test cases for PrintLogger class.
"""
import unittest
import os
import tempfile
from datetime import datetime
from printlogr import PrintLogger

class TestPrintLogger(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.log_file = os.path.join(self.temp_dir, "test_log.txt")
        self.logger = PrintLogger(self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        os.rmdir(self.temp_dir)

    def test_basic_logging(self):
        test_message = "Test message"
        print(test_message)
        self.logger.save_logs()
        
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            self.assertIn(test_message, log_content)
            self.assertIn(datetime.now().strftime("%Y-%m-%d"), log_content)

    def test_multiple_formats(self):
        test_message = "Test message"
        print(test_message)
        
        # Test TXT format
        self.logger.save_logs(format="txt")
        self.assertTrue(os.path.exists(self.log_file))
        
        # Test CSV format
        csv_file = os.path.join(self.temp_dir, "test_log.csv")
        self.logger.save_logs(format="csv", output_file=csv_file)
        self.assertTrue(os.path.exists(csv_file))
        
        # Test PDF format
        pdf_file = os.path.join(self.temp_dir, "test_log.pdf")
        self.logger.save_logs(format="pdf", output_file=pdf_file)
        self.assertTrue(os.path.exists(pdf_file))

    def test_context_manager(self):
        test_message = "Context manager test"
        with PrintLogger(self.log_file) as logger:
            print(test_message)
        
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            self.assertIn(test_message, log_content)

if __name__ == '__main__':
    unittest.main() 