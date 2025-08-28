import struct

with open("records.bin", "rb") as infile:
    record_size = struct.calcsize("i20sif")
    while True:
        data = infile.read(record_size)
        if not data:
            break
        record = struct.unpack("i20sif", data)
        record = (record[0], record[1].decode().rstrip('\x00'), record[2], record[3])
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]:.2f}")