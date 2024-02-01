#Dikshya Panta
#Quiz 5

import arcpy
import os

list_of_paths = []

root_path  = "C:\\Users\\dzp0089\\Desktop\\GIS Programming\\Quiz5_data"

for subdir, dirs, files in os.walk(root_path):
    for file in files:
        if file.endswith('edges.shp'):
            list_of_paths.append(os.path.join(subdir, file))

result_path = "C:\\Users\\dzp0089\\Desktop\\GIS Programming\\results\\merged_counties.shp"

#calculating length of roads in each counties--one by one
#lee county
with arcpy.da.SearchCursor(list_of_paths[0], 'length') as cursor:
    # for every row in the shapefiles attribute table
    lee_roads_len_sum=0 #initializing counter
    for row in cursor:
        lee_roads_len_sum += row[0] #adding up the values
    print("Total length of roads in Lee county is: "+str(lee_roads_len_sum))

#macon county
with arcpy.da.SearchCursor(list_of_paths[1], 'length') as cursor:
    # for every row in the shapefiles attribute table
    macon_roads_len_sum=0
    for row in cursor:
        macon_roads_len_sum += row[0]
    print("Total length of roads in Macon county is: "+str(macon_roads_len_sum))

#russell county
with arcpy.da.SearchCursor(list_of_paths[2], 'length') as cursor:
    # for every row in the shapefiles attribute table
    russell_roads_len_sum=0
    for row in cursor:
        russell_roads_len_sum += row[0]
    print("Total length of roads in Russell county is: "+str(russell_roads_len_sum))


#now merging all counties shapefile into one shapefile

arcpy.Merge_management(list_of_paths, result_path)
print("merging passed")

#calculating length of roads in merged shapefile i.e. toal length of roads in all counties
with arcpy.da.SearchCursor(result_path, 'length') as cursor:
    # for every row in the shapefiles attribute table
    merged_roads_len_sum=0
    for row in cursor:
        merged_roads_len_sum += row[0]
    print("Total length of roads in all counties is: "+str(merged_roads_len_sum))

