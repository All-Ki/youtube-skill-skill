from mycroft import MycroftSkill, intent_file_handler


class YoutubeSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.youtube.intent')
    def handle_skill_youtube(self, message):
        self.speak_dialog('skill.youtube')


def create_skill():
    return YoutubeSkill()

