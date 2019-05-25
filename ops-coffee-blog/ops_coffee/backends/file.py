from django.conf import settings


class FileRun:
    def __init__(self):
        self.file = settings.BASE_DIR + '/ops_coffee/backends/blog.json'

    def read(self):
        try:
            with open(self.file, 'r', encoding='utf8') as f:
                return True, f.read()

        except Exception as e:
            return False, str(e)

    def write(self, content):
        try:
            with open(self.file, 'w', encoding='utf8') as f:
                return True, f.write(content)

        except Exception as e:
            return False, str(e)
