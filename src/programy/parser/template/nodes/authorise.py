"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.exceptions import ParserException

class TemplateAuthoriseNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)
        self._role = None

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    def resolve(self, bot, clientid):
        try:
            # Check if the user, role or group exists, assumption being, that if defined
            # in the tag and exists then we can execute the inner children
            # Assumption is that user has been authenticated and passed and is value
            if bot.brain.authorisation is not None:
                if bot.brain.authorisation.authorise(clientid, self.role) is False:
                    srai_text = bot.brain.authorisation.get_default_denied_srai()
                    resolved = bot.ask_question(clientid, srai_text, srai=True)
                    logging.debug("[%s] resolved to [%s]", self.to_string(), resolved)
                    return resolved

            # Resolve afterwards, as pointless resolving before checking for authorisation
            resolved = self.resolve_children_to_string(bot, clientid)
            logging.debug("[%s] resolved to [%s]", self.to_string(), resolved)
            return resolved

        except Exception as excep:
            logging.exception(excep)
            return ""

    def to_string(self):
        text = "AUTHORISE ("
        text += "role=%s"%self._role
        text += ")"
        return text

    def to_xml(self, bot, clientid):
        xml = '<authorise'
        xml += ' role="%s"' % self._role
        xml += '>'
        xml += self.children_to_xml(bot, clientid)
        xml += '</authorise>'
        return xml

    #######################################################################################################
    # AUTHORISE_ATTRIBUTES ::= role="ROLEID"
    # AUTHORISE_EXPRESSION ::== <authorise( AUTHORISE_ATTRIBUTES)*>TEMPLATE_EXPRESSION</authorise> |

    def parse_expression(self, graph, expression):

        if 'role' in expression.attrib:
            self._role = expression.attrib['role']

        if self._role is None:
            raise ParserException("AUTHORISE role attribute missing !")

        head_text = self.get_text_from_element(expression)
        self.parse_text(graph, head_text)

        for child in expression:
            graph.parse_tag_expression(child, self)
            tail_text = self.get_tail_from_element(child)
            self.parse_text(graph, tail_text)

