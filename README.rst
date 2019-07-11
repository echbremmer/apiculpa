Apiculpa
===============
A simple way to run an API that behaves in a configurably poor manner. It is designed to help your application handle API calls correctly even if they do not behave very well. 

Installation
------------
.. code-block:: console

  $ git clone https://github.com/echbremmer/apiculpa.git
  
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
To start an API with some default unreliability simply run following command with the
provided example json as data that the api will return.

.. code-block:: console

  $ apiculpa examples/culpa.json

To specify the unreliability you would like the API to have you can provide these as 
options:

.. code-block:: console

  -F, --failrate INTEGER       The chance that the API will not respond to a
                               request. E.g. a value of 10 will result in the
                               api having a 10% chance of not responding.
  -L, --latency INTEGER        The number of milliseconds that the API will wait
                               before sending a response.
  -R, --latency-range INTEGER  The latency is randomly increased upto the given
                               milliseconds
  -P, --port INTEGER           Port where the API will be listening
  -H, --host TEXT              Host of the API

.. code-block:: console

  $ apiculpa examples/culpa.json --latency=5000 --latency-range=2500 --failrate=30

Limitations / TODO
------------------
There are some limitations in its current form. Feel free to contribute by means of a pull request:

* Multithreading is not supported so this tool cannot be used for load/stress testing.

* Mimicking functional and server side errors (e.g. receiving a 4xx or 5xx) is not supported currently (failrate will drop the connection to the API)

* Responses from the API are either hardcoded (e.g. headers and http response codes) or based on a static file that is read during loading of the script (body). 

Naming
------
Derived from the Latin "Mea Culpa":

.. code-block:: text

*Mea culpa is a Latin phrase that 
means "through my fault" and is an 
acknowledgement of having done wrong.*

Source `wikipedia`_

.. _wikipedia: https://en.wikipedia.org/wiki/Mea_culpa
