import socket
import threading
import pygame


class server:
    def __init__(self, window, host, text, board):
        self.window = window
        self.chat_text = []
        self.writing_font = pygame.font.Font(None, 22)
        self.sender = None
        self.board = board
        board.set_server(self)
        if host:
            self.opp_title = "P2: "
            self.play_title = "P1: "
            self.new_server()
        else:
            self.opp_title = "P1: "
            self.play_title = "P2: "
            self.join(text)

    def new_server(self):
        # Creates new server
        new_socket = socket.socket()
        host_name = socket.gethostname()
        ip = socket.gethostbyname(host_name)
        port = 8080
        new_socket.bind((host_name, port))
        self.post("Your game ID is " + ip, "")

        # Starts a new thread to listen for connections
        listen_thread = threading.Thread(target=self.listening, args=([new_socket]))
        listen_thread.start()

    def join(self, address):
        # Connects to an existing server
        new_socket = socket.socket()
        self.sender = new_socket
        port = 8080
        new_socket.connect((address, port))
        self.post("Connected!", "")

        # Starts a new thread to listen for messages
        y = threading.Thread(target=self.rec, args=([new_socket]))
        y.start()

    def listening(self, new_socket):
        # Listens for a connection
        new_socket.listen(1)
        conn, address = new_socket.accept()
        self.sender = conn
        self.post("Player 2 has joined.", "")
        y = threading.Thread(target=self.rec, args=([conn]))
        y.start()

    def rec(self, sock):
        # Receives messages from other player
        while True:
            mess = sock.recv(8080)
            mess = mess.decode()
            if "##" in mess:
                p1 = self.board.squares[int(mess[2])][int(mess[3])]
                p2 = self.board.squares[int(mess[4])][int(mess[5])]
                self.board.move(p1, p2)
            else:
                self.post(str(mess), self.opp_title)

    def send_message(self, message):
        # Sends messages to other player
        self.sender.send(message.encode())
        if "##" not in message:
            self.post(message, self.play_title)

    def post(self, text, title):
        self.chat_text.append(title + text)

        # Resets text box
        pygame.draw.rect(self.window, (186, 140, 99), (480, 245, 200, 30))

        # Scrolls down
        if len(self.chat_text) > 10:
            self.chat_text.pop(0)
            pygame.draw.rect(self.window, (245, 245, 220), (480, 40, 240, 200))

        # Posts new text
        y = 47
        for text in self.chat_text:
            text_input = self.writing_font.render(text, True, (0, 0, 0))
            self.window.blit(text_input, (485, y))
            y += 19
