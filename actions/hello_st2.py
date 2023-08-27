import os
from st2common.runners.base_action import Action

class HelloStackStorm(Action):
    def run(self):
        os.system("bash test_api_call.sh")
        print("Hello Stackstorm, want to be friends?")
        return True, "Let's be friends!"
