import urllib.request
from urllib.request import Request, urlopen
import bs4 
from bs4 import BeautifulSoup as soup
import os
import shutil

#build an opener to pass HTTP 403 forbidden
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def craw_image(image_url):
    #take the name of the file from the url link
    filename = image_url.split('/')[-1]
    #download the file 
    try: 
        urllib.request.urlretrieve(image_url, filename)
        print("succesfully craw image, save as :", filename)
    except FileNotFoundError:
        pass
    return filename

def extract_img_tag(url):
    #open a page's url
    page = urllib.request.urlopen(url)
    #find all the <img/> 
    images = soup(page).findAll('img')
    #take its src and alt 
    return images

def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
        print("create new folder in: " + folder_path)
    except FileExistsError:
        pass

def main():
    path = os.getcwd()
    for i in range(1, 3):
        for image in extract_img_tag("https://javmodel.com/jav/homepages.php?page=%d" % i): 

                #make a path for each image 
                image_folder = path + "/" + image['alt']
                create_folder(image_folder)

                #download each image
                image_path = os.path.abspath(craw_image(image['src']))

                #move it to its own folder
                shutil.move(image_path, image_folder)

if __name__ == "__main__":
  main()



