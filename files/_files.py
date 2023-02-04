# file = open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r")
# # not a good way of reading file
# contents = file.read()  # entire contents of the file is read as one single string
# file.close()
# starndard way of reading files
# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     contents = file.readlines()  # reads the entire contents of the file into a list  
#     for line in contents:
#         print(line)

# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     for _ in range(10):     # _ (underscore) is called as "throw-away" variable 
#         line = file.readline()
#         print(line)
    
# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     for line in file:
#         print(line)


# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     for index, line in enumerate(file, start=1):
#         print(index, line)

# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     contents = file.readlines()
#     print(len(contents))

# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     count = 0
#     for line in file:
#         count = count + 1
#     print(f"total lines {count}")

# extracting IP Address from log file
ip_address = [ ]
with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
    for line in file:
        words = line.split()
        ip_address.append(words[0])
    
# unique ip address
unique_ip = set(ip_address)

# solution2
unique_ip = [ ]
for item in ip_address:
    if item not in unique_ip:
        unique_ip.append(item)

# d = {"10.1.2.3": 10, "198.34.23.33": 3}

# ip_count_pair = { }
# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     for line in file:
#         words = line.split()
#         ip_address = words[0]
#         if ip_address in ip_count_pair:
#             ip_count_pair[ip_address] = ip_count_pair[ip_address] + 1
#         else:
#             ip_count_pair[ip_address] = 1

# from collections import defaultdict

# d = defaultdict(int)
# with open("/Users/sandeep/Desktop/Training/_python/data_files/access-log.txt", "r") as file:
#     for line in file:
#         words = line.split()
#         ip_address = words[0]
#         # not checking if the key is present in the dict or not
#         d[ip_address] = d[ip_address] + 1

# errors ={"INFO": 100, "WARNING": 10, "TRACE": 20}

# errors = { }
# with open("/Users/sandeep/Desktop/Training/_python/data_files/sample.log", "r") as file:
#     for line in file:
#         if line.strip():        # boolean value if string
#             words = line.split()
#             message_type = words[2]
#             if message_type not in errors:
#                 # key does not exist. So please goahed and create a key and initlise the value to 1
#                 errors[message_type] = 1
#             else:
#                 # get the existing value of the key and increment by 1
#                 errors[message_type] = errors[message_type] + 1

# from collections import defaultdict
# _errors = defaultdict(int)
# with open("/Users/sandeep/Desktop/Training/_python/data_files/sample.log", "r") as file:
#     for index, line in enumerate(file, start=1):
#         clean_line = line.strip()
#         if clean_line:        # boolean value if string
#             words = clean_line.split()
#             message_type = words[2]
#             # creation of the key, initlization, incrementation
#             _errors[message_type] = _errors[message_type] + 1
#         else:
#             print(f"line no. {index} is empty")

def word_count(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                words = clean_line.split()
                count += len(words)
    return count

def count_word(which_word, filepath):
    count = 0
    with open(filepath, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                count += clean_line.count(which_word)
    return count

# writing to a text file
# with open('spam.txt', 'a') as file:
#     file.write("this is python class")


# with open("/Users/sandeep/Desktop/Training/_python/data_files/sample.log", "r") as read_file:
#     with open("trace_messages.txt", "w") as write_file:
#         for lineno, line in enumerate(read_file, start=1):
#             if "INFO" in line:
#                 write_file.write(f"Line No: {lineno} {line.strip()} \n")

# with open("/Users/sandeep/Desktop/Training/_python/data_files/sample.log", "r") as read_file, open("info_messages.txt", "w") as write_file:
#     for lineno, line in enumerate(read_file, start=1):
#         if "INFO" in line:
#             write_file.write(f"Line No: {lineno} {line.strip()} \n")

with open("/Users/sandeep/Desktop/Training/_python/training/file1.txt") as f1, open("/Users/sandeep/Desktop/Training/_python/training/file2.txt") as f2:
    for file1_line, file2_line in zip(f1, f2):
        print(f"{file1_line.strip()} \t {file2_line.strip()}")
