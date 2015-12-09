# hivemind-server
Back-End Server for Hive Mind

Uses Heroku instead of Parse. Used for data analysis using Linear Algebra.

Information for JEFF:

Heroku.com is where our hivemind-analytics application is located. It contains server-side code in python (but can include any other language if necessary).

Heroku credentials:

username: nicholas.zarate@gmail.com

password: NZtennis15

Heroku Command Line Documentation: https://devcenter.heroku.com/categories/command-line
(Has a link for the Heroku Toolbelt, which is how you control deployment of code to the Heroku Application)

GIT COMMANDS (in general):

git add .               : adds all modified files to the "add" list

git commit -m "comment" : commits all files on the "add" list

git push                : pushes all commits to github

All of these files represent our server-side Heroku code. However, making changes to any of this code that you can see on Github does not actually DEPLOY any
of that code to our actual server on Heroku.

"git add ." and "git commit -m "comment"" will prep code to be deployed to either github or heroku, then...

to deploy code to Github:

git push origin master

to deploy code to Heroku Application: \ngit push heroku master