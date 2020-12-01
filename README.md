# ASB developer codes user manual

## Getting Started Tutorial

This tutorial will walk through the creation and execution of a simple workflow in the Automated Service Builder (ASB), which can serve as a starting template for future workflows.

### Introduction

The ASB interface is built around the concept of creating processes and workflows. 
A process can be viewed as a sort of "unit of work", a building block that has inputs/outputs and does an elementary part of the work.
Each process runs it's own docker container.
By connecting the appropriate outputs to inputs between a set of processes, one can create workflows.
A workflow can then be executed on the uderlying cluster.

In this example the maximum normalized difference vegetation index (NDVI) will be calculated. 
The formula for NDVI is (B8-B4)/(B8+B4), where the input bands B4 is the red and B8 of the near-infrared part of the reflectance spectrum. 
The inputs will be taken from the Sentinel L2A observations and NDVI needs to be computed at every pixel in the area of interest. 
Finally the max NDVI image is obtained by taking the maximum over a given time period.   

### Pre-requisites

You have read the following parts of the documentation:

* nomenclature: [https://mep-wps.vgt.vito.be/docs/user/index.html#definitions-and-acronyms](https://mep-wps.vgt.vito.be/docs/user/index.html#definitions-and-acronyms)
* how to manage processes: [https://mep-wps.vgt.vito.be/docs/user/index.html#processes-management](https://mep-wps.vgt.vito.be/docs/user/index.html#processes-management)
* how to manage workflows: [https://mep-wps.vgt.vito.be/docs/user/index.html#workflows-management](https://mep-wps.vgt.vito.be/docs/user/index.html#workflows-management)

And at least basic knowledge of Python language, since the codes used in this tutorial are written in Python.
 
### What are we going to do

The straightforward approach is to first query the sources, then compute NDVI in a distributed fashion and finally combine the parts together using maximum function. 
Within the ASB interface this requires five processes:

1. Product query: obtains the list of the corresponding B4 and B8 image pairs
1. Dynamic splitter: parallelizes the work based on the query results and launches the NDVI calculators
1. NDVI calculator: computes NDVI over an image pair
1. Joiner: waits for all NDVI calculators to finish
1. Collect_and_max: combines the outputs of the NDVI calculators 

### Creating/reusing the processes

Login to the portal: [https://mep-wps.vgt.vito.be](https://mep-wps.vgt.vito.be)

The advantage of the process/workflow system is the reusability of the processes in many different workflows. In fact 3 out of the 5 processes are readily available. 
The product_query, dynamic list splitter and the oin processes will be reused.

#### Product query

As mentioned, one does not have to implement the search, rather reuse the query_product process developed by VITO.
It can be used to search in the Terrascope database [terrascope.be](terrascope.be) provided by VITO.
Given the area of interest in WKT string, the date range, collection id and band names it returns a list of strings, which describe the location of the images on the file system.

<span style="color:red"> TESTCOLOR </span>

Due to the current limitation on the length of the strings in the list (imposed by the splitter), the strings are encoded as follows:

    /path/to/data/S2B_20180605T105029_31UFS_TOC-B0+4_10M_V200.tif+8_10M_V200.tif

This string has to be split at '+' characters and the first entry is the common prefix of the rest of the array.
In this case this represents a list of two files:

    /path/to/data/S2B_20180605T105029_31UFS_TOC-B04_10M_V200.tif
    /path/to/data/S2B_20180605T105029_31UFS_TOC-B08_10M_V200.tif

LIST INPUTS

#### Dynamic list splitter

This is also a builtin process that takes an array of strings as json. It splits up the array and indepenently launches the next process in the chain. 
Note that the splitter is a smart process in terms of resource management. 
For example if 10 cpus available and each process is using 2, but the split yields to 50 processes: the splitter ensures that 5 processes willbe running concurrently.

#### Compute NDVI

This process has to be developed since it contains our 'business logic'. 
Let's implement it in the following fashion:
* load B4 and B8 into xarrays
* using the area of interest WKT, restrict  

#### Joiner

Again, this is a builtin pocess. 
It waits until all the upstream dynamic processes finish and puts 'success' on its single output in case of no failures.

#### collect_and_max

With a big modifications this process could be generalized into a 'temporal max' function.

### Assembling the workflow