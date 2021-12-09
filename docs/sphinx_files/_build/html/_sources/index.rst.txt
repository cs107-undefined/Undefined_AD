.. Undefined - an automatic differentiation tool documentation master file, created by
   sphinx-quickstart on Fri Dec  3 16:56:55 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Undefined - an automatic differentiation tool's documentation!
===========================================================================

..
   Authors: Xinran Tang, Renhao Luo, Chelse Swoopes, Shijia Zhang

Features
--------

Be awesome and fast automatic differentiation calculation!!!

- We utilized the dual number approach in the forward mode to achieve fast computation. 

- In the reverse mode, we implemented a two-step approach to recover the partial derivative, and eventually trace backwards for the final derivative results. For details about the implementation, refer to our *implementation* section.

Implementation of the ``forward`` and ``reverse`` mode to automatically calculate derivative.

Build computational graphs in the ``reverse`` mode.

Link to the project `Github page <https://github.com/cs107-undefined/cs107-FinalProject>`_.

About
----------------------------------

.. toctree::
   :maxdepth: 3

   about

Getting started
---------------------------------

.. toctree::
   :maxdepth: 3

   usage


Software Organization
-----------------------
.. toctree::
   :maxdepth: 3

   organization


Implemetation
---------------
.. toctree::
   :maxdepth: 3

   implementation



Source Code Details
---------------------

.. toctree::
   :maxdepth: 3

   modules


Licensing
-----------
We will use the ``MIT`` license for open source software development so that other people who are interested in our software will have access to contribute. 

Reason for our choice: We want it to be simple and permissive.
Under the ``MIT`` license, anyone can contribute to this project by adding functionality, debug, or customize it to meet their needs. 
Please see the ``LICENCE`` file in your github for details.

..
   Search
   ==================
   * :ref:`search`
