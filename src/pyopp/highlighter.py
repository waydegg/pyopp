from rich.highlighter import RegexHighlighter
from rich.text import Text


class XMLHighlighter(RegexHighlighter):
    """Highlights XML"""

    base_style = "xml."
    highlights = [
        r"(?P<tag><(/?)[^/<>]*>)",
        r"(?P<attribute_name>\b[\w-]+(?=\s*=\s*[\"']))",
        r"(?P<attribute_value>[\"'][^\"']*[\"'])",
        r"(?P<comment><!--[^>]*-->)",
        r"(?P<doctype><!DOCTYPE[^>]*>)",
        r"(?P<processing_instruction><\?[^>]*\?>)",
        r"(?P<cdata><!\[CDATA\[[^\]]*\]\]>)",
    ]

    def highlight(self, text: Text) -> None:
        super().highlight(text)


xml_highlighter = XMLHighlighter()
