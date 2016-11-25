DAG simulation tool
===================

* Simulate different scheduling schemes using SimGrid framework.
* Visualize simulations as Gantt charts

Examples
========

TODO


Dependencies
============

C++

* C++11 capable compiler (tested with GCC/G++ 4.8.4)
* SimGrid built with graphviz support (build script provided, tested v3.13) [SimGrid download page](http://simgrid.gforge.inria.fr/download.php)

Python

* python 2.7 or 3.4+
* cython (for full rebuild)
* matplotlib (optional)


Build instructions
==================

Ubuntu 14.04+
-------------

Install system dependencies (list is not full):

```
#!bash

sudo apt-get install libboost-context-dev libboost-program-options-dev libboost-filesystem-dev doxygen graphviz-dev
```

Use provided scripts to get dependencies:

```
#!bash

./get_simgrid.sh
```

Development build (inplace)

```
#!bash

python3 setup.py build_ext --inplace
```

Test the build:

```
#!bash

python3 run_tests.py
```

FAQ
===

1. Where to get platform definition files? They look scary.
-----------------------------------------------------------

SimGrid source distribution contains quite a few of platform examples of different complexity and scale.


2. Where to get some ready DAGs?
--------------------------------

* Pegasus workflows, DAX format  
    * See [Pegasus Workfow Generator](https://confluence.pegasus.isi.edu/display/pegasus/WorkflowGenerator)
    * Direct download (warning: ~400Mb) [[link](https://download.pegasus.isi.edu/misc/SyntheticWorkflows.tar.gz)]


3. What about multi-core tasks?
-------------------------------

They are not supported for now. Two main reasons:

* Existing SimGrid task parsers do not support them, so you need custom task format to even setup this.
* There are some [discouraging words](http://simgrid.gforge.inria.fr/simgrid/3.12/doc/platform.html#pf_Cr) in SimGrid documentation about validity of such simulation.