import tempfile
import os


class File:
    def __init__(self, path):
        if os.path.exists(path):
            self.path = path
        else:
            self.path = path
            with open(self.path, 'w') as f:
                pass

    def __str__(self):
        return self.path

    def __add__(self, other):  # create a new file with writing to it
        local_path = os.path.join(tempfile.gettempdir(), "something.txt")
        result = File(local_path)
        result.write(self.read() + other.read())
        #with open(local_path, 'w'):
            #with open(self.path, 'r') as first:
             #   result.write(first.read())
            #with open(other.path, 'r') as second:
             #   result.write(second.read())
        return result

    def write(self, message=str):
        with open(self.path, 'a') as f:
            return f.write('{}'.format(message))

    def read(self):
        try:
            with open(self.path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''

    def __iter__(self):
        return open(self.path, 'r')



path_to_file = 'some_filename'
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
print(file_obj.read())
file_obj.write('some text')
print(file_obj.read())
file_obj.write('Message')
print(file_obj.read())
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('Hello\n')
file_obj_2.write('My\n')
file_obj_2.write('Name\n')
file_obj_2.write('IS\n')
file_obj_2.write('Daniil\n')
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
print(new_file_obj)
for line in new_file_obj:
    print(line)


