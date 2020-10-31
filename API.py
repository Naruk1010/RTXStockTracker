import configparser
import sys


class API:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config")

        self.API_KEY = self.config.get("SECRETS", "ApiKey", fallback="NoKey")
        self.API_SECRET = self.config.get("SECRETS", "ApiSecret", fallback="NoSecret")
        self.ACCESS_TOKEN = self.config.get("SECRETS", "AccessToken", fallback="NoAccessToken")
        self.ACCESS_TOKEN_SECRET = self.config.get("SECRETS", "AccessTokenSecret", fallback="NoAccessTokenSecret")

        if "NoKey" in self.API_KEY:
            print("No API key found. Please set one in the config file.")
            sys.exit(0)

        if "NoSecret" in self.API_SECRET:
            print("No API secret found. Please set one in the config file.")
            sys.exit(0)

        if "NoAccessToken" in self.ACCESS_TOKEN:
            print("No API bearer found. Please set one in the config file.")
            sys.exit(0)

        if "NoAccessTokenSecret" in self.ACCESS_TOKEN_SECRET:
            print("No API bearer found. Please set one in the config file.")
            sys.exit(0)

    def getAPIKey(self):
        return self.API_KEY

    def getAPISecret(self):
        return self.API_SECRET

    def getAPIBearer(self):
        return self.API_BEARER

    def getAccessToken(self):
        return self.ACCESS_TOKEN

    def getAccessTokenSecret(self):
        return self.ACCESS_TOKEN_SECRET