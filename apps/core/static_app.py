import os

from django.conf import settings
from django.contrib.staticfiles.apps import StaticFilesConfig
from django.contrib.staticfiles.finders import BaseFinder
from django.contrib.staticfiles.utils import matches_patterns
from django.core.files.storage import FileSystemStorage


def get_files(storage, ignore_patterns=None, location=''):
    if ignore_patterns is None:
        ignore_patterns = []
    directories, files = storage.listdir(location)
    for fn in files:

        if matches_patterns(fn, ignore_patterns):
            continue
        if location:
            fn = os.path.join(location, fn)

            if matches_patterns(fn, ignore_patterns):
                continue
        yield fn

    for dir_ in directories:
        if matches_patterns(dir_, ignore_patterns):
            continue
        if location:
            dir_ = os.path.join(location, dir_)
        yield from get_files(storage, ignore_patterns, dir_)


class MadanStaticfilesConfig(StaticFilesConfig):
    ignore_patterns = ['CVS', '.*', '*~', '*.sass', '*.js', '*.css']


class NodeModulesFinder(BaseFinder):
    """
    The static files finder that find static files stored
    in the NODE_MODULES_ROOT, and excludes metadata and unwanted files when
    static files will be collected.
    """
    storage = FileSystemStorage(location=settings.NODE_MODULES_ROOT)
    ignore_patterns = [
        '*.less',
        '*.scss',
        '*.styl',
        '*.sh',
        '*.htm',
        '*.html',
        '*.md',
        '*.markdown',
        '*.rst',
        '*.php',
        '*.rb',
        '*.txt',
        '*.map',
        '*.yml',
        '*.yaml',
        '*.json',
        '*.xml',
        '*.ts',
        '*.es6',
        '*.coffee',
        '*.litcoffee',
        '*.lock',
        '*.patch',
        'README*',
        'LICENSE*',
        'LICENCE*',
        'CHANGES',
        'CHANGELOG',
        'HISTORY',
        'NOTICE',
        'COPYING',
        'license',
        '*test*',
        '*bin*',
        '*samples*',
        '*example*',
        '*docs*',
        '*tests*',
        '*demo*',
        'Makefile*',
        'Gemfile*',
        'Gruntfile*',
        'gulpfile.js',
        '.tagconfig',
        '.npmignore',
        '.gitignore',
        '.gitattributes',
        '.gitmodules',
        '.editorconfig',
        '.sqlite',
        'grunt',
        'gulp',
        'less',
        'sass',
        'scss',
        'coffee',
        'tasks',
        'node_modules',
    ]

    def find(self, path, all_=False):
        matches = []
        if self.storage.exists(path):
            matched_path = self.storage.path(path)
            if not all_:
                return matched_path
            matches.append(matched_path)
        return matches

    def list(self, *args, **kwargs):
        for path in get_files(self.storage, self.ignore_patterns):
            yield path, self.storage
