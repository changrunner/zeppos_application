import unittest
from zeppos_application.app_config import AppConfig

class TestTheProjectMethods(unittest.TestCase):
    def test_get_json_config_dict_methods(self):
        self.assertEqual("123", AppConfig.get_json_config_dict(__file__)["test_me"])
        self.assertEqual(None, AppConfig.get_json_config_dict(__file__, "config_not_there.json"))


if __name__ == '__main__':
    unittest.main()
