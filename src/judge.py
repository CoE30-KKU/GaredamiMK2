from src.types import JudgeResult, Submission

class Judge():

    def _initJudge(self) -> None:
        #? Judge setup
        pass

    def __init__(self) -> None:
        self._initJudge()
    
    def Judge(self, submission: Submission) -> JudgeResult:
        #? big Judge submission
        return JudgeResult("Accepted", 100, 100, 0, 0, [], None)