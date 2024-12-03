import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from pydantic import BaseModel

import selene_in_action
from selene_in_action import utils


class Config(BaseModel):
    # remote_url: str = os.getenv('remote_url')
    # deviceName: str = os.getenv('DEVICE_NAME')
    # platformName: str = os.getenv('PLATFORM_NAME')
    # platformVersion: str = os.getenv('PLATFORM_VERSION')
    # appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    # app_local: str = os.getenv('APP', '/Users/nlevochkina/Downloads/app-alpha-universal-release.apk')
    # app_bstack: str = os.getenv('APP')
    # udid: str = os.getenv('UDID')
    # load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env'))
    # context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICE_NAME')
    udid: str = os.getenv('UDID')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    # app_local: str = utils.file.abs_path_from_project(os.getenv('APP'))
    app_bstack: str = os.getenv('APP')
    platformName: str = os.getenv('PLATFORM_NAME')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env'))
    userName: str = os.getenv('userName')
    accessKey: str = os.getenv('accessKey')


    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)

        if context == 'brstack':
            load_dotenv()
            username = os.getenv('userName')
            accesskey = os.getenv('accessKey')
            options.set_capability('remote_url', 'http://hub.browserstack.com/wd/hub')
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_bstack)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Wikipedia tests project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'Wikipedia tests',
                    'userName': username,
                    'accessKey': accesskey,
                },
            )

        return options