def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
                                   fcntl.ioctl(0, termios.TIOCSWINSZ,
                                               struct.pack('HHHH', 0, 0, 0)))
    return tw, th


print('Number of columns and Rows: ', terminal_size())
