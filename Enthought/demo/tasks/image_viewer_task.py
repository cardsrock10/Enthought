# Enthought library imports.
from pyface.api import GUI
from pyface.tasks.api import Task, TaskWindow, TaskLayout, PaneItem, TraitsTaskPane, TraitsDockPane
from pyface.tasks.action.api import DockPaneToggleGroup, SMenuBar, \
    SMenu, SToolBar, TaskAction
from pyface.api import ConfirmationDialog, FileDialog, \
    ImageResource, YES, OK, CANCEL
from traits.api import on_trait_change

# Local imports.
from image_viewer import ImageViewerPane
from file_browser_pane import FileBrowserPane


class ImageViewerTask(Task):
    """ A simple task for viewing images.
    """
    #### Task interface #######################################################

    id = 'example.image_viewer_task'
    name = 'Image Viewer'

    #default_layout = TaskLayout(
    #    left=PaneItem('example.python_script_browser_pane'))

    menu_bar = SMenuBar(SMenu(TaskAction(name='Open...', method='open',
                                         accelerator='Ctrl+O'),
                              id='File', name='&File'),
                        SMenu(DockPaneToggleGroup(),
                              id='View', name='&View'))

    tool_bars = [ SToolBar(TaskAction(method='open',
                                      tooltip='Open a file',
                                      image=ImageResource('document_open'))) ]

    ###########################################################################
    # 'Task' interface.
    ###########################################################################

    def _default_layout_default(self):
        return TaskLayout(
            left=PaneItem('image_viewer.file_browser_pane'))

    def activated(self):
        """ Overriden to set the window's title.
        """
        filename = self.window.central_pane.model.path
        self.window.title = filename if filename else 'Untitled'

    def create_central_pane(self):
        """ Create the central pane: the image viewer.
        """
        return ImageViewerPane()
        
    def create_dock_panes(self):
        """ Create the file browser and connect to its double click event.
        """
        browser = FileBrowserPane(filters=["*.jpg"])
        handler = lambda: self._open_file(browser.selected_file)
        browser.on_trait_change(handler, 'activated')
        return [ browser ]

    ###########################################################################
    # 'ExampleTask' interface.
    ###########################################################################

    def open(self):
        """ Shows a dialog to open a file.
        """
        dialog = FileDialog(parent=self.window.control, wildcard='*.jpg')
        if dialog.open() == OK:
            self._open_file(dialog.path)
            
    ###########################################################################
    # Protected interface.
    ###########################################################################

    def _open_file(self, filename):
        """ Opens the file at the specified path in the editor.
        """
        self.window.central_pane.model.path = filename
        self.activated()


def main(argv):
    """ A simple example of using Tasks.
    """
    # Create the GUI (this does NOT start the GUI event loop).
    gui = GUI()

    # Create a Task and add it to a TaskWindow.
    task = ImageViewerTask()
    window = TaskWindow(size=(800, 600))
    window.add_task(task)
    # Show the window.
    window.open()

    # Start the GUI event loop.
    gui.start_event_loop()


if __name__ == '__main__':
    import sys
    main(sys.argv)
