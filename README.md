Description: This is a Python script that uses BeautifulSoup4 and lxml to scrape job listings from the website hh.uz. The script extracts information such as job title, company name, job location, years of experience required, job market, contact email, job description, and list of skills required. The scraped data is then stored in JSON format.

Usage: To use the script, you'll need to have Python installed on your machine. To install the necessary libraries, run `pip install -r requirements.txt`. You can run the script from the command line by running the command `python hh.py`. Before running the script, make sure to update the `urls.json` file with the URLs of the job listings you want to scrape.

Efficiency Improvements: The script has been optimized to reduce unnecessary requests and data processing, significantly reducing hardware resource wastage. Error handling has been implemented to manage failed requests or parsing errors gracefully, ensuring the script runs smoothly.

Contributing: Contributions are welcome! If you find any issues with the script, feel free to open a GitHub issue or submit a pull request.

NOTE: Python script will scrap jobs(1000 vacancies) for about 10mins. When you run the code and see empty blanc, it doesn't mean that nothing is happening, it's actually scrapping! 
