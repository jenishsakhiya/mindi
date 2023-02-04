


def receive_message(peer_socket, header_length=10):
    HEADER_LENGTH = header_length
    try:
        # Receive our "header" containing message length, it's size is defined and constant
        message_header = peer_socket.recv(HEADER_LENGTH)

        # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(message_header):
            return False

        # Convert header to int value
        message_length = int(message_header.decode('utf-8').strip())

        # Return an object of message header and message data
        message = peer_socket.recv(message_length)
        print("Received message:", message)
        return {'header': message_header, 'data': message.decode('utf-8')}

    except Exception as e:
        raise e
        # If we are here, client closed connection violently, for example by pressing ctrl+c on his script
        # or just lost his connection
        # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
        # and that's also a cause when we receive an empty message
        return {'data': False}

def send_message(peer_socket, message, header_length=10):
    HEADER_LENGTH = header_length
    try:
        print("Sending message:", message)
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        peer_socket.send(message_header + message)
        return True
    except Exception as e:
        raise e
        # If we are here, client closed connection violently, for example by pressing ctrl+c on his script
        # or just lost his connection
        # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
        # and that's also a cause when we receive an empty message
        return False