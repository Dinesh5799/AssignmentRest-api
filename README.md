# AssignmentRest-api
AssignmentRest-api

Pre-requisites for running the flask app:-
1.) Python(I used the latest).
2.)Packages required Flask,jsonify,request(Installing Packages Ex:- pip install flask).
Steps to run the app.
1.) After installing flask and adding the path run the below commands in shell.
    1.) set FLASK_APP=rest_api.py
    2.) flask run(This starts a local server).
To view the app.
After starting the server visit the follow url:-
1.)http://127.0.0.1:5000/users/pages?page=1 (Pagination->10 records at a time).
2.)http://127.0.0.1:5000/users?firstName=Thomas (Format to retrieve data using firstName)
3.)http://127.0.0.1:5000/users?lastName=Hockensmith (Format to retrieve data using lastName)
4.)http://127.0.0.1:5000/users?email=Oscar.Huggins@test.com (Format to retrieve data using email)

Note:- Sample data is present in the file data.json.



