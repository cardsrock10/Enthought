""" Demo for the 'Preprocessing Exercises' notebook.

Quick-and-dirty demo for giving an intuition of the principal components of
faces. The script opens a window showing the average face from the Olivetti
dataset. The user can use sliders to interactively add principal components
to the mean face.

The 'Random face' button generates a random face by applying a random mix
of the first principal components to the average face.
"""

import numpy as np

from sklearn import datasets
from sklearn import decomposition

from chaco.api import ArrayPlotData, gray, Plot
from enable.api import ComponentEditor
from traits.api import (Array, Button, HasStrictTraits, Instance,
    on_trait_change, Property, Range)
from traitsui.api import Item, View


dataset = datasets.fetch_olivetti_faces(shuffle=True, random_state=34)
faces = dataset.data

pca = decomposition.PCA(n_components=0.95, whiten=False)
pca.fit(faces)
transformed = pca.transform(faces)

mean = pca.mean_
components = pca.components_
scales = np.sqrt(pca.explained_variance_)


class FaceViewer(HasStrictTraits):

    plot_data = Instance(ArrayPlotData)

    plot = Instance(Plot)

    random_face = Button

    face = Property(Array, depends_on='coefficients')

    coefficients = Property(Array, depends_on='c0,c1,c2,c3,c4,c5,c6,c7')

    # Individual normalized coefficients.
    c0 = Range(-3.0, 3.0, 0.0)
    c1 = Range(-3.0, 3.0, 0.0)
    c2 = Range(-3.0, 3.0, 0.0)
    c3 = Range(-3.0, 3.0, 0.0)
    c4 = Range(-3.0, 3.0, 0.0)
    c5 = Range(-3.0, 3.0, 0.0)
    c6 = Range(-3.0, 3.0, 0.0)
    c7 = Range(-3.0, 3.0, 0.0)

    def _random_face_fired(self):
        self.coefficients = np.random.normal(size=8)

    def _get_coefficients(self):
        return np.array(
            [self.c0, self.c1, self.c2, self.c3,
             self.c4, self.c5, self.c6, self.c7])

    def _set_coefficients(self, coeffs):
        self.c0, self.c1, self.c2, self.c3, self.c4, \
            self.c5, self.c6, self.c7 = coeffs

    def _get_face(self):
        return (mean + np.dot(
            scales[:8] * self.coefficients, components[:8])).reshape(64, 64)

    def _plot_data_default(self):
        plot_data = ArrayPlotData(face=self.face)
        return plot_data

    def _plot_default(self):
        plot = Plot(self.plot_data)
        plot.img_plot('face', origin="top left", colormap=gray)
        return plot

    @on_trait_change('face')
    def _update_plot_data_on_face_change(self):
        self.plot_data.set_data('face', self.face)

    traits_view = View(
        Item('plot', editor=ComponentEditor()),
        Item('random_face'),
        Item('c0'),
        Item('c1'),
        Item('c2'),
        Item('c3'),
        Item('c4'),
        Item('c5'),
        Item('c6'),
        Item('c7'),
        resizable=True,
    )


if __name__ == '__main__':
    viewer = FaceViewer()
    viewer.configure_traits()
