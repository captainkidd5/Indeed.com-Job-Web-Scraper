import requests
import sys

from bs4 import BeautifulSoup


def printResults():
    
    print(title_elem.text.strip())
    print(salary_elem.text.strip())
    for requirement_elem in requirements_elem_list:
        if None in (requirement_elem):
            continue

        print(requirement_elem.text.strip())
    print()
    print()


URL = sys.argv[1]


while(True):
    
    page = requests.get(URL)

    if(page.status_code != 200):
        break
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find(id='resultsCol')

    job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

    for job_elem in job_elems:
        title_elem = job_elem.find('h2', class_='title')
        salary_elem = job_elem.find('div', class_='salarySnippet')
        requirements_elem_list = job_elem.find_all('div', class_='jobCardReqItem')
        
        if None in (title_elem, salary_elem,requirements_elem_list):
            continue

        if(len(sys.argv) > 2):
            if(sys.argv[2].lower() in title_elem.text.lower()):
                printResults()
            else:
                print('End of results found for: ' + sys.argv[2])
                break
        else:
            printResults()
        
        


    
    






