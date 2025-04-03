"""
Command-line interface for PrintLog.
"""
import argparse
import sys
from printlog import PrintLogger

def main():
    parser = argparse.ArgumentParser(description="PrintLog - Log print statements with timestamps")
    parser.add_argument("--output", "-o", default="print_log.txt",
                      help="Output file path (default: print_log.txt)")
    parser.add_argument("--format", "-f", choices=["txt", "csv", "pdf"],
                      default="txt", help="Output format (default: txt)")
    parser.add_argument("--clear", "-c", action="store_true",
                      help="Clear existing logs before starting")
    
    args = parser.parse_args()
    
    logger = PrintLogger(args.output)
    if args.clear:
        logger.clear_logs()
    
    print(f"PrintLog started. Logging to {args.output} in {args.format} format.")
    print("Press Ctrl+C to stop and save logs.")
    
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            print(line.rstrip())
    except KeyboardInterrupt:
        print("\nSaving logs...")
        logger.save_logs(format=args.format)
        print("Done!")

if __name__ == "__main__":
    main() 