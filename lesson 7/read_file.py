# by Kami Bigdely
# Remove control flag
# Reference: https://stackoverflow.com/a/10140333/81306
# This code snippet reads up to the end of the file

# Size of each chunk to read from the file (in bytes)
n = 16

# Open the file in binary read mode
with open('foobar.file', 'rb') as fp:
    # Read the file in chunks until the end is reached
    while True:
        # Read a chunk of 'n' bytes from the file
        chunk = fp.read(n)
        
        # Check if we've reached the end of the file
        # When read() returns an empty bytes object, we've reached EOF
        if chunk == b'':
            break  # Exit the loop when end of file is reached
        else:
            # Process the current chunk (in this case, just print it)
            print(chunk)
            # Uncomment the line below to add custom processing logic
            # process(chunk)
