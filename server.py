import socket
import threading
import pygame

sender = None
oppo_title = ""
play_title = ""
window = None
chat_text = None
writing_font = None


def new_server(wind, chat, writing):
    # Appoints graphics
    global oppo_title, play_title, window, chat_text, writing_font
    oppo_title = "P2: "
    play_title = "P1: "
    window = wind
    chat_text = chat
    writing_font = writing

    # Creates new server
    new_socket = socket.socket()
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    port = 8080
    new_socket.bind((host_name, port))
    post("Your game ID is " + ip, "")

    # Starts a new thread to listen for connections
    listen_thread = threading.Thread(target=listening, args=([new_socket]))
    listen_thread.start()


def join(address, wind, chat, writing):
    # Appoints graphics
    global oppo_title, play_title, window, chat_text, writing_font, sender
    oppo_title = "P1: "
    play_title = "P2: "
    window = wind
    chat_text = chat
    writing_font = writing

    # Connects to an existing server
    new_socket = socket.socket()
    sender = new_socket
    server_host = address
    port = 8080
    new_socket.connect((server_host, port))
    post("Connected!", "")

    # Starts a new thread to listen for messages
    y = threading.Thread(target=rec, args=([new_socket]))
    y.start()


def listening(new_socket):
    # Listens for a connection
    new_socket.listen(1)
    conn, address = new_socket.accept()
    global sender
    sender = conn
    post("Player 2 has joined.", "")
    y = threading.Thread(target=rec, args=([conn]))
    y.start()


def rec(sock):
    # Receives messages from other player
    while True:
        mess = sock.recv(8080)
        mess = mess.decode()
        post(str(mess), oppo_title)


def send_message(message):
    # Sends messages to other player
    sender.send(message.encode())
    post(message, play_title)


def post(text, title):
    chat_text.append(title + text)

    # Resets text box
    pygame.draw.rect(window, (186, 140, 99), (480, 245, 200, 30))

    # Scrolls down
    if len(chat_text) > 10:
        chat_text.pop(0)
        pygame.draw.rect(window, (245, 245, 220), (480, 40, 240, 200))

    # Posts new text
    y = 47
    for text in chat_text:
        text_input = writing_font.render(text, True, (0, 0, 0))
        window.blit(text_input, (485, y))
        y += 19
