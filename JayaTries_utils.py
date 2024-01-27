# Online Python-3 Compiler (Interpreter)
print ("Hello, World!")
"""
This module provides a reusable byline for jaya
"""

#Import Dependencies

import math
import statistics

#Defining Variables
company_name: str = "Stellar Analytics Inc."
count_active_projects: int = 6
has_international_presence: bool = True
average_client_satisfaction: float = 4.7
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
Google_Sidebar_Presence: bool = True
Number_of_employees: int = 98
job_options: list = ['Data Analyst', 'Data engineer','Data scientist','Intern']
Salary_Range: str = '80k'

#Define formated strings
active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"
services_offered_string: str = f"Services Offered: {services_offered}"
job_options_string: str = f"Job_Options:{job_options}"

#Calculate Stats
import statistics

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

#Byline String
byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{client_satisfaction_string}
{services_offered_string}
{stats_string}
{job_options_string}

"""
def main():
    ''' Display all output'''
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print(services_offered_string)
    print(stats_string)
    print(job_options_string)

    # If all of the above works, then the byline should work too:
    print(byline)

#Conditional Script execution
if __name__ == '__main__':
    main()

