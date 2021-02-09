RSTED
=====

Simple online editor for reStructuredText on Flask.

This repository contains the necessary modifications to run on Python3
with up-to-date versions of the packages it depends upon. The original
repository at https://github.com/anru/rsted is no longer maintained,
and works only on Python2.

The link to try it online (http://rst.ninjs.org/) is, alas, no longer
working.

Getting setup
-------------

Requirements for rsted:

* Flask
* rst2html (from Docutils)

These requirements are expressed in the pip-requirements.txt file and may be
installed by running the following (from within a virtual environment)::

    pip install -r pip-requirements.txt


How to run
----------

Your Environment
++++++++++++++++
From within your environment, just run::

    ./application.py

This will start a server on port 5000.  Just visit http://localhost:5000/ in
your browser.

Docker
++++++
In a docker installed host, just build and run::

    docker build -t rsted .
    docker run --name rsted --rm -p 5000:5000 rsted

A server starts on port 5000. Please adjust it, if you need another port
by changing run command above. And then just visit http://localhost:5000/ in
your browser.
