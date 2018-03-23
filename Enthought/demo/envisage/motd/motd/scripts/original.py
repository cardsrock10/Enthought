""" Basic MOTD Application

This script prints out a message of the day from a list

"""


def main():
    from motd.model.motd import MOTD
    from motd.messages import messages
    from motd.util import print_message
    
    motd = MOTD(messages=messages)
    message = motd.get_messages()
    print_message(message)
    

if __name__ == "__main__":
    main()

