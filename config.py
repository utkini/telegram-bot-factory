from pathlib import Path

import yaml


class YAMLReader:
    # tmp_path = Path(tempfile.gettempdir())
    tmp_path = Path('/Users/igor/feed')

    def __init__(self, yaml_path):
        self.yaml_path = yaml_path
        with open(self.yaml_path) as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
        self.actions = self.data.get('actions')

    def get_webhook(self, name):
        webhooks = dict()
        commands = self.actions.get('behaviors').get('commands')
        for command in commands:
            webhooks[command.get('name')] = command.get('webhook')

        files = self.actions.get('behaviors').get('files')
        for file in files:
            file_extension = file.get('type')[0]
            file_type = self.get_file_type(file_extension)
            webhooks[file_type] = file.get('webhook')

        regexps = self.actions.get('behaviors').get('regexp')
        for regexp in regexps:
            webhooks[regexp.get('pattern')] = regexp.get('webhook')

        return webhooks.get(name)

    def get_file_type(self, extension):
        file_types = self.data.get('extensions')
        for file_type in file_types:
            extensions = file_type.get('type')
            if extension in extensions:
                return file_type.get('name')

    @property
    def bot_token(self):
        return self.data.get('bot-token')

    @property
    def login(self):
        return self.data.get('rpa-login')

    @property
    def password(self):
        return self.data.get('rpa-password')

    @property
    def base_url(self):
        return self.data.get('rpa-base-url')

    @property
    def start_description(self):
        return self.actions.get('start').get('response-msg')

    @property
    def help_description(self):
        return self.actions.get('help').get('response-msg')

    @property
    def supported_behaviours(self):
        behaviors = self.actions.get('behaviors')
        return list(behaviors.keys())

    def get_commands(self):
        commands = self.actions.get('behaviors').get('commands')
        for command in commands:
            yield command.get('name'), command.get('webhook')

    def get_files(self):
        files = self.actions.get('behaviors').get('files')
        for file in files:
            yield file.get('type'), file.get('webhook')

    def get_regexp(self):
        regexps = self.actions.get('behaviors').get('regexp')
        for regexp in regexps:
            yield regexp.get('pattern'), regexp.get('webhook')


yaml_path = 'config_bot.yaml'
CONFIG = YAMLReader(yaml_path=yaml_path)

