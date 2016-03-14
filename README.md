# Environment Setup

Make sure you have successfully synced the git submodule (See [Deployment](https://github.com/nickzarate/hivemind-analytics#deployment))

Setup the Heroku remote
```
heroku git:remote -a hivemind-analytics
```

Install [vagrant](https://www.vagrantup.com/) and type in the following commands...
```
vagrant up
vagrant ssh
cd /
cd vagrant
python run.py
```
Open `http://localhost:5000`.

Use `exit` to leave the virtual machine set up by vagrant and `vagrant destroy` to terminate it.

# Deployment

One time setup:

In order to sync the build branch of hivemind-web, we must add it as a git submodule.
```
rm -rf hivemind/static
git rm --cached hivemind/static
git submodule add -b build --name static https://github.com/nickzarate/hivemind-web.git hivemind/static
```

Normal deploy process:

Anytime the build branch of the hivemind-web repository is updated, run this command to update the submodule
```
git submodule foreach git pull origin build
```

Add and commit new changes made in the client code, then push to hivemind-analytics, and to the heroku app.
(The last command will not work, the proper heroku remote must be setup first README needs updating...)

```
$ git add hivemind/static
$ git commit -m "Update submodule"
$ git push (push to this repository)
$ git push heroku master (Deploy)
$ heroku open (Check out the newly deployed app!)
```
