import asyncio

data_storage = dict()


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data: bytes):
        decoding_data = data.decode()[:-1].split(" ")
        resp = self.value_processing(decoding_data)
        self.transport.write(resp.encode())

    def value_processing(self, param):
        if param[0] == "put":
            return self.receive_data(param[1], param[2], param[3])
        elif param[0] == "get":
            return self.send_data(param[1])
        else:
            return 'error\nwrong command\n\n'

    @staticmethod
    def send_data(key):
        status = 'ok\n'
        if key == "*":
            for key, values in data_storage.items():
                for items in values:
                    status += f'{key} {items[1]} {items[0]}\n'
        else:
            if key in data_storage:
                for val in data_storage[key]:
                    status += f"{key} {val[1]} {val[0]}\n"
        return status + '\n'

    @staticmethod
    def receive_data(key, metric, timestamp):
        status = 'ok\n'
        local = (timestamp, metric)
        if key not  in data_storage:
            data_storage[key] = list()
        if local not  in data_storage[key]:
            data_storage[key].append(local)
            data_storage[key].sort()
        return status + '\n'


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


#if __name__ == '__main__':
    #run_server('127.0.0.1', 10001)
