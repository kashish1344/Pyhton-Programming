import bs4
import urllib.request as url

job_name=input("Enter Your Profession: ")
job_name=job_name.replace(' ','-')
print("Job For ",job_name)
path='https://www.freshersworld.com/jobs/jobsearch/{}-jobs'.format(job_name)
res=url.urlopen(path)
page= bs4.BeautifullSoup(res, 'lxml')
job=page.find_all(id="tab_search",class_="margin-none latest-jobs-title font-20")

for i in range(len(job)):
    print(job[i].text)
