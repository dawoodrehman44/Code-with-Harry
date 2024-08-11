with open('myfile2.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)

    print(f.tell()) # tell() function track the seek function's location 

    #Read the next 5 bytes
    data = f.read(5)
    print(data)
