import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = value_processing(data.decode())
        self.transport.write(resp.encode())


def value_processing(self, string):
    string_massive = string.split("\n").split(" ")
    for _ in string_massive:
        str_upd = _.split(' ')
        if str_upd[0] == "get":
            send_data(str_upd[1])
        elif str_upd[0] == "put":
            receive_data(str_upd[1], str_upd[2], str_upd[3])
        else:
            return 'error\nwrong command\n\n'


data_storage = {}
status = 'ok\n'


def send_data(key):
    string = status
    if key == "*":
        if data_storage != {}:
            massive = list(data_storage.keys())
            for smth in massive:
                for val in data_storage[smth]:
                    string += f"{key} {val[1]} {val[0]}\n"
        else:
            return string + '\n'
    else:
        if key in data_storage:
            for val in data_storage:
                try:
                    string += f"{key} {val[1]} {val[0]}\n"
                except IndexError:
                    return 'error\nwrong command\n\n'
    return string + '\n'


def receive_data(key, metric, timestamp):
    local = [timestamp, metric]
    if key not in data_storage:
        data_storage[key] = list()
    if not (timestamp, metric) in data_storage:
        data_storage[key].append(local)
    data_storage[key].sort()
    return status + '\n'


def run_server(host, port):
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
