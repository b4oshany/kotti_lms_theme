# -*- coding: utf-8 -*-

"""
Created on 2017-01-10
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import kotti_lms_theme.resources
    kotti_lms_theme.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_lms_theme.kotti_configure'}
