from zeppos_root.root import Root
from os import path
from json import loads
from cachetools import cached, LRUCache, TTLCache

class AppConfig:

    @staticmethod
    # cache data for no longer than ten minutes
    @cached(cache=TTLCache(maxsize=1024, ttl=600))
    def get_json_config_dict(current_module_filename, config_file_name="config.json"):
        root_path = Root.find_root_of_project(
                    current_module_filename=current_module_filename,
                    root_marker_filename_list=[config_file_name]
                )
        if root_path and path.exists(root_path):
            config_full_file_name = \
                path.join(
                    root_path,
                    config_file_name
                )
            if path.exists(config_full_file_name):
                with open(config_full_file_name, 'r') as fl:
                    return loads(fl.read())

        return None


