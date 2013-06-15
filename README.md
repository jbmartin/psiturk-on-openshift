psiTurk on OpenShift
====================

This git repository helps you get up and running quickly w/ a psiTurk installation
on OpenShift.


Running on OpenShift
--------------------

Create an account at http://openshift.redhat.com/ and download the commandline tools at https://www.openshift.com/developers/rhc-client-tools-install

Create a python-2.7 application and add a MySQL cartridge to the app

    rhc app create psiturk python-2.7 mysql-5.1 --from-code git://github.com/jbmartin/psiturk-on-openshift.git

or you can do this to watch the build

    rhc app create -a psiturk -t python-2.7
    rhc cartridge add psiturk -a mysql-5.1

Add this upstream psiturk repo

    cd psiturk
    git remote add upstream -m master https://github.com/jbmartin/psiturk-on-openshift.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://psiturk-$YOURNAMESPACE.rhcloud.com
