Apiculpa
===============
A simple way to run an API that behaves in a configurably poor manner

Installation
------------
.. code-block:: console

  $ git clone https://github.com/echbremmer/Apiculpa.git
  
  $ cd apiculpa
   
  $ python3 -m venv venv
  
  $ . venv/bin/activate
  
  $ pip install .
  
If you are using Python 2 you need to use virtualenv instead of venv

.. code-block:: console

  # Debian, Ubuntu
  sudo apt-get install python-virtualenv

  # CentOS, Fedora
  sudo yum install python-virtualenv

  # Arch
  sudo pacman -S python-virtualenv

Usage
-----
.. code-block:: console

  $ apiculpa examples/culpa.json

This will start the api endpoint with some basic unreliability. To specify 
what unreliability you would like the API to have you can provide these as 
options to the command.

.. code-block:: console

  $ apiculpa examples/culpa.json --latency=5000 --latency-range=2500 --failrate=30


