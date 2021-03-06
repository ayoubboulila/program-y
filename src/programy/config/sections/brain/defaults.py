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

from programy.config.base import BaseConfigurationData


class BrainDefaultsConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, "defaults")
        self._default_get = "unknown"
        self._default_property = "unknown"
        self._default_map = "unknown"
        self._learn_filename = "learnf.aiml"

    @property
    def default_get(self):
        return self._default_get

    @property
    def default_property(self):
        return self._default_property

    @property
    def default_map(self):
        return self._default_map

    @property
    def learn_filename(self):
        return self._learn_filename

    def load_config_section(self, file_config, bot_config, bot_root):
        binaries = file_config.get_section("defaults", bot_config)
        if binaries is not None:
            self._default_get = file_config.get_option(binaries, "default-get", missing_value=None)
            self._default_property = file_config.get_option(binaries, "default-property", missing_value=None)
            self._default_map = file_config.get_option(binaries, "default-map", missing_value=None)
            learn_filename = file_config.get_option(binaries, "learn-filename", missing_value=None)
            if learn_filename is not None:
                self._learn_filename = self.sub_bot_root(learn_filename, bot_root)
        else:
            logging.warning("'spelling' section missing from bot config, using to defaults")