# Automate_Creation_of_Job_Alerts_on_LinkedIn

## Overview

Ever thought of creating job alerts for lots of companies? Well, this project's objective is to achieve that. As of July 2023, the endpoint URL to create job alerts on LinkedIn using its API has been deprecated. So, Selenium will be utilized to automate the creation of job alerts on LinkedIn, and the best part about this is that you only need your LinkedIn login credentials.

### Files
There are Three files in this repo
- job_alerts_linkedin.py
- company_list.xlsx
- requirements.txt
  
## Requirements

To run this project, you need the following:

- Python (version 3.x)
- Selenium library for Python
- Pandas library for Python
- Google Chrome browser or Firefox (If you choose to use Firefox then comment the line that creates the Chrome session and uncomment the line that creates a session with firefox)
- ChromeDriver (compatible with your Chrome version) OR geckodriver (compatible with your Firefox version)

## Installation

1. Install Python: Download and install Python from the official website: https://www.python.org/downloads/

2. Clone this repository:
```
git clone https://github.com/krissemmy/Automate_Creation_of_Job_Alerts_on_LinkedIn.git
```
3. Create a Virtual environment
```
python -m virtualenv my-venv   
```
4. Activate the virtual environment
```
source my-venv/bin/activate
```
5. Install the required dependencies:
```
pip install -r requirements.txt
```
Depending on the browser you choose to use for chrome follow number 3 instructions, while for Firefox follow number 4.

6.Download ChromeDriver: Download the ChromeDriver executable that matches your Chrome browser version from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads

Extract the geckodriver archive:

On Linux or macOS:
```
# Assuming you downloaded the Chromedriver to the Downloads folder
cd ~/Downloads

# Extract the tar.gz file
tar -xvzf chromedriver-vX.XX.X-linux64.tar.gz
```
On Windows:

Right-click on the downloaded zip file and select "Extract All."

Choose a destination folder for the extracted files (e.g., C:\path\to\chromedriver\).


Move the Chromedriver executable to a suitable location:

On Linux or macOS:
```
# Assuming you want to move chromedriver to /usr/local/bin/
sudo mv chromedriver /usr/local/bin/
```
On Windows:

Open File Explorer and navigate to the folder where you extracted Chromedriver (e.g., C:\path\to\chromedriver\).

Copy the chromedriver.exe file.

Navigate to a suitable directory that is included in your system's PATH (e.g., C:\Program Files\).

Paste the chromedriver.exe file in the chosen directory.

Optional:

To install Chromedriver on Ubuntu, run the below command.There will be no need to carry out the 4th step if you do use the below command.
```
sudo apt install chromium-chromedriver
```
To install Chromedriver on Mac, run the below command.
```
brew install cask chromedriver
```
If you are utilizing an M1 Mac, run the following command instead
```
brew install cask chromedriver-beta
```
To verify that it is installed run the following command:
```
chromedriver --version
```
7. Download Geckodriver: Download the ChromeDriver executable that matches your Chrome browser version from the official website: https://github.com/mozilla/geckodriver/releases . 

Extract the geckodriver archive:

On Linux or macOS:
```
# Assuming you downloaded the geckodriver to the Downloads folder
cd ~/Downloads

# Extract the tar.gz file
tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
```
On Windows:

Right-click on the downloaded zip file and select "Extract All."

Choose a destination folder for the extracted files (e.g., C:\path\to\geckodriver\).


Move the geckodriver executable to a suitable location:

On Linux or macOS:
```
# Assuming you want to move geckodriver to /usr/local/bin/
sudo mv geckodriver /usr/local/bin/
```
On Windows:

Open File Explorer and navigate to the folder where you extracted geckodriver (e.g., C:\path\to\geckodriver\).

Copy the geckodriver.exe file.

Navigate to a suitable directory that is included in your system's PATH (e.g., C:\Program Files\).

Paste the geckodriver.exe file in the chosen directory.

Optional:

To install geckodriver on Ubuntu, run the below command.There will be no need to carry out the 5th step if you do use the below command.
```
sudo apt install firefox-geckodriver
```
To install Chromedriver on Mac, run the below command.
```
brew install geckodriver
```
To verify that it is installed, run the following command:
```
geckodriver --version
```

## Usage
1.Replace 'your_email' and 'your_password' in the code with your actual LinkedIn login credentials.

2.Prepare the company list: Create an Excel file named 'company_list.xlsx' with a column named 'Company name' containing the names of the companies you want to set job alerts for, Or you can use the dfault company names present in the alredy provided excel file available on the repo.

3.Customize job_titles: Modify the 'job_titles' list in the code to include the job titles you want to set alerts for.

4.Run the code: Open your terminal or command prompt, navigate to the directory containing the code file, and run the following command:
```
python job_alerts_linkedin.py

```
5.Sit back and relax: The code will automate the process of setting job alerts for the specified companies and job titles on LinkedIn.

### Handling Duplicate Companies
One limitation of this project is that if multiple companies have the same name but work in different fields/domains, the code will always select the first company that appears when searching for a company. 
To address this issue, the user  should ensure the correct company name is inputed in the excel file, e.g
- "Google" not "goggle"
- "Cloud2, a BNC Group company" not "Cloud2/BNC"

## Contributing
We welcome contributions to this project! If you have any improvements or bug fixes, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact Information
If you have any questions, suggestions, or issues related to the project, you can reach out to the project owner:

- Name: Emmanuel Christopher
- Email: krissemmy17@gmail.com
- LinkedIn: [Profile link](https://www.linkedin.com/in/emmanuel-christopher/)
