# Football Players Salary Web Scraping

This project aims to scrape football players' salary data from the Salary Sport website using Scrapy. The scraped data includes the players' names, weekly wages, monthly wages, ages, positions, and countries. The data is then saved into a CSV file and uploaded to both MongoDB and ScrapyHub for further analysis and access.

## Overview

Football player salaries are a topic of interest for many fans and stakeholders in the football industry. By scraping salary data from the Salary Sport website, we can gain insights into the earnings of various players across different leagues and teams.

## Requirements

To run the web scraping script, you will need:

- Python 3.x
- Scrapy
- MongoDB (optional)
- ScrapyHub account (optional)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/FaeyO/webscrapping-salarysport.com-website.git
cd football_salary
```

2. Install the required Python packages:

```bash
pip install scrapy pymongo
```

## Usage

1. Navigate to the project directory and run the Scrapy spider:

```bash
cd football_salary
scrapy crawl salaries
```

2. The scraped data will be saved into a CSV file named `football_players_salary.csv`.

3. Optionally, if you have MongoDB installed, you can configure the settings in `settings.py` to save the data to a MongoDB database.

4. Additionally, if you have a ScrapyHub account, you can deploy the spider to ScrapyHub for scheduled scraping and access to the scraped data via API.

## Process Explanation

1. **Scraping**: The Scrapy spider (`salaries.py`) navigates through the Salary Sport website, extracting relevant information such as player names, wages, ages, positions, and countries.

2. **Data Storage**: The scraped data is stored locally in a CSV file (`football_players_salary.csv`). Optionally, it can be saved to a MongoDB database for more efficient querying and management.

3. **Deployment**: The spider can be deployed to ScrapyHub, a cloud-based platform for running and managing web crawlers. This allows for scheduled scraping and easy access to the scraped data via APIs.

## Conclusion

Scraping football player salary data from the Salary Sport website provides valuable insights for stakeholders in the football industry. By leveraging Scrapy and other tools, we can automate the process of collecting and analyzing this data, enabling informed decision-making and research.

Feel free to contribute to this project by improving the scraping logic, adding new features, or exploring additional sources of football player salary data.

**Note:** Ensure compliance with the website's terms of service and legal regulations when scraping data.

### website view

![image](https://github.com/FaeyO/webscrapping-salarysport.com-website/assets/118575325/eab9e073-dde4-4fb8-8b7b-65bb782ca325)
