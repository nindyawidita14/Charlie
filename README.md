
# About the Project

This project involves developing a prescribing dashboard for Integrated Care Board (ICB) members to monitor the cost management of prescriptions in their GP practices.

# Target Users

Integrated Core Board (ICB) member  

# Aim of the Projects

**Phase 1**: Monitor resource and cost management for various drugs across GP practices

**Phase 2**: Expand dashboard usage to GP practices within the ICB’s catchment area for local management, benchmarking performance, and setting goals by comparing against similar practices and regional averages

# Dashboard Link 
Development: http://127.0.0.1:5000/dashboard/home/ 

# Contributors
1. Luwa Adeniji-Fasohla
2. Yu Chen
3. Aiswarya Xavier
4. Mogahid Tahir
5. Nindya Widita Ayuningtyas

# Agile Method for Dashboard Development 
We use agile method during the dashboard development. The agile method use iterative development that consist of plan, build, test, and review. We use the scrum framework as our guidance for conducting the development. 

![Scrum Framework](https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/2023-09/scrum-framework-with-sdo-logo-9.29.23.png)

# Sprint 1 

## User stories

1. As a Manager, I want to quickly view summary data on the main page to make faster decisions
2. As a Manager, I want to view how many unique items are in the database to understand the scope of the data
3. As a Manager I would like written guidance on how to use and maintain the dashboard so that the project can be worked on by others  which will increase its lifespan
4. As a Manager, I want to see details of the purpose of dashboard and support team contact details, so that it can be useful for future information.

## Features implemented
1. Add the ACT cost to the summary tile at the top of the dashboard
2. Add the number of unique items to the summary tile at the top of the dashboard
3. Add a readme to the GitHub page
4. Add some information to the "About" popup to detail the purpose of dashboard and details of your team and support contact

## Role 
1. Luwa Adeniji-Fasohla - Product Owner
2. Yu Chen - Developer
3. Aiswarya Xavier - Developer
4. Mogahid Tahir - Scrum Master
5. Nindya Widita Ayuningtyas - Tester

# Sprint 2 

## User stories
1. As a manager, I want to see illustrations of drug data in bar form so that I can read drug data faster than in a table or written prose
2. As a manager, I want to see short descriptions of links and buttons when I hover over them, so that I know what they do before using them.
3. As a Manager I want to view a summary of drug spending so that it is easier to track across all regions in the ICB.
4. As a Manager I want the dashboard to appear in a house style so that it can be customised for different users
5. As a clinician, I want to test clinical calculators related to prescribing so that I can evaluate their utility and reduce reliance on multiple software tools.

## Features implemented
1. Add percentage bars to the “Infection treatment drug % of all infection treatments” section. 
2. Add some tooltip text to links/buttons on the dashboard when the user hovers over them
3. Create and add a new summary tile showing the total spend on drugs
4. Change the appearance of the dashboard to match dual UoM and UCL branding
5. Add in a new calculator that allows the user to compute a patient's body Mass Index (BMI)

## Role 
1. Luwa Adeniji-Fasohla - Product Owner
2. Yu Chen - Developer
3. Aiswarya Xavier - Developer
4. Mogahid Tahir - Tester
5. Nindya Widita Ayuningtyas - Scrum Master

# Sprint 3 

## User stories
1. As a Manager, I want to see which item has the greatest quantity and by what percentage, so that I can manage stock across regions
2. As a clinician, I want to calculate creatinine clearance so that I can quickly evaluate kidney function within the dashboard
3. As a manager, I want to see the total number of prescribed antibiotics for each GP practice for selected PCT, so that we can identify potential overprescribing

## Features implemented
1. Add the description of the item with the max quantity, and a percentage bar showing what % of all prescriptions this is to the summary tile at the top of the dashboard
2. Add functionality to the “Creatinine clearance calculator” that was started using the "Cockroft Gault Equation"
3. Add a bar chart that displays the total number of prescribed antibiotics for each GP practice in a selected PCT

## Role 
1. Yu Chen - Developer
2. Aiswarya Xavier - Developer
3. Mogahid Tahir - Tester
4. Nindya Widita Ayuningtyas - Product Owner & Scrum Master

# Acknowledgements

The original dashboard has been derived from https://github.com/IAM-lab/MIE-skeleton