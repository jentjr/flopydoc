Created 12/17/2013
Last modified 12/17/2013 (langevin)
Last modified 04/04/2014 (langevin)
Last modified 11/01/2014


I found this command at:  http://stackoverflow.com/questions/2120844/how-do-i-add-all-new-files-to-svn
This will add all new files to svn.  Seems to work well for me.  It can be run from within the sphinx directory to add all new files within the sphinx folder and its subfolders.
svn st | grep ^? | sed 's/?    //' | xargs svn add

For google code to serve these html pages, the html files need to have the correct propset.  This is done with the following command (from http://code.google.com/p/support/wiki/SubversionFAQ):

svn propset svn:mime-type 'text/html' FILENAME


To build the html files, simply type 'make' at the command line when in the sphinx folder.  You will need to have numpydoc and sphinx installed in order for this to work.

Notes for working with sphinx and flopy.  

Note the following line, which is in conf.py.  The last two entries were added.  Basically, we are using the numpydoc package with sphinx in order to build the html pages.  I looked at Epydoc and generic restructured text but found that numpydoc seemed to give us decent looking pages.

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'numpydoc']

The following are some examples of how to write docstrings.  Presently, the flopy code is pretty bad.  It doesn't conform to PEP8 standards.  Sphinx gives lots of build errors due to these PEP8 violations.

We should strongly consider mangling many of the methods (adding _ before the method name).  If we do this, then those methods won't show up in the sphinx html pages.  User's probably don't need to know about them anyways.

See this website for more numpydoc info: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

class AnyClass(AnySuperClass):
    """
    Docstring goes here. And can continue on the next line, but do not exceed
    79 characters.

    Parameters
    ----------
    i : int
        An integer.
    a : float
        A floating point number.
    b : ndarray
        A numpy array.
    kwargs : dictionary, optional
        xoffset, yoffset and rotation can be provided.

    Returns (not needed for a class)
    -------

    Attributes (can include these for a class, but not required)
    ----------
    xoffset : float
        Offset of grid in x direction.
    yoffset : float
        Offset of grid in y direction.
    rotation : float
        Clockwise rotation angle, in degrees, around lower left corner. Note
        that this does not work yet.

    See Also
    --------
    ModflowGrid

    Notes
    -----

    Examples
    --------

    """
    
    