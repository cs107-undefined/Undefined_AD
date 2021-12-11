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

- Our design of the software is friendly for the users in command-line interaction, and our codes are well encapsulated and modularized.

Implementation of the ``forward`` and ``reverse`` mode (extended feature) to automatically calculate derivative.

In the extended feature, our package can build computational graphs in the ``reverse`` mode.

Link to the project on `Github page <https://github.com/cs107-undefined/cs107-FinalProject>`_.

Link to the package on `PyPI <https://pypi.org/project/undefined-AD/>`_.


.. toctree::
   :maxdepth: 3
   :caption: Introduction and Background

   about


.. toctree::
   :maxdepth: 3
   :caption: Getting started


   usage


.. toctree::
   :maxdepth: 3
   :caption: Software Organization

   organization


.. toctree::
   :maxdepth: 3
   :caption: Implementation

   implementation

.. toctree::
   :maxdepth: 3
   :caption: Broader Impact and Future Directions

   statement


.. toctree::
   :maxdepth: 3
   :caption: Code details

   modules


Licensing
-----------
We will use the ``MIT`` license for open source software development so that other people who are interested in our software will have access to contribute. 

Reason for our choice: We want it to be simple and permissive.
Under the ``MIT`` license, anyone can contribute to this project by adding functionality, debug, or customize it to meet their needs. 
Please see the ``LICENSE`` file in your github for details.

..
   Search
   ==================
   * :ref:`search`
