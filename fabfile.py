#! -*- coding: utf-8 -*-

from __future__ import with_statement
from itertools import dropwhile
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import *


env.local_src_dir = '/Users/manmanli/xm-webs/djangoperm/'


def add():
    local('git add -A')


def commit():
    with warn_only():
        result = local('git commit -m "djangoperm"', capture=True)
        if result.failed and 'nothing to commit' not in result:
            abort(red(result))


def push():
    local('git push')


@task
def prepare_deploy():
    with lcd(env.local_src_dir):
        add()
        commit()
        push()
    print green('-- prepare_deploy success.')
