from setuptools import setup, find_packages
setup(
    name = "PsiTurkOnOpenShift",
    version = "0.1",
    packages = ["psiturk"],
    entry_points = {
        'console_scripts': ['psiturk = psiturk.psiturk:run_webserver']
    },
    setup_requires = ["Flask", "boto", "SQLAlchemy"],
    extras_require = {
        "gunicorn": "gunicorn"
    },
    author = "NYU Computation and Cognition Lab",
    author_email = "http://nyuccl.org",
    description = "A web framework for dynamic behavioral experiments",
    url = "http://github.com/NYUCCL/psiturk"
)

