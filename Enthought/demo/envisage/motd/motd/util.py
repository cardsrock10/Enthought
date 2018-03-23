

def print_message(message):
    """ Pretty-print the message to stdout """
    
    print '\n"{message.text}"\n\n- {message.author}'.format(message=message)
