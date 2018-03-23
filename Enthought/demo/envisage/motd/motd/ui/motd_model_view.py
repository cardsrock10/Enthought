
from traits.api import HTML, Property, Supports, cached_property
from traitsui.api import Action, Item, ModelView, View


html_template = """
<html>
<head><title>Message of the Day</title></head>
<body>
<p>
{message.text}
</p>
<p>
- {message.author}
</p>
</body>
</html>
"""

new_message_action = Action(
    name="New Message",
    action="on_new_message",
)

class MOTDModelView(ModelView):
    
    #: the current message we are displaying
    message = Supports('motd.model.i_message.IMessage')
    
    #: the text of the message, formatted using HTML
    html = Property(HTML, depends_on=['message.text', 'message.author'])
    
    @cached_property
    def _get_html(self):
        html = html_template.format(message=self.message)
        return html

    def _model_changed(self, new):
        if new:
            self.message = self.model.get_message()

    def _model_default(self):
        from motd.model.motd import MOTD
        return MOTD()

    def _message_default(self):
        message = self.model.get_message()
        return message

    def on_new_message(self, event=None):
        """ Get a new message from the MOTD instance """
        self.message = self.model.get_message()

    view = View(
        Item('html', show_label=False),
        width=400, height=200,
        title="Message of the day",
        buttons=[new_message_action],
    )
