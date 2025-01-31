import urllib.request
import zipfile

#  create a list of URLs to download each WMA DEM (WMAs 1 through 20)
url_list = []

for i in range(1, 21):
    if i < 10:
        url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma0" + str(i) + "lat.zip")
    else:
        url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma" + str(i) + "lat.zip")

print("Create url_list: Complete. " + str(url_list))

#  create a list of file paths/file names for download
filename_list = []

your_downloads_folder = "C:/Users/bagta/Downloads/"

for i in range(1, 21):
    if i < 10:
        filename_list.append(
            str(your_downloads_folder) + "wma0" + str(i) + ".zip")
    else:
        filename_list.append(
            str(your_downloads_folder) + "wma" + str(i) + ".zip")

print("Create filename_list: Complete." + str(filename_list))

print("Files Downloading to your folder")

#  download all WMA DEMs to the specified file paths
for url_item, filename_item in zip(url_list, filename_list):
    urllib.request.urlretrieve(url_item, filename_item)

print("Download all DEMs: Complete")

#  download the street network file, then append file location to filename_list
urllib.request.urlretrieve(
    "https://www.state.nj.us/transportation/gis/zip/NJ_Roads_shp.zip",
    str(your_downloads_folder) + "NJ_Roads_shp.zip"
    )

print("Create filename_list: Complete. " + str(filename_list))

#  unzip files from the location listed in filename_list into the specified folder (your_project_folder)


def unzip_file(zip_file_name, extract_location):
    zip_object = zipfile.ZipFile(zip_file_name, 'r')
    zip_object.extractall(extract_location)


#  designate the folder where you want to extract the data

your_project_folder = "C:/Users/bagta/Documents/810 Project/"

#  extract the data
for i in range(len(filename_list)):
    unzip_file(
        filename_list[int(i) - 1],
        your_project_folder
    )

print("All Data: Extracted")

