# chrphb_quarto_util


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This file will become your README and also the index of your
documentation.

## Install

``` sh
pip install chrphb_quarto_util
```

## How to use

Fill me in please! Don’t forget code examples:

``` python
1+1
```

    2

``` python
from chrphb_quarto_util.core import create_post_from_template
```

``` python
! mkdir /tmp/templates
```

``` python
! mkdir /tmp/posts
```

``` python
! touch /tmp/templates/index.ipynb
```

``` python
create_post_from_template('/tmp/templates','/tmp/posts','test2')
```

    NameError: name 'create_post_from_template' is not defined
    [0;31m---------------------------------------------------------------------------[0m
    [0;31mNameError[0m                                 Traceback (most recent call last)
    Cell [0;32mIn[1], line 1[0m
    [0;32m----> 1[0m [43mcreate_post_from_template[49m([38;5;124m'[39m[38;5;124m/tmp/templates[39m[38;5;124m'[39m,[38;5;124m'[39m[38;5;124m/tmp/posts[39m[38;5;124m'[39m,[38;5;124m'[39m[38;5;124mtest2[39m[38;5;124m'[39m)

    [0;31mNameError[0m: name 'create_post_from_template' is not defined

``` python
! ls -lRt /tmp/posts
```

    /tmp/posts:
    total 4
    drwxrwxr-x 2 chris chris 4096 juil. 30 23:40 2024-07-30-test

    /tmp/posts/2024-07-30-test:
    total 0
    -rw-rw-r-- 1 chris chris 0 juil. 30 23:40 index.ipynb
