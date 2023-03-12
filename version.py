# -*- coding: utf-8 -*-

# version information of the application
class AppVersion:
    APP_VERSION = '1.0.0'
    APP_BUILD = '97'
    APP_BUILD_DATE = '2023-03-11'

    @staticmethod
    def get_version():
        return 'Version: ' + AppVersion.APP_VERSION

    @staticmethod
    def get_build():
        return 'Build: ' + AppVersion.APP_BUILD + ', ' + AppVersion.APP_BUILD_DATE