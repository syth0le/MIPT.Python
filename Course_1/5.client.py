import socket
import time


class ClientInitError(Exception):
    # this error appears when connection wasn't done successfully
    pass


class ClientError(Exception):
    # this error appears when work of method 'put' was done unsuccessfully
    pass


class TimestampError(Exception):
    # this error appears when invalid timestamp was entered
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        try:
            self.sock = socket.create_connection((host, int(port)), int(timeout))
        except socket.error as error:
            raise ClientInitError("Connection error", error)

    def get(self, name):
        message = f'get {name}\n'
        self._data_send(message)
        message_out = str(self._data_read())
        message_dict = {}
        if message_out[0:3] != 'ok\n':
            raise ClientError(message_out)

        message_out = str(message_out).split('\n')

        for _ in message_out[1:-2]:
            local = _.split(' ')
            if len(local) == 3:
                if not local[0] in message_dict:
                    message_dict[local[0]] = list()
                local_list = message_dict.get(local[0], [])
                local_list.append((int(local[2]), float(local[1])))
                message_dict.update({local[0]: sorted(local_list)})

            elif local not in [["'ok"], [""], ["'"]]:
                raise ClientError

        return message_dict

    def put(self, name, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        message = f'put {name} {str(value)} {str(timestamp)}\n'
        self._data_send(message)
        message_out = self._data_read()
        if message_out[0:3] != 'ok\n':
            raise ClientError(message_out)

    def _data_read(self):
        try:
            server_answer = self.sock.recv(1024).decode("utf8")
        except socket.error as error:
            raise ClientError("Error receiving data", error)
        return server_answer

    def _data_send(self, message):
        try:
            self.sock.sendall(message.encode('utf-8'))
        except socket.error as error:
            raise ClientError("Put data unavailable", error)


if __name__ == "__main__":
    client = Client("127.0.0.1", 10001, timeout=10)
    client.put("first", 0.5, timestamp=1)
    client.put("first", 2.0, timestamp=2)
    client.put("first", 0.5, timestamp=3)
    client.put("snf", 0.5, timestamp=3)
    client.put("second", 3, timestamp=4)
    client.put("second", 4, timestamp=5)
    client.put("first", 0.54, timestamp=1)
    client.put("first", 2.04, timestamp=2)
    client.put("first", 0.52, timestamp=3)
    client.put("second", 33, timestamp=4)
    client.put("33", 33, timestamp=4)
    print(client.get("*"))

