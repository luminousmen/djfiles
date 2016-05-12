[![Coverage Status](https://coveralls.io/repos/github/luminousmen/djfiles/badge.svg?branch=master)](https://coveralls.io/github/luminousmen/djfiles?branch=master)

DJFiles
=====

DJFiles is a simple Django app for manage static files of your project.

### Requirements

* Django >= 1.8
* unicode-slugify

### Installation

Add ```djfiles``` to your INSTALLED_APPS setting like this:

```
INSTALLED_APPS = [
    ...

    'djfiles',
]
```

Apply ```djfiles``` migrations:

```bash
$ python manage.py migrate djfiles
```
