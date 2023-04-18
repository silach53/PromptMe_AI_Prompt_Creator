import os

def read_all_files(directory):
    file_contents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if(file_path[-4:]=="x.py"):
                continue 
            if file_path.endswith('.py') or file_path.endswith('.html') or file_path.endswith('.css') or file_path.endswith('.js'):
                with open(file_path, 'r') as f:
                    file_contents.append('/'.join([x for x in file_path.split('/')[4:]]))
                    file_contents.append(f.read())
    return '\n\n'.join(file_contents)

print(os.getcwd())
all_file_contents = read_all_files(os.getcwd())
with open('x.txt', 'w') as f:
    f.write(all_file_contents)
