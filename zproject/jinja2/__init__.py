
from typing import Any

from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.defaultfilters import slugify, pluralize
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils import translation
from django.http import HttpResponse
from jinja2 import Environment

from .compressors import minified_js
from zerver.templatetags.app_filters import display_list, render_markdown_path


def environment(**options: Any) -> Environment:
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'render_markdown_path': render_markdown_path,
        'minified_js': minified_js,
    })

    env.install_gettext_translations(translation, True)

    env.filters['slugify'] = slugify
    env.filters['pluralize'] = pluralize
    env.filters['display_list'] = display_list

    return env
