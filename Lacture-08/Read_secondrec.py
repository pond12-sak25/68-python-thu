import struct

record_format = "i20sif"
record_size = struct.calcsize(record_format)
with open("records.bin", "rb") as file:
    file.seek(record_size)  # Move to the second record
    data = file.read(record_size)
    data = struct.unpack(record_format, data)
    data = (data[0], data[1].decode().rstrip('\x00'), data[2], data[3])
    print(f"ID: {data[0]}, Name: {data[1]}, Age: {data[2]}, GPA: {data[3]:.2f}")