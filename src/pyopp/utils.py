import os
import re
from xml.etree.ElementTree import Element

from pygments.lexers import HtmlLexer, JsonLexer, XmlLexer
from pygments.lexers.python import PythonLexer

from .enums import Language


def get_xml_namespace(element: Element) -> str:
    match = re.search(r"\{(.*?)\}", element.tag)
    return match.group(1) if match else ""


def get_language(data: str | object) -> Language:
    if not isinstance(data, str):
        return Language.PYTHON
    elif data.startswith("{") or data.startswith("["):
        return Language.JSON
    elif data.startswith("<"):
        # TODO: return HTML or XML
        return Language.XML
    else:
        raise ValueError("Input must be JSON, XML, or HTML")


def get_lexer(language: Language):
    match language:
        case Language.PYTHON:
            return PythonLexer()
        case Language.JSON:
            return JsonLexer()
        case Language.XML:
            return XmlLexer()
        case Language.HTML:
            return HtmlLexer()


def get_style() -> str:
    style = os.getenv("PYOPP_STYLE")
    if style is None:
        style = "default"

    return style
