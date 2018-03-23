# Standard library imports.
import os.path

from pyface.tasks.api import TraitsDockPane
from traits.api import HasTraits, Event, File, Instance, List, Str
from traitsui.api import View, Item, FileEditor

class FileBrowserPane(TraitsDockPane):
    """ A simple file browser pane.
    """

    #### TaskPane interface ###################################################

    id = 'image_viewer.file_browser_pane'
    name = 'File Browser'

    #### FileBrowserPane interface ############################################

    # Fired when a file is double-clicked.
    activated = Event

    # The list of wildcard filters for filenames.
    filters = List(Str)

    # The currently selected file.
    selected_file = File(os.path.expanduser('~'))

    # The view used to construct the dock pane's widget.
    view = View(Item('selected_file',
                     editor=FileEditor(dclick_name='activated',
                                       filter_name='filters'),
                     style='custom',
                     show_label=False),
                resizable=True)

