import unittest
from zeppos_application.app_config import AppConfig
from zeppos_logging.app_logger import AppLogger

class TestTheProjectMethods(unittest.TestCase):
    def test_get_json_config_dict_methods(self):
        # AppLogger.configure_and_get_logger("test")
        # AppLogger.set_debug_level()
        self.assertEqual("123", AppConfig.get_json_config_dict(__file__)["test_me"])
        self.assertEqual(None, AppConfig.get_json_config_dict(__file__, "config_not_there.json"))

    def test_config_values_for_app_methods(self):
        # AppLogger.configure_and_get_logger("test")
        # AppLogger.set_debug_level()
        self.assertEqual('main', AppConfig.config_values_for_app('tests')["environment"])


if __name__ == '__main__':
    unittest.main()
