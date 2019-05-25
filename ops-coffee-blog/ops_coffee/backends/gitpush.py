from git import Repo
from django.conf import settings


class GitRun:
    def __init__(self):
        self.repo = Repo(settings.OPS_COFFEE_GIT_DIR)

    def push(self):
        # git clone git@github.com:ops-coffee/ops-coffee.github.com.git .

        try:
            self.repo.git.add(A=True)
            self.repo.index.commit('ops-coffee')
            self.repo.remote(name='origin').push()

            return True, True
        except Exception as e:
            return False, str(e)
