#!/usr/bin/env python3

import socket, sys

HOST = 'AMDarch'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'abc')

    def on_press(key):
        global ev
        s.sendall(str.encode("e"+str(key)))

    if sys.platform == "linux":  # Use another (not on xserver relying) way to read keyboard input, to make this shit work in tty or via ssh, where no xserver is available
        def recogniser():
            import tty, sys, termios
            global ev, old_settings, termios, fd, do_exit

            do_exit = False
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(fd)
            while True:
                char = sys.stdin.read(1)
                ev = {ord(char): f"'{char.rstrip()}'", 13: "Key.enter", 127: "Key.backspace", 32: "Key.space", 27: "Key.esc"}[ord(char)]
                if ord(char) == 3 or do_exit:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    ev = "exit"
                s.sendall(str.encode("e"+ev))
    else:
        from pynput.keyboard import Key, Listener
        def recogniser():
            global ev
            while True:
                with Listener(on_press=on_press) as listener:
                    listener.join()
    recogniser()
    #data = s.recv(1024)

#print('Received', repr(data))
