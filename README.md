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

### Results: **still needs to be written**

Updated graphs (made with Plotly)
<img width="1400" alt="Screen Shot 2022-10-26 at 2 20 51 PM" src="https://user-images.githubusercontent.com/30237570/198105488-a48abcf9-deca-4104-b361-43537d8b5ca1.png">


### Team Reflection: **still needs to be written**

### Contribution List: 
* Calvin:
* Ben:
* Matt:
* Hannah: Created inheritance for the seach bar, created inheritance for the nav bar drop down
* Milo: Initially made the web application runnable
* Tamsin: Create dummy csv data for readiness, sleep, nutrition, and whole team readiness, graphs branch: read csv data into plotly graphs (pie charts and line graphs) via JSON, working on reading csv data into athlete breakdown table
* Nicole: 

### Extensions: 
We added a functional ReadMe file to our repository detailing the website.

### References: 
Naser Al Madi


## Uploading files

CSV files can be uploaded from the path `"/upload"`. An uploaded file will be automatically parsed and ingested into the database. In order for the file to be properly parsed and inserted, the following conventions must be followed:

- The filename must be in `{"user.csv", "nutrition.csv", "recovery.csv", "sleep.csv"}`. Uploaded files currently overwrite the previous csv of the same name; this should be changed in a later version.
- The csv file must contain the correct column labels.
