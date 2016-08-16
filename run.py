import csv
import requests

def get_urls_from_csv(urls_location):
    """Accepts a single column .csv file and returns it as a list"""
    with open(urls_location, 'r') as f:
        reader = csv.reader(f)
        urls_list = []
        for row in reader:
            urls_list.extend(row)

    return(urls_list)

def archive_url(url):
    """takes the given URL and begins the Archive.org Way Back Machine Archiving Process"""
    endpoint = 'https://web.archive.org/save/'
    target = endpoint + str(url)

    r = requests.get(url=target)
    if r.status_code == 200:
        print(str(url) + " has bee archived")
    else:
        print("There was an error when attempting to archive " + str(url))

if __name__=="__main__":

    # location of a single column .csv file containing the URLs you want to archive
    urls_location = 'urls.csv'

    urls_list = get_urls_from_csv(urls_location)

    for url in urls_list:
        archive_url(url)