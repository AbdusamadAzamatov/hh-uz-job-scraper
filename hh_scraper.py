import requests
from bs4 import BeautifulSoup
import json


headers = {         
         
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "__ddg1_=7ondZqL8UZs7luo6gIGX; _xsrf=a0bca09646f1a2278a7dbb80567b8cb3; redirect_host=tashkent.hh.uz; hhtoken=kb6_Ou6eeJycnAUMnDAvAuhPDxVT; hhuid=llTYgg3BsNoUS2RHqUEydQ--; hhrole=anonymous; regions=2759; region_clarified=NOT_SET; display=desktop; GMT=5; _ym_uid=1682417990138523634; _ym_d=1682417990; _gid=GA1.2.1020669329.1682417990; _ym_isad=2; __zzatgib-w-hh=MDA0dBA=Fz2+aQ==; __zzatgib-w-hh=MDA0dBA=Fz2+aQ==; device_magritte_breakpoint=s; total_searches=3; _ga_LGX55EQH2G=GS1.1.e560331ad0f6aac8d71ef4ad74d43973c904b9ec4b1550680af50e6bab376e73.1.1.1682418498.60.0.0; _ga=GA1.1.2102430221.1682417990; device_breakpoint=s; cfidsgib-w-hh=pzA3ZaKyri2wTQ+0kmh01+C4XW1SdY2K6bDqR2wU5Se7ZmlP23xcFcJabUBmXpTuPL5UvCtujRrPbvizcmxpCT3nmnjXqiPTsZ96paQYNSj2vGw6sRjui+zw3MFnRkjKFiS7rNiSujJKR8ilBB87A9KSgWf4+PY4w+FaBQ==; gsscgib-w-hh=XbZQu1NwXdcHWCYWMgku8wWs5h+25LPSZhZQ+TxIFisKlLpjnjxSNooB4tk0g0PHuzNvfEvFenF6xOD2QDv6iZkGgw8WD2L2QKs2b3LBeG0D7hDwbSfPby60fMh/7IJhpvADDorTTtdwCtAPhRvO2wfOeXwAHr/VySStgKEG4MbAIm05ZZYSMeRNs9ZwUBbw1NUwrclGgO6CpbiOs0y339Fg38dDEGX4OhhlmktbKBxRl06HH/lavxEZ4jKJJPQ=; gsscgib-w-hh=XbZQu1NwXdcHWCYWMgku8wWs5h+25LPSZhZQ+TxIFisKlLpjnjxSNooB4tk0g0PHuzNvfEvFenF6xOD2QDv6iZkGgw8WD2L2QKs2b3LBeG0D7hDwbSfPby60fMh/7IJhpvADDorTTtdwCtAPhRvO2wfOeXwAHr/VySStgKEG4MbAIm05ZZYSMeRNs9ZwUBbw1NUwrclGgO6CpbiOs0y339Fg38dDEGX4OhhlmktbKBxRl06HH/lavxEZ4jKJJPQ=; cfidsgib-w-hh=sLOCNwSElYNzHXzPj0711dUtDTkRl8j4HXzVmYDXIHkGHo09oFHjdVxlFgjY4Dc3ZDtMEiRHXFmY2XypuDnDTLX0f72YsRNXOr8jm3MBNqlybsU55nPys7jPTo1uf4TSo3dOdAPTLjuv0RrRQNcKLsRjrb3iGWUNW/gorw==; cfidsgib-w-hh=sLOCNwSElYNzHXzPj0711dUtDTkRl8j4HXzVmYDXIHkGHo09oFHjdVxlFgjY4Dc3ZDtMEiRHXFmY2XypuDnDTLX0f72YsRNXOr8jm3MBNqlybsU55nPys7jPTo1uf4TSo3dOdAPTLjuv0RrRQNcKLsRjrb3iGWUNW/gorw==; fgsscgib-w-hh=NAnba619ee05aa3295d1704be942a3f68db09876; fgsscgib-w-hh=NAnba619ee05aa3295d1704be942a3f68db09876",
        "dnt": "1",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Microsoft Edge\";v=\"112\", \"Not:A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"                                                                                         
    }

def get_data():
    """
    Scrapes the job vacancy URLs from the hh.uz website for Tashkent city, Uzbekistan.
    
    Returns:
        None. The URLs are written to a JSON file called 'urls.json' in the current working directory.
        
    Raises:
        None. However, if the request to the website returns a status code other than 200, no data is scraped.
    """
        
    base_url = 'https://tashkent.hh.uz/search/vacancy?text=&area=2759&page={}'
    

    req = requests.get(base_url, headers=headers)
    if  req.status_code != 200:
        return
    soup = BeautifulSoup(req.text, 'lxml')    

    num_pages = int(soup.find("div", class_="pager").find_all("span",recursive=False)[-1].find("a").find("span").text)

    urls = []

    for page_num in range(num_pages):
    # Make a request to the page URL
        url = base_url.format(page_num)
        response = requests.get(url, headers=headers)
    
    # Parse the HTML content using BeautifulSoup
        soup1 = BeautifulSoup(response.content, 'lxml')
    
    # Find all the links on the page and append them to the list
        for link in soup1.find_all('a', href=True):
            link_url = link.get('href')
            if link_url.startswith('https://tashkent.hh.uz/vacancy/'):
                urls.append(link_url)


    # Write the URLs to a JSON file
    with open('urls.json', 'w') as f:
        json.dump(urls, f)

    

def parse_response():
    """
    Parses the HTML content of each URL in the 'urls.json' file and extracts relevant job information.

    """

    with open('urls.json', 'r', encoding='UTF-8') as f:
        urls = json.load(f)

    
    
        job_listings = []
        counter = 0

        for url in urls:        
            if counter >= 30:
                # Write the first 30 job listings to a JSON file
                # Modify this number to scrape more or less job listings
                break

            response = requests.get(url, headers=headers)
            try:
                soup = BeautifulSoup(response.text, 'lxml')
                vacancies = soup.find("div", class_="main-content")
                vacancy_data = {}

                if vacancies.find("h1", attrs={"data-qa": "vacancy-title"}):
                    vacancy_data['Job Title'] = vacancies.find("h1", attrs={"data-qa": "vacancy-title"}).text.replace("\u202f", " ")
                else:
                    vacancy_data['Job Title'] = None
                
                if vacancies.find("span",attrs={"data-qa":"vacancy-experience"}):
                    vacancy_data['Employement Type and Schedule'] = vacancies.find("p",attrs={"data-qa":"vacancy-view-employment-mode"}).text.strip().replace("\u202f", " ")
                else:
                    vacancy_data['Employement Type and Schedule'] = None

                if vacancies.find("div", attrs={"data-qa": "vacancy-salary"}):
                    vacancy_data['Salary'] = vacancies.find("div", attrs={"data-qa": "vacancy-salary"}).text.replace("\u202f", " ")
                else:
                    vacancy_data['Salary'] = None

                if vacancies.find("a", attrs={"data-qa":"vacancy-company-name"}):
                    vacancy_data['Company Name'] = vacancies.find("a",attrs={"data-qa":"vacancy-company-name"}).find("span").text.strip().replace("\u202f", " ")
                else:
                    vacancy_data['Company Name'] = None

                if vacancies.find("span",attrs={"data-qa":"vacancy-experience"}):
                    vacancy_data['Years of Experience Required'] = vacancies.find("span",attrs={"data-qa":"vacancy-experience"}).text.strip().replace("\u202f", " ")
                else:
                    vacancy_data['Years of Experience Required'] = None

                if vacancies.find("div", class_="bloko-tag-list"):
                    skills = [tag.span.text.strip() for tag in vacancies.find("div", class_="bloko-tag-list").find_all("div")]
                    vacancy_data['List of Skills Required'] = ', '.join(skills)
                else:
                    vacancy_data['List of Skills Required'] = None

                if vacancies.find("span",attrs={"data-qa":"vacancy-view-raw-address"}):
                    vacancy_data['Job Location'] = vacancies.find("span",attrs={"data-qa":"vacancy-view-raw-address"}).text.strip().replace("\u202f", " ")
                else:
                    vacancy_data['Job Location'] = None

                if vacancies.find("p", class_="vacancy-creation-time-redesigned"):
                    vacancy_data['Date Posted'] = vacancies.find("p", class_="vacancy-creation-time-redesigned").text.strip().replace("\u202f", " ")
                else:
                    vacancy_data['Date Posted'] = None

                if vacancies.find("div", class_="g-user-content"):
                    vacancy_data['Job Description'] = vacancies.find("div", class_="g-user-content").text.strip().replace("\u202f", " ")
                else:
                    vacancy_data['Job Description'] = None

                """if only logged in"""
                # vacancy_data['Contact Email'] =soup.find(
                # "div",attrs={"data-qa":"vacancy-contacts__fio"}).text.strip()
                vacancy_data['Source'] = 'hh.uz'

                job_listings.append(vacancy_data)

                with open('hh_uz.json', 'w', encoding='UTF-8') as f:
                    json.dump(job_listings, f, ensure_ascii=False, indent=4)

                #print(vacancy_data)

            except Exception as e:
                print(e)
                print("Error occured with URL: {}".format(url))
        

def get_job_data():
    """
    Loads the JSON file containing the job data and returns a list of dictionaries.

    """

    
    with open('hh_uz.json', 'r', encoding='UTF-8') as f:
        job_listings = json.load(f)
        
    # create a list of Oneapp-formatted job data
    oneapp_data_list = []
    for job_data in job_listings:
        oneapp_data = match_fields(job_data)
        oneapp_data_list.append(oneapp_data)

    # write the Oneapp-formatted job data to a JSON file
    with open('oneapp_jobs.json', 'w', encoding='UTF-8') as f:
        json.dump(oneapp_data_list, f, ensure_ascii=False, indent=4)


def match_fields(job_data):
    """
    Matches the fields in the job_data to the fields in the Oneapp job template.

    """
    oneapp_data = {}
    oneapp_data['Job Title'] = job_data['Job Title']  # add your code to get this data from the job_data
    oneapp_data['years of experience required'] = job_data['Years of Experience Required']
    oneapp_data['job description'] = job_data['Job Description']
    oneapp_data['Salary'] = job_data['Salary']  # add your code to get this data from the job_data 
    oneapp_data['Employement type'] = job_data['Employement Type and Schedule']
    oneapp_data['Description'] = job_data['Job Description']

    # create a list of skills needed for each job and add it to the oneapp_data
    skills = []
    if job_data['List of Skills Required']:
        skills = [s.strip() for s in job_data['List of Skills Required'].split(',')]
    oneapp_data['Skills'] = skills

    return oneapp_data

            

    


def main():
    """
    Main function that calls the other functions.
    
    """
    #get_data()
    parse_response()
    get_job_data()



if __name__ == '__main__':
    main()
