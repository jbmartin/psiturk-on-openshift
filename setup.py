from setuptools import setup, find_packages
setup(
    name = "PsiTurk",
    version = "0.1",
    entry_points = {
        'console_scripts': ['psiturk = psiturk.psiturk:run_webserver']
    },
    install_requires=["Flask", "boto", "SQLAlchemy", "gunicorn", "psycopg2"],
    author = "NYU Computation and Cognition Lab",
    author_email = "http://nyuccl.org",
    description = "A web framework for dynamic behavioral experiments",
    url = "http://github.com/NYUCCL/psiturk"
)

