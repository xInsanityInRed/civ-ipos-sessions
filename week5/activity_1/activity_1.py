# from io import

def main():
    pass

# Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal
def reverse_bytes(bytes_data):
    return bytes_data[::-1]

def convert_bytes_to_text(bytes_data):
    return bytes_data.decode('utf-8')

def convert_bytes_to_utf8(bytes_data):
    return bytes_data.encode('utf-8')

# Main program logic
try:
    # Open the binary file for reading and create output text and bytes files for writing using the context manager
    with open("data.bin", "rb") as file, \
        open("converted.bin", "w") as text_output, \
        open("reversed_bytes.bin", "wb") as bytes_output:
        # Iterate through each line in the binary file
        for line in file:
            # Decode the line to Unicode string and remove leading/trailing whitespaces
            line = line.decode('utf-8').strip()
            # Check if the line starts with "TEXT:"
            if line.startswith("TEXT:"):
                # Extract text content, convert to uppercase, and write to text file
                continue
            elif line.startswith("BYTES:"):
                encoded_hex_data = line[6:].encode().hex()
                bytes_data
    pass

            # Check if the line starts with "BYTES:"
            # elif line.startswith("BYTES:"):

                # Extract the string and encode to hexadecimal

                # Extract byte content, convert to bytes object(using fromhex()), 
     
                # reverse bytes, and write to bytes file


    # Print success message


# Handle file I/O errors
except IOError:
    print("You have no file!")

# Handle other exceptions using the exception class

if __name__ == "__main__":
    main()