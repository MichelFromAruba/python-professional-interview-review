message = 'foo'


def show_message(msg: str = 'default message'):
    print(f'message: {msg}')

    global message

    message = msg

    return message


returned_message = show_message('bar')

print(f'returned message: {returned_message}')
print(f'final message: {message}')
