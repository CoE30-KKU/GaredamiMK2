
class Submission():
    def __init__(self, submissionId:str, lang:str, problem:str, code:str, problemSetting) -> None:
        self.submissionId = submissionId
        self.lang = lang
        self.problem = problem
        self.code = code
        self.problemSetting = problemSetting
        