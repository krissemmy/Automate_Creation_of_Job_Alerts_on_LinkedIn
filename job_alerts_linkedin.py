from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
import numpy as np

def create_alert():
    """
    Automates the creation of job alerts on LinkedIn for specified job titles and companies.

    Note:
    - Replace 'your_email' and 'your_password' with your LinkedIn credentials.
    - Prepare the 'company_list.xlsx' file with a column 'Company name' containing the names of companies.

    """
    option = Options()

    # Add an option to disable website notifications
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    # Add an option to disable the "Chrome is being controlled by automated test software" notification
    option.add_argument("--disable-infobars")
    
    # If your chromedriver is in a different directory yo can uncomment line 29 and add the path to the chromedriver, also uncomment line 31 so that the service argument will be added
    #service = ChromeService(executable_path="/home/krissemmy/Downloads/chromedriver-linux64/chromedriver")

    driver = webdriver.Chrome(options=option)#, service=service)
    # driver = webdriver.Firefox()
    website = 'https://www.linkedin.com/uas/login'
    driver.get(website)
    driver.maximize_window()
    time.sleep(5)

    # Replace 'email_or_num' with your email or phone number, and 'your_password' wiith your password which are your LinkedIn credentials
    # Also replace the number of Dataframes you want your original list to be broken down to
    email_or_num = "chrisemma2005@gmail.com"
    password = "asdfghjkl6789"
    parts = 3

    # Locate the email input field and enter the LinkedIn email/username
    email_input = driver.find_element(By.XPATH, '//*[@id="username"]')
    email_input.send_keys(email_or_num)
    time.sleep(2)

    # Locate the password input field and enter the LinkedIn password
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)
    time.sleep(3)

    # Click the 'Sign in' button to log in to LinkedIn
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    time.sleep(20)

    # Go to the 'Jobs' section on LinkedIn
    jobs = driver.find_element(By.XPATH, '//header/div/nav/ul/li[3]/a')
    jobs.click()
    time.sleep(5)

    # List of job titles for which job alerts will be set
    job_titles = ["Data Engineer", "BI Developer", "Data Scientist", "BI Analyst", "Data Analyst"]

    # The first job title to start with
    first_job = job_titles[0]

    # Read the company names from the 'company_list.xlsx' file
    file_name = 'company_list.xlsx'
    df = pd.read_excel(file_name)
    df1 = df['Company name']
    # Split the dataframe into dataframes, the number of times specified in the 'parts' variable
    dfs = np.array_split(df1, parts)

    time.sleep(5)
    # Locate the job title input field and enter the first job title
    title = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
    title.send_keys(first_job)
    title.send_keys(Keys.ENTER)
    time.sleep(5)

    for n, df_part in enumerate(dfs):
        # Locate the job title input field and enter the first job title
        title = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
        title.clear()
        time.sleep(1)
        title.send_keys(first_job)
        title.send_keys(Keys.ENTER)
        time.sleep(3)

        # Locate the location input field and enter "Worldwide" to search for jobs globally
        location = driver.find_element(By.XPATH, '//header/div/div/div/div[2]/div[2]/div/div/input[1]')
        location.clear()
        time.sleep(1)
        location.send_keys("Worldwide")
        location.send_keys(Keys.ENTER)
        time.sleep(3)
        for i in df_part:
            # Locate the 'Companies' button and click it to search for companies
            companies = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/span/button')
            companies.click()
            time.sleep(3)

            # Locate the input field to enter the company name and search for the company
            input_c = driver.find_element(By.XPATH, '//div/div/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[1]/div/div/input')
            input_c.clear()
            input_c.send_keys(i)
            time.sleep(2)

            # Use the 'ActionChains' to select the first company from the search results
            actions = ActionChains(driver)
            actions.pause(1).key_down(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ENTER).perform()
            time.sleep(2)

            # Close the company search popup
            close = driver.find_element(By.XPATH, '//div/section/div/div/div/ul/li[5]/div/div/div/div[1]/button')
            close.click()
            time.sleep(2)

        # Click the 'Companies' button again to see the selected companies
        companies = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/span/button')
        companies.click()
        time.sleep(3)

        # Click the 'Show jobs' button to see all jobs for the selected company and job title
        show_jobs = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]')
        show_jobs.click()
        time.sleep(3)

        # Click the 'Create alert' button to set a job alert for the selected company and job title
        create_alert = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/header/div[2]/div/div')
        create_alert.click()
        time.sleep(3)

        # Loop through the remaining job titles to set alerts for each of them
        for job_t in job_titles[1:]:
            j_title = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[1]/div/div/input[1]')
            j_title.clear()
            time.sleep(2)
            j_title.send_keys(job_t)
            j_title.send_keys(Keys.ENTER)
            time.sleep(6)
            try:
                create_alert = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/header/div[2]/div/div')
                create_alert.click()
                time.sleep(3)
            except:
                print(f"For the {n} company list, No Matching jobs found for {job_t}")

        # Refresh the 'Jobs' page to set alerts for the next batch of companies
        refresh_jobs = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[3]/a')
        refresh_jobs.click()
        time.sleep(5)

    # Close the browser
    driver.quit()
    print("Success!")

# Call the 'create_alert' function to start setting job alerts on LinkedIn
create_alert()