# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.core.urlresolvers import NoReverseMatch, reverse
from jinja2 import contextfunction

from shuup.utils.importing import cached_load


@contextfunction
def model_url(context, model, absolute=False):
    uri = None

    model_url_method = cached_load('SHUUP_MODEL_URL_RESOLVER_SPEC')
    if callable(model_url_method):
        uri = model_url_method(context, model, absolute)
        if uri is not None:
            return uri


def get_url(url, *args, **kwargs):
    """
    Try to get the reversed URL for the given route name, args and kwargs.

    If reverse resolution fails, returns None (instead of throwing an exception).

    :param url: URL name.
    :type url: str
    :param args: URL args
    :type args: Iterable[object]
    :param kwargs: URL kwargs
    :type kwargs: dict[str, object]
    :return: Reversed URL or None
    :rtype: str|None
    """
    try:
        return reverse(url, args=args, kwargs=kwargs)
    except NoReverseMatch:
        return None


def has_url(url, *args, **kwargs):
    """
    Try to get the reversed URL for the given route name, args and kwargs and return a success flag.

    :param url: URL name.
    :type url: str
    :param args: URL args
    :type args: Iterable[object]
    :param kwargs: URL kwargs
    :type kwargs: dict[str, object]
    :return: Success flag
    :rtype: bool
    """
    return bool(get_url(url, *args, **kwargs))
