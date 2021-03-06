import unittest

from programy.config.file.yaml_file import YamlConfigurationFile
from programy.config.sections.brain.defaults import BrainDefaultsConfiguration
from programy.config.sections.client.console import ConsoleConfiguration

class BrainDefaultsBinariesConfigurationTests(unittest.TestCase):

    def test_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            defaults:
                default-get: unknown
                default-property: unknown
                default-map: unknown
                learn-filename: y-bot-learn.aiml
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        defaults_config = BrainDefaultsConfiguration()
        defaults_config.load_config_section(yaml, brain_config, ".")

        self.assertEqual("unknown", defaults_config.default_get)
        self.assertEqual("unknown", defaults_config.default_property)
        self.assertEqual("unknown", defaults_config.default_map)
        self.assertEqual("y-bot-learn.aiml", defaults_config.learn_filename)


    def test_without_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            defaults:
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        defaults_config = BrainDefaultsConfiguration()
        defaults_config.load_config_section(yaml, brain_config, ".")


    def test_with_no_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        defaults_config = BrainDefaultsConfiguration()
        defaults_config.load_config_section(yaml, brain_config, ".")

