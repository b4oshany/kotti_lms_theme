# -*- coding: utf-8 -*-

"""
Created on 2017-01-10
:author: Oshane Bailey (b4.oshany@gmail.com)
"""
from datetime import datetime
from kotti.resources import File
from pyramid.i18n import TranslationStringFactory
from kotti.views.util import TemplateAPI
from kotti.util import Link

_ = TranslationStringFactory('kotti_lms_theme')

TOP_NAV_MENU = []
SIDE_NAV_MENU = []

class LMSTemplateAPI(TemplateAPI):

    @property
    def TOP_NAV_MENU(self):
        return TOP_NAV_MENU

    @property
    def SIDE_NAV_MENU(self):
        return SIDE_NAV_MENU
        
    @property
    def system_time(self):
        return datetime.now()


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_lms_theme.kotti_configure

        to enable the ``kotti_lms_theme`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_lms_theme'
    settings["kotti.templates.api"] = 'kotti_lms_theme.LMSTemplateAPI'
    settings['kotti.alembic_dirs'] += ' kotti_lms_theme:alembic'
    settings['kotti.fanstatic.view_needed'] += ' kotti_lms_theme.fanstatic.css_and_js'


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.override_asset('kotti', 'kotti_lms_theme:')
    config.add_translation_dirs('kotti_lms_theme:locale')
    config.add_static_view('static-kotti_lms_theme', 'kotti_lms_theme:static')

    config.scan(__name__)
