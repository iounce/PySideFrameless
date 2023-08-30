# -*- coding: utf-8 -*-

# version information of the application
class AppVersion:
    APP_VERSION = '1.0.1'
    APP_BUILD = 'b413dc7'
    APP_BUILD_DATE = '2023-08-30'

    @staticmethod
    def get_version():
        return 'Version: ' + AppVersion.APP_VERSION

    @staticmethod
    def get_build():
        return 'Build: ' + AppVersion.APP_BUILD + ', ' + AppVersion.APP_BUILD_DATE