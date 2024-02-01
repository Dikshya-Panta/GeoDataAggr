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

# Script Overview
This Python script is designed to automate the process of aggregating road network data from multiple shapefiles representing different administrative regions into a single, comprehensive shapefile. Additionally, it calculates and reports the total length of road networks for each individual region and for the combined dataset.

**Features**
Dynamic Data Aggregation: Automatically identifies and merges shapefiles from specified subdirectories.
Length Calculation: Calculates the total length of road networks within each shapefile and the merged dataset.
Flexibility: Adapts to different folder structures and file names with minimal user input.
**Prerequisites**
Before running this script, ensure you have the following installed:

Python 3.x
ArcPy (comes with ArcGIS Desktop or ArcGIS Pro)
Access to ArcGIS environment (ArcGIS Desktop or ArcGIS Pro must be installed)
**Setup**
Clone or download this repository to your local machine.
Ensure you have the required software installed (Python and ArcGIS).
Prepare your data directory with subdirectories containing the shapefiles to be processed.
**Usage**
Open the script in a Python IDE or text editor.
Modify the root_path variable to point to your data directory containing the county road shapefiles.
Modify the result_path variable to specify the desired output location and name of the merged shapefile.
Run the script. The console will output the total length of roads for each county and the total length of roads in the merged shapefile.
**Inputs**
root_path: Path to the folder containing subdirectories with the shapefiles.
result_path: Path where the merged shapefile will be saved.
**Outputs**
A single shapefile named as specified in result_path, containing the merged road networks from all input shapefiles.
Console output displaying the total road length for each individual shapefile and the merged dataset.

**Disclaimer**
This script was developed for educational purposes in a graduate-level Geography program.
