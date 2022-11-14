full_path = input().split("\\")
filename, extension = full_path[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
