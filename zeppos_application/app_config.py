from zeppos_root.root import Root
from json import loads
from cachetools import cached, TTLCache
from zeppos_logging.app_logger import AppLogger
from os import path, getcwd
from zeppos_git.branch import Branch


class AppConfig:
    @staticmethod
    # cache data for no longer than ten minutes
    @cached(cache=TTLCache(maxsize=1024, ttl=600))
    def get_json_config_dict(current_module_filename, config_file_name="config.json"):
        AppLogger.logger.debug(f"current_module_filename: {current_module_filename}")
        AppLogger.logger.debug(f"config_file_name: {config_file_name}")
        root_path = Root.find_root_of_project(
                    current_module_filename=current_module_filename,
                    root_marker_filename_list=[config_file_name]
                )
        AppLogger.logger.debug(f"root_path: {root_path}")
        if root_path and path.exists(root_path):
            config_full_file_name = \
                path.join(
                    root_path,
                    config_file_name
                )
            if path.exists(config_full_file_name):
                with open(config_full_file_name, 'r') as fl:
                    config_values = loads(fl.read())
                    AppLogger.logger.debug(f"Config Values: {config_values}")
                    return config_values
        return None

    @staticmethod
    # cache data for no longer than ten minutes
    @cached(cache=TTLCache(maxsize=1024, ttl=600))
    def config_values_for_app(app_dir):
        AppLogger.logger.debug("Get Configuration")
        AppLogger.logger.debug(f"__file__: {__file__}")
        AppLogger.logger.debug(f"Root: {Root.find_root_of_project(__file__)}")
        AppLogger.logger.debug(f"current_module_filename: {path.join(Root.find_root_of_project(__file__), app_dir)}")
        AppLogger.logger.debug(f"config_file_name: config.{Branch.get_current()}.json")

        config_dict = AppConfig.get_json_config_dict(
            current_module_filename=path.join(Root.find_root_of_project(__file__), app_dir),
            config_file_name=f"config.{Branch.get_current()}.json"
        )

        if config_dict:
            AppLogger.logger.debug(f"Environment: {config_dict['environment']}")
        else:
            AppLogger.logger.error(f"There is no config [config.{Branch.get_current()}.json] probably! "
                                   f"The branch should be local, test, production.")
        return config_dict


