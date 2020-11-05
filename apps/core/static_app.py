from django.contrib.staticfiles.apps import StaticFilesConfig


class MadanStaticfilesConfig(StaticFilesConfig):
    ignore_patterns = ['CVS', '.*', '*~', '*.sass', '*.js', '*.css']
