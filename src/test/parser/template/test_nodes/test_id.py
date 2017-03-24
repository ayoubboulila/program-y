import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.id import TemplateIdNode
from programy.parser.template.nodes.word import TemplateWordNode

from test.parser.template.base import TemplateTestsBaseClass


class TemplateIdNodeTests(TemplateTestsBaseClass):

    def test_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        node = TemplateIdNode()
        self.assertIsNotNone(node)

        root.append(node)
        self.assertEqual(len(root.children), 1)

        self.assertEqual(root.resolve(None, "clientid"), "clientid")

    def test_to_xml(self):
        root = TemplateNode()
        root.append(TemplateIdNode())

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual("<template><id /></template>", xml_str)
