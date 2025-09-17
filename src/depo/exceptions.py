class Missing(Exception):
    def __init__(self, message: str):
        self.message = message

class DepoWarning(Warning):
    def __init__(self, message: str):
        self.message = message