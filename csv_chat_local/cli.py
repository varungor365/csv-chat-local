import os
import subprocess
import sys


def main():
    """Run the Streamlit app"""
    # Find the path to app.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(current_dir, "app.py")
    
    # Run streamlit
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path], check=True)
    except KeyboardInterrupt:
        print("\nShutting down csv-chat-local...")
        sys.exit(0)

if __name__ == "__main__":
    main()
