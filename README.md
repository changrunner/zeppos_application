# zeppos_application
All things to get an application moving.


## usage

Add a config.json
```
{
  "test_me": "123"
}
```

Python

```
from zeppos_application.app_config import AppConfig

class SomeClassName:
    def __init__(self):
        self.config_dict = AppConfig.get_json_config_dict(__file__)
        print(self.config_dict['test_me'])
```
or
```
from zeppos_application.app_config import AppConfig

class SomeClassName:
    def __init__(self):
        self.config_dict = AppConfig.get_json_config_dict(__file__, config_file_name="config.json")
        print(self.config_dict['test_me'])
```
