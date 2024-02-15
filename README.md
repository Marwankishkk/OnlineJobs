# OnlineJobs
1- pipenv install

2-pipenv shell

3-python3 manage.py makemigrations

4-python3 manage.py migrate


5-python3 manage.py add_data

accounts/users        # to create a user
accounts/users/employer/     #add user logged in to employer model
accounts/users/employer/profile     #shows your logged in employer data and edit it

accounts/users/employee/    #add user logged in to employee model
accounts/users/employee/profile   #shows your logged in employee data and edit it


jobs/              # list jobs for any user and create a job by employer

applicants/<int:jobs_id>       # show the jobs the logged in employer posted


applicants/<int:jobs_id>/<int:id>/ # accept or reject the the application for a job


swagger/   # shows all the endpoints
