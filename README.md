DJFiles
=====

Files is a simple Django app to add files to project.

### Requirements

* Django >= 1.8
* unicode-slugify

### Installation

1. Add "djfiles" to your INSTALLED_APPS setting like this:

```
INSTALLED_APPS = [
    ...

    'djfiles',
]
```

2. Apply migrations:

```bash
$ python manage.py migrate djfiles
```
