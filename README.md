psiTurk on OpenShift
====================

This git repository helps you get up and running quickly w/ a psiTurk installation
on OpenShift.


Running on OpenShift
--------------------

Create an account at http://openshift.redhat.com/

Create a python-2.7 application

    rhc app create -a psiturk -t python-2.7

Add this upstream psiturk repo

    cd psiturk
    git remote add upstream -m master https://github.com/jbmartin/flask-on-openshift.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://psiturk-$YOURNAMESPACE.rhcloud.com
