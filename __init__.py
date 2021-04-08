from mycroft import MycroftSkill, intent_file_handler


class FootballInformation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('information.football.intent')
    def handle_information_football(self, message):
        self.speak_dialog('information.football')


def create_skill():
    return FootballInformation()

