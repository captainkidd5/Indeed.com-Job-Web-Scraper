import requests
import sys

from bs4 import BeautifulSoup


def printResults():
    
    text_file.write('TITLE: ' + title_elem.text.strip() + '\n')
    text_file.write('SALARY: ' + salary_elem.text.strip() + '\n')
    text_file.write('REQUIREMENTS: ')
    for requirement_elem in requirements_elem_list:
        if None in (requirement_elem):
            continue

        text_file.write(requirement_elem.text.strip())
    if(link_elem != None):
            text_file.write('\n' + 'APPLY:')
            text_file.write('www.indeed.com' + link_elem['href'].strip() + '\n')

    text_file.write("\n \n")


State = sys.argv[1].upper()
City = sys.argv[2].capitalize()
number_of_pages_to_search = int(sys.argv[3])

URL = 'https://www.indeed.com/l-' + City + ',-' + State + '-jobs.html'

page_index = 10
page_num = 0

with open("Output.txt", "w") as text_file:
    
    while(page_num < number_of_pages_to_search):
        text_file.write('RESULTS FOR PAGE ' + str(page_num) + '\n')
        text_file.write('----------------------------------' + '\n')
        page_num = page_num + 1
        page = requests.get(URL)

        if(page.status_code != 200):
            break
        soup = BeautifulSoup(page.content,'html.parser')
        results = soup.find(id='resultsCol')

        job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

        for job_elem in job_elems:
            title_elem = job_elem.find('h2', class_='title')


            link_elem = title_elem.find('a',href = True)
        


            salary_elem = job_elem.find('div', class_='salarySnippet')
            requirements_elem_list = job_elem.find_all('div', class_='jobCardReqItem')
        
            if None in (title_elem, salary_elem,requirements_elem_list):
                continue

            if(len(sys.argv) > 4):
                if(sys.argv[4].lower() in title_elem.text.lower()):
                    printResults()
                else:
                    text_file.write('End of results found for: ' + sys.argv[4])
                    break
            else:
                printResults()
    
        URL = 'https://www.indeed.com/jobs?q=&l=' + City + '%2C+' + State + '&start=' + str(page_index)
        page_index = page_index + 10
        
        
print('END OF FILE')
    






