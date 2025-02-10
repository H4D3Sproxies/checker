import os
import requests

def get_proxy_files():
    folder = 'proxies'
    
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):  # Check if it's a file
            remove_duplications(file_path)
        elif os.path.isdir(file_path):  # Optionally handle directories
            print(f"Directory: {file_path}")


def remove_duplications(file_path):
    # Use a set to store unique lines
    unique_lines = set()

    # Open the input file and process it
    with open(file_path, "r", encoding="utf-8") as infile:
        for line in infile:
            # Strip whitespace and add the line to the set
            unique_lines.add(line.strip())

    # Write the unique lines back to the output file
    with open(file_path, "w", encoding="utf-8") as outfile:
        for line in unique_lines:
            outfile.write(line + "\n")

    print(f"Duplicate lines removed. Unique lines saved to '{file_path}'.")

def clean_garbage():
    folder_path = "proxies/legacy"

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Only process text files
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            # Remove lines containing '='
            filtered_lines = [line for line in lines if "=" not in line]

            # Write back to the file
            with open(file_path + 't', "w") as file:
                file.writelines(filtered_lines)

      

def combine_files(protocol):
    # Specify the folder containing your text files
    folder_path = "proxies"
    output_file = f"proxies/{protocol}.txt"

    # Open the output file in write mode
    with open(output_file, "a", encoding="utf-8") as outfile:
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            # Make sure it's a text file
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                try:
                    # Open each file and append its contents to the output file
                    with open(file_path, "r", encoding="utf-8") as infile:
                        outfile.write(f"=== Contents of {filename} ===\n")  # Optional: Add header for each file
                        outfile.write(infile.read() + "\n")  # Append the content with a newline
                        outfile.write("\n")  # Add a blank line after each file's contents
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    print(f"All files have been combined into '{output_file}'.")

def verify_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Folder '{dir_name}' created.")

def get_ip():
    # Test endpoint to check public IP
    url = "https://api64.ipify.org?format=json"

    # Send a request through the VPN
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()['ip']
        else:
            print(f"Failed to fetch IP: {response.status_code}")
            return ''
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        
def check_ip(ip):
    if get_ip() == ip:
        return True
    
    return False