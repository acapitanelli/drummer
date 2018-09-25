import socket
from messages import Message, MessageCode

# accepted connections
class SocketServerException(Exception):
    pass

class SocketServer():

    def init_socket(self):

        hostname = 'localhost'
        port = 10300

        max_connections = 1
        buffer_size = 4096

        # create TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket
        sock.bind( (hostname, port) )

        return sock, max_connections, buffer_size


    def run(self):

        # create TCP/IP socket
        sock, max_connections, buffer_size = self.init_socket()

        # listen mode
        sock.listen(max_connections)

        while True:

            # open a new connection
            connection, client_address = sock.accept()

            with connection:

                print('connection established with {0}'.format(client_address))

                try:

                    data_size = connection.recv(buffer_size).decode('utf-8')
                    print('message size is {0}'.format(data_size))

                    # send response about message size
                    connection.send(MessageCode.STATUS_OK.encode('utf-8'))

                    # init received data
                    data = b''
                    received_data = 0

                    # Receive the data in small chunks
                    while received_data < int(data_size):

                        chunk = connection.recv(buffer_size)

                        received_data += len(chunk)

                        data += chunk

                    # decode client request
                    request = Message.from_bytes(data)
                    print(request)

                    connection = self.send_response(connection, received_data)

                except Exception:
                    raise SocketServerException('error in server socket')

                finally:

                    # Clean up the connection
                    #connection = self.send_response(connection)
                    connection.close()


    def send_response(self, connection, received_data):

        # send response
        response = (
            Message()
            .add_entry('type', 'response')
            .add_entry('size', received_data)
            .add_entry('status', MessageCode.STATUS_OK)
            .to_bytes()
        )

        try:
            # Send data
            print('sending the response')

            res = connection.sendall(response)

            if res:
                raise SocketServerException('impossible to send response to client')

            else:
                print('response sent')

        except Exception:
            raise SocketServerException('generic error, impossible to send response to client')

        return connection


if __name__ == '__main__':

    ss = SocketServer()
    ss.run()