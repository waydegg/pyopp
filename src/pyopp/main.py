import json
import pprint
from typing import cast
from xml.etree import ElementTree

import pygments
from pygments.formatters import Terminal256Formatter

from .enums import Language
from .utils import get_language, get_lexer, get_style, get_xml_namespace


def prettify_object(data: object):
    object_str = pprint.pformat(data, indent=1, width=88)

    return object_str


def prettify_json(data: str):
    json_obj = json.loads(data)
    json_str = json.dumps(json_obj, indent=2)

    return json_str


def prettify_xml(data: str):
    element = ElementTree.XML(data)
    namespace = get_xml_namespace(element)
    ElementTree.register_namespace("", namespace)
    ElementTree.indent(element)
    element_str = ElementTree.tostring(element, encoding="unicode")

    return element_str


def prettify_html(data: str):
    raise NotImplementedError()


def pretty_print(data: str | object, highlight: bool = True, style: str | None = None):
    language = get_language(data)
    match language:
        case Language.PYTHON:
            data_str = prettify_object(data)
        case Language.JSON:
            data_str = prettify_json(cast(str, data))
        case Language.XML:
            data_str = prettify_xml(cast(str, data))
        case Language.HTML:
            data_str = prettify_html(cast(str, data))

    if highlight:
        lexer = get_lexer(language)
        style = style or get_style()
        formatter = Terminal256Formatter(style=style)
        data_str = pygments.highlight(data_str, lexer, formatter)

    print(data_str)
