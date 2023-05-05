from typing import cast
from xml.etree import ElementTree

from rich.console import Console
from rich.json import JSON
from rich.theme import Theme

from .enums import Language
from .highlighter import xml_highlighter
from .utils import get_language, get_xml_namespace

theme = Theme(
    {
        ### PYTHON
        "repr.bool_true": "bold cyan",
        "repr.bool_false": "bold bright_red",
        "repr.none": "bold grey23",
        ### JSON
        "json.null": "bold purple",
        "json.bool_true": "bold cyan",
        "json.bool_false": "bold bright_red",
        ### XML
        "xml.tag": "bold blue",
        "xml.attribute_name": "cyan",
        "xml.attribute_value": "green",
        "xml.comment": "grey70",
        "xml.doctype": "bold yellow",
        "xml.processing_instruction": "italic magenta",
        "xml.cdata": "italic red",
    }
)
console = Console(theme=theme)


def prettify_xml(data: str):
    element = ElementTree.XML(data)
    namespace = get_xml_namespace(element)
    ElementTree.register_namespace("", namespace)
    ElementTree.indent(element)
    element_str = ElementTree.tostring(element, encoding="unicode")

    return element_str


def opp(data: str | object):
    language = get_language(data)
    match language:
        case Language.PYTHON:
            console.print(data)
        case Language.JSON:
            console.print(JSON(cast(str, data)))
        case Language.XML:
            pretty_xml = prettify_xml(cast(str, data))
            highlighted_xml = xml_highlighter(pretty_xml)
            console.print(highlighted_xml)
        case Language.HTML:
            raise NotImplementedError()
