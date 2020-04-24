import asyncio

data_storage = {}
status = 'ok\n'


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data: bytes):
        resp = self.value_processing(data.decode())
        self.transport.write(resp.encode())

    def value_processing(self, string):
        string_massive = string[:-1].split(" ")
        if len(string_massive) != 1:
            if string_massive[0] == "get":
                return self.send_data(string_massive[1])
            elif string_massive[0] == "put":
                return self.receive_data(string_massive[1], string_massive[2], string_massive[3])
            else:
                return 'error\nwrong command\n\n'
        else:
            return 'error\nwrong command\n\n'

    @staticmethod
    def send_data(key):
        if key == "*":
            for key, values in data_storage.items():
                values.sort()
                string = status
                for items in values:
                    try:
                        string += f'{key} {items[1]} {items[0]}\n'
                    except IndexError:
                        return 'error\nwrong command\n\n'
        else:
            if key in data_storage:
                string = status
                massive = data_storage[key]
                for val in massive:
                    try:
                        string += f"{key} {val[1]} {val[0]}\n"
                    except IndexError:
                        return 'error\nwrong command\n\n'
            else:
                string = status
        return string + '\n'

    @staticmethod
    def receive_data(key, metric, timestamp):
        local = [timestamp, metric]
        if key not in data_storage:
            data_storage[key] = list()
        else:
            for every in data_storage[key]:
                if timestamp == every[0]:
                    data_storage[key].remove(every)
                    data_storage[key].append(local)
                    data_storage[key].sort()
        return status + '\n'


def run_server(host='127.0.0.1', port=10001):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server()