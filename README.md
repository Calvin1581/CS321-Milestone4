# CS321-Milestone4
<h2>Dynamic website with Flask</h2>

## Installing dependencies

In order to run this Flask app, activate the virtual environment of your choice, then run:

`
pip install -r requirements.txt
`

This will install all the requirements needed to run the Flask app.

In order to actually run the app, navigate to the base repository directory. Your current directory should contain main.py. Run the following:

`
flask --app main run
`

The command line will output the port on which the website is running.

# Report

### Abstract: 
This milestone involved developing a dynamic version of the Athletic Management system.  We created a database to handle athlete data and connected it to our HTML pages from the previous milestone, in addition to functional dashboards for various users, and login/signup ability.  We updated the graphs from the Corona bootstrap to Plotly so that they can be updated in real time via CSV.

### Sprint Backlog:
User stories (general):
<p>As a user a can create a new account using an email and password – Completed</p>
As a user of the website I can log in to the website with a username and password – Completed
As a user of the website I can login to my assigned role –Completed
As a user of the website, I can navigate back to my dashboard by clicking on the mule icon – Partially completed (works for moving between athlete detail pages and dashboard)

Admin/Peak:
As an Admin, I can edit the permissions of all other users. – Started but unfinished
As an Admin, I can view the sports science data (sleep, nutrition, readiness) of athletes and teams – Completed
As an Admin, I can upload csv with the sport science data of our athletes, or add users – Partially completed (admin can upload data through CSV, but the data does not go into the database at this time)
As an Admin, I can delete users accounts without deleting the user’s data – not implemented

Athlete:
As an Athlete, I can view graphs detailing my most recent sports science data (sleep, nutrition, readiness). – Completed (using dummy data) 
As an Athlete, I can view a graph showing changes in my sports science data over time. – Completed (using dummy data)
As an Athlete, I can change the range of time over which I view changes in my sports science data.--not implement
As an Athlete, I can download a csv file of my sports science data.--not implemented
As an Athlete, I can view detail pages on different aspects of my sports science data (sleep, readiness, calories) – Partially completed (can view detail pages, need to add graphs)
As an Athlete, I can view notes on my readiness to play, sleep, and nutrition.--Completed

Coach
As a Coach, I can view sports science data from athletes on my teams –Completed
As a Coach, I can choose which of my teams I wish to view– not implemented
As a Coach, I can navigate to an athlete’s individual page by clicking on their profile – Completed
As a Coach, I can see graphs showing changes in sports science data over time (readiness, sleep, nutrition) –Partially completed (Have plots, but they wouldn’t load in detailed athlete pages)
As a Coach, I can download csvs of my athlete’s sports science data? –not implemented

### Results: 
In this milestone we created a dynamic version of the Athletic Management System. Our website includes a database that stores athlete data and sources it to the pages of the website. All of the pages and clickable link are workable and link to their correct locations. A user is now able to sign up and login to the system now to see their specific data. The graph were also taken from imagees to Plotly graphs that are updateable via CSV.

### Burn Down Chart:
![image](https://user-images.githubusercontent.com/70499767/198411961-5d580d47-4cb9-4bb7-ad28-31d38ea5981d.png)


Updated graphs (made with Plotly)
<img width="1400" alt="Screen Shot 2022-10-26 at 2 20 51 PM" src="https://user-images.githubusercontent.com/30237570/198105488-a48abcf9-deca-4104-b361-43537d8b5ca1.png">


### Team Reflection: 
In this milestone we held multiple in person meetings to update the group needs, issues, and duties. These were very useful and eliminated the delay of text message respones. We did a lot of our work seperately and when pull requests were made they were revised promptly. Obstacle we overcame included: our scrum master having covid, difficulties in specific code, and some organization of issues. We utilized communication and praise during code reviews during this mileston.**

### Contribution List: 
* Calvin: Scrum Master, Created database for Jump Metric data, Reviewed and merged requests, Created burndown chart
* Ben:
* Matt:
* Hannah: Created inheritance for the seach bar, created inheritance for the nav bar drop down, linked the signup, the three detail pages, and made the mule a back button.
* Milo: Initially made the web application runnable
* Tamsin: Create dummy csv data for readiness, sleep, nutrition, and whole team readiness, graphs branch: read csv data into plotly graphs (pie charts and line graphs) via JSON, working on reading csv data into athlete breakdown table
* Nicole: 

### Extensions: 
We added a functional ReadMe file to our repository detailing the website.

### References: 
Naser Al Madi

