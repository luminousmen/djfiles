[![Coverage Status](https://coveralls.io/repos/github/luminousmen/djfiles/badge.svg?branch=master)](https://coveralls.io/github/luminousmen/djfiles?branch=master)
[![Build Status](https://travis-ci.org/luminousmen/djfiles.svg?branch=master)](https://travis-ci.org/luminousmen/djfiles)

DJFiles
=====

DJFiles is a simple Django app for manage static files of your project.

### Requirements

* Python == 2.7
* Django >= 1.8

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
$ ./manage.py migrate djfiles
```
