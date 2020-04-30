from django import template
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

register = template.Library()


@register.filter(name='to_highlight')
def to_highlight(text, language):
    lexer = get_lexer_by_name(language)
    return highlight(text, lexer, HtmlFormatter(linenos=True))
