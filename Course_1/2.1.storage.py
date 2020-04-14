import argparse
import os
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.isfile(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        local_data = f.read()
        if local_data:
            return json.loads(local_data)

        return {}


def get(key):
    data = get_data()
    return data.get(key)


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def clear():
    os.remove(storage_path)

#def keys():


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="key-value storage")
    parser.add_argument('--key', help='Key')
    parser.add_argument('--value', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')
    #parser.add_argument('--keys', help='Keys')
    args = parser.parse_args()
    data = get_data()

    if args.clear:
        clear()
    elif args.key and args.value:
        put(args.key, args.value)
    elif args.key:
        if not os.path.exists(storage_path):
            print(None)
        else:
            if args.key not in data:
                print(None)
            else:
                massive = get(args.key)
                string = ''
                for elem in massive:
                    string += elem + ', '
                print(string[:-2])
    else:
        print('Something was done unsuccessfully')







