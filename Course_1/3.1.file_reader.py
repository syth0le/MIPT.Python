class FileReader:

    def __init__(self, storage_path):
        self.raw = storage_path

    def read(self):
        try:
            with open(self.raw, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            return ''
