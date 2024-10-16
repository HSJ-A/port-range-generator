import os
import sys
import traceback

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_remote_port_choice():
    while True:
        choice = input("Choose remote port option (1 or 2):\n1. Fixed number\n2. Match local port\nYour choice: ")
        if choice in ['1', '2']:
            return choice
        print("Invalid choice. Please enter 1 or 2.")

def generate_template(start_port, end_port, conn_type, remote_port_choice, fixed_remote_port=None):
    template = ""
    for port in range(start_port, end_port + 1):
        remote_port = fixed_remote_port if remote_port_choice == '1' else port
        template += f"""[[proxies]]
name = "{port}"
type = "{conn_type}"
localIP = "127.0.0.1"
localPort = {port}
remotePort = {remote_port}

"""
    return template

def main():
    try:
        start_port = get_int_input("Enter the start port range: ")
        end_port = get_int_input("Enter the end port range: ")
        conn_type = input("Enter the connection type (e.g., tcp): ")
        
        remote_port_choice = get_remote_port_choice()
        fixed_remote_port = None
        if remote_port_choice == '1':
            fixed_remote_port = get_int_input("Enter the fixed remote port number: ")

        template = generate_template(start_port, end_port, conn_type, remote_port_choice, fixed_remote_port)

        # Use the current working directory instead of script directory
        filename = os.path.join(os.getcwd(), "advanced_port_range_template.txt")

        print(f"Attempting to save file to: {filename}")

        with open(filename, "w") as f:
            f.write(template)

        if os.path.exists(filename):
            print(f"Template has been generated and saved to {filename}")
            print(f"File size: {os.path.getsize(filename)} bytes")
            with open(filename, "r") as f:
                print("First few lines of the file:")
                print(f.read(200))  # Print first 200 characters
        else:
            print(f"Error: File was not created at {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
        print("Traceback:")
        traceback.print_exc()
        print(f"Python version: {sys.version}")
        print(f"Current working directory: {os.getcwd()}")

    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
