Flopy Documentation
===================

This repository contains the flopy documentation, which can be viewed at:

http://modflowpy.github.io/flopydoc/

The actual html files are contained on the gh-pages branch of this repository.  The concept used to create the documentation is described here:

http://daler.github.io/sphinxdoc-test/includeme.html#general-workflow


Build the Documentation
-----------------------

For anyone who is inclined to build this documentation on your own, it can be done.  Here are a few steps that you will need to follow:

  * Everything here assumes that the flopy version 3 repository has been cloned to a folder called flopy3.git.  From a working folder, this can be created using the following command:

git clone git@github.com:modflowpy/flopy3.git

  * Now create a new folder at the same level as flopy3.git.  Call this folder flopy3doc.

  * Change into this folder and setup the main repository by cloning flopydoc.  Use the following command:

git clone git@github.com:modflowpy/flopydoc.git

  * Also create another folder in flopy3doc called flopydoc-doc by executing:

mkdir flopydoc-doc

  * Now change into flopydoc-doc and checkout the flopy documentation into an html folder:

git clone git@github.com:modflowpy/flopydoc.git html

  * Upon checkout into the html folder, the master branch will be selected (type git branch to confirm).  This needs to be changed to the gh-branch:

git checkout -b gh-pages remotes/origin/gh-pages

  * At this point, the directory structure should match the directory structure that was used to create the documentation.  Changes can now be made to flopy3.git by editing the files in that folder and running the following command from flopy3.git/docs:

make html

  * This will update the html files in flopydoc-doc.  Pushing these changes to github will update the documentation served from github.  That's it!

