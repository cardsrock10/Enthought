from traits.api import HasTraits, File, Instance, Property, cached_property
from traitsui.api import View, Item, ImageEditor
from pyface.image_resource import ImageResource
from pyface.tasks.api import TraitsTaskPane

class ImageViewer(HasTraits):
    
    path = File('saturn.jpg')
    
    image = Property(Instance(ImageResource), depends_on=['path'])
    @cached_property
    def _get_image(self):
        return ImageResource(self.path)
    
    view = View(
        Item('image',
            editor=ImageEditor(
                scale=False,
                preserve_aspect_ratio=True,
                allow_upscaling=True),
            springy=True,
            show_label=False,
            visible_when='image_file != ""'),
        scrollable=True,
        resizable=True,
    )

class ImageViewerPane(TraitsTaskPane):
    
    model = Instance(ImageViewer, ())
    
    view = View(
        Item('image',
            editor=ImageEditor(
                scale=False,
                preserve_aspect_ratio=True,
                ),
            show_label=False,
            visible_when='image_file != ""'),
        scrollable=True,
        resizable=True,
    )


if __name__ == '__main__':
    f = ImageViewer(image_file='/Users/cwebster/plot1.png')
    f.edit_traits()
