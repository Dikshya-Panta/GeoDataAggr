# GeoDataAggr
Geospatial Data Aggregation Script Assignment
**Overview**

In this assignment, you are tasked with developing a Python script that automates the process of aggregating geospatial data from multiple sources. The script will primarily deal with shapefiles representing road networks within various administrative regions. Your goal is to merge these individual road network layers into a single, comprehensive shapefile, while also calculating and reporting the total road lengths for each region and the combined dataset.

**Objectives**

Data Aggregation: Combine multiple shapefiles into a single shapefile.
Attribute Analysis: Calculate the total length of road networks within each individual shapefile and the merged shapefile.
Automation: Ensure the script can dynamically adapt to different folder structures and file names, requiring minimal user input.

**Requirements**

The script should accept two inputs from the user:

The path to the directory containing the subdirectories of geospatial data.
The path where the output file (merged shapefile) will be saved.
The script must be able to identify and process shapefiles located within subdirectories named "edges", which contain polyline representations of road networks.

The script should calculate the total length of the road networks within each individual shapefile and print this information, followed by the total length of the road networks in the merged shapefile.

The script should be designed to handle different sets of regional data, not limited to predefined names or numbers of regions.
