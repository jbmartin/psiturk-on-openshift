psiTurk on OpenShift
====================

This git repository helps you get up and running quickly w/ a psiTurk installation
on OpenShift.


Running on OpenShift
--------------------

Create an account at http://openshift.redhat.com/ and download the command line tools at https://www.openshift.com/developers/rhc-client-tools-install

Create a python-2.7 application and add a PostgreSQL cartridge to the app

    rhc app create psiturk python-2.7 postgresql-8.4 --from-code git://github.com/jbmartin/psiturk-on-openshift.git

or you can do this to watch the build

    rhc app create -a psiturk -t python-2.7
    rhc cartridge add -a psiturk20 postgresql-8.4

Add this upstream psiturk repo

    cd psiturk
    git remote add upstream -m master https://github.com/jbmartin/psiturk-on-openshift.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

That's it, you can now checkout your application at

    http://psiturk-$YOURNAMESPACE.rhcloud.com


Accessing Your Database
-----------------------

Run

    rhc port forward -a psiturk

Connect to the database using your favorite SQL app, the PostgreSQL Local specs, and your credentials.
