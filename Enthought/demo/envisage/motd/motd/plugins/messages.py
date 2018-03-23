""" A plugin which contributes the default motd messages """

from traits.api import Instance, List
from envisage.api import Plugin


class MessagesPlugin(Plugin):
    """ A plugin which contributes the default motd messages. """
    
    #: The Ids of the extension points that this plugin contributes to.
    MESSAGES = 'motd.messages'

    # This tells us that the plugin contributes the value of this trait to the
    # MESSAGES extension point.
    messages = List(Instance('motd.model.message.Message'),
                    contributes_to=MESSAGES)

    # This shows how you can use a standard trait initializer to populate the
    # list dynamically.
    def _messages_default(self):
        """ Get the default messages from the motd messages module. """

        # we defer loading the messages until something asks for them
        from motd.messages import messages
        
        return messages

