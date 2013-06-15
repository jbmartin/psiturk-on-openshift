from setuptools import setup

setup(name='PsiTurkOnOpenShift', version='0.1',
      description="PsiTurk on OpenShift",
      author='Jay B Martin', author_email='jbmartin@nyu.edu',
      url='http://www.github.com/nyuccl/psiturk',
      install_requires=['sqlalchemy', 'Flask', 'boto', 'gunicorn']
     )
