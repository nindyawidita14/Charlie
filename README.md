
# About the Project

This project involves developing a prescribing dashboard for Integrated Care Board (ICB) members to monitor the cost management of prescriptions in their GP practices.

# Target Users

Integrated Core Board (ICB) member  

# Aim of the Projects

**Phase 1**: Monitor resource and cost management for various drugs across GP practices

**Phase 2**: Expand dashboard usage to GP practices within the ICB’s catchment area for local management, benchmarking performance, and setting goals by comparing against similar practices and regional averages

# Data Sources
Data sources for the prescribing dashboard are from NHS Digital's Practice Level Prescribing Data. The data is available on the [NHS Digital website](https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-data-more-information).

**Link to prescribing data:  [https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-data-more-information(opens in a new tab)](https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-data-more-information)**

**Explanation of variables used:  [https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-glossary-of-terms(opens in a new tab)](https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-glossary-of-terms)**

**The BNF online:  [https://www.bnf.org/products/bnf-online/](https://www.bnf.org/products/bnf-online/)**

# Documentation of Dashboard Development 
We use agile method during the dashboard development. The agile method use iterative development that consist of plan, build, test, and review. We use the scrum framework as our guidance for conducting the development. 

![Scrum Framework](https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/2023-09/scrum-framework-with-sdo-logo-9.29.23.png)

## Sprint 1 

### User stories

 1. As a Manager, I want to quickly view summary data on the main page to make faster decisions
 2. As a Manager, I want to view how many unique items are in the database to understand the scope of the data
 3. As a Manager I would like written guidance on how to use and maintain the dashboard so that the project can be worked on by others  which will increase its lifespan
 4. As a Manager, I want to see details of the purpose of dashboard and support team contact details, so that it can be useful for future information.

### Features implemented
1. Add the ACT cost to the summary tile at the top of the dashboard
2. Add the number of unique items to the summary tile at the top of the dashboard
3. Add a readme to the GitHub page
4. Add some information to the "About" popup to detail the purpose of dashboard and details of your team and support contact

### Role 
1. Luwa Adeniji-Fasohla - Product Owner
2. Yu Chen - Developer
3. Aiswarya Xavier - Developer
4. Mogahid Tahir - Scrum Master
5. Nindya Widita Ayuningtyas - Tester

## Sprint 2 

### User stories
1. As a manager, I want to see illustrations of drug data in bar form so that I can read drug data faster than in a table or written prose
2. As a manager, I want to see short descriptions of links and buttons when I hover over them, so that I know what they do before using them.
3. As a Manager I want to view a summary of drug spending so that it is easier to track across all regions in the ICB.
4. As a Manager I want the dashboard to appear in a house style so that it can be customised for different users
5. As a clinician, I want to test clinical calculators related to prescribing so that I can evaluate their utility and reduce reliance on multiple software tools.

### Features implemented
1. Add percentage bars to the “Infection treatment drug % of all infection treatments” section. 
2. Add some tooltip text to links/buttons on the dashboard when the user hovers over them
3. Create and add a new summary tile showing the total spend on drugs
4. Change the appearance of the dashboard to match dual UoM and UCL branding
5. Add in a new calculator that allows the user to compute a patient's body Mass Index (BMI)

### Role 
1. Luwa Adeniji-Fasohla - Product Owner
2. Yu Chen - Developer
3. Aiswarya Xavier - Developer
4. Mogahid Tahir - Tester
5. Nindya Widita Ayuningtyas - Scrum Master

## Sprint 3 

### User stories
1. As a Manager, I want to see which item has the greatest quantity and by what percentage, so that I can manage stock across regions
2. As a clinician, I want to calculate creatinine clearance so that I can quickly evaluate kidney function within the dashboard
3. As a manager, I want to see the total number of prescribed antibiotics for each GP practice for selected PCT, so that we can identify potential overprescribing

### Features implemented
1. Add the description of the item with the max quantity, and a percentage bar showing what % of all prescriptions this is to the summary tile at the top of the dashboard
2. Add functionality to the “Creatinine clearance calculator” that was started using the "Cockroft Gault Equation"
3. Add a bar chart that displays the total number of prescribed antibiotics for each GP practice in a selected PCT

### Role 
1. Yu Chen - Developer
2. Aiswarya Xavier - Developer
3. Mogahid Tahir - Tester
4. Nindya Widita Ayuningtyas - Product Owner & Scrum Master

## GitHub
The dashboard's repository can be accessed through https://github.com/nindyawidita14/Charlie.git 

# Guidance on Dashboard Usage & Maintainance 

## Setting up the development environment
1. Install python on your machine. (Recommendation: [Anaconda](https://www.anaconda.com/))
2. Install the required modules by typing the following commands into the Powershell prompt (Windows) or Terminal (Mac)
	conda install -c anaconda flask 
	conda install -c conda-forge flask-sqlalchemy 
	conda install -c anaconda sqlalchemy

## Setting up Git
1. Go to the GitHub page ([https://github.com/(opens in a new tab)](https://github.com/)) and register for an account if you don't already have one.
2. Install Git on your machine ([https://git-scm.com/book/en/v2/Getting-Started-Installing-Git(opens in a new tab)](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)).
3. Git has replaced passwords with personal access tokens. This link explains how to set one up ([https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token(opens in a new tab)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)).

## Working with the database (Optional)
1. Install free DB Browser for [SQLite tool](https://sqlitebrowser.org/%28opens%20in%20a%20new%20tab%29)

## Setting up Dashboard 
1. Installing Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 
2. Create a new repository from https://github.com/nindyawidita14/Charlie.git 
3. Create a new folder/directory for the project on your machine
4. Clone the projects into your folder
		git clone https://github.com/nindyawidita14/Charlie.git 
5. Running the dashboard
		on terminal type: python run.py
		on browser: http://127.0.0.1:5000/dashboard/home 

When making changes to the dashboard code - hold the CTRL button on your keyboard and click the refresh button (windows) or on the internet browser to force a refresh

## Features Available 
1. Summary tiles : total items, average act costs, total drug spend, top prescribed item, number of unique items
2. Visualisation : prescribed items per Primary Care Trusts (PCT), Infection treatment drug as % of all infection treatments, BNF data per PCT, Total number of prescribed antibiotics for each GP practice in a selected PCT
3. About pop-up
4. BMI Calculator
5. Creatinine Clearance Calculator
6. Tooltip 
7. Dual University of Manchester and University College London branding

## Development of Features
1. Each developer should clone the repository into their local machine
2. Create a new branch for each of selected features
3. Update your code for selected features
4. Make a test for the selected features
5. Commit your change with message and push to the remote repository 
6. Pull request your branch to agreed development branch 

# Contributors
1. Luwa Adeniji-Fasohla
2. Yu Chen
3. Aiswarya Xavier
4. Mogahid Tahir
5. Nindya Widita Ayuningtyas

# Contact
Contact the support team @+441234567899 or email support@icb.net

# Acknowledgements

The original dashboard has been derived from https://github.com/IAM-lab/MIE-skeleton