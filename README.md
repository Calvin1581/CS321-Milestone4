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


## Uploading files

CSV files can be uploaded from the path `"/upload"`. An uploaded file will be automatically parsed and ingested into the database. In order for the file to be properly parsed and inserted, the following conventions must be followed:

- The filename must be in `{"user.csv", "nutrition.csv", "recovery.csv", "sleep.csv"}`. Uploaded files currently overwrite the previous csv of the same name; this should be changed in a later version.
- The csv file must contain the correct column labels.