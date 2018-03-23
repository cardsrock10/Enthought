""" A 'Message of the Day' implementation """


# Enthought library imports.
from traits.api import HasTraits, List, Supports, provides

# Local imports.
from i_message import IMessage
from i_motd import IMOTD


@provides(IMOTD)
class MOTD(HasTraits):
    """ A 'Message of the Day' implementation """

    # The list of possible messages.
    messages = List(Supports(IMessage), minlen=1)

    ###########################################################################
    # 'IMOTD' interface.
    ###########################################################################

    def get_message(self):
        """ Prints a random message. """
        from random import choice

        message = choice(self.messages)
        return message

    ###########################################################################
    # 'MOTD' interface.
    ###########################################################################

    def _messages_default(self):
        """ The default message list to use when no other messages are provided """
        from message import Message
        messages = [
            Message(
                author='Anon', text='Work hard and be good to your Mother'
            ),
        ]
        return messages


#### EOF ######################################################################
