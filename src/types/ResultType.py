import enum
from typing import List


class ErrorType(enum.Enum):
    NONE = 0
    PROBLEM = 1
    JUDGE = 2

class VerdictType(enum.Enum):
    ACCEPTED = 0
    PARTIAL = 1
    WRONG_ANSWER = 2
    TIME_LIMIT_EXCEEDED = 3
    RUNTIME_ERROR = 4
    SKIPPED = 5
    PROBLEM_ERROR = 6
    JUDGE_ERROR = 7



class ErrorResult():
    def __init__(self, errorType: ErrorType, errorLog: str,) -> None:
        self.errorType = errorType
        self.errorLog = errorLog
    
    def isError(self) -> bool:
        return self.errorType != ErrorType.NONE

class JudgeResultCase():
    def __init__(self, verdict: VerdictType, score:float, maxScore:float, timeUsed:int, memUsed:int, comment:str ) -> None:
        self.verdict = verdict
        self.score = score
        self.maxScore = maxScore
        self.timeUsed = timeUsed
        self.memUsed = memUsed
        self.comment = comment

class JudgeResult():
    def __init__(self, dispResult: str, score: float, maxScore: float, timeUsed: int, memUsed: int, details: List[JudgeResultCase], error: ErrorResult) -> None:
        self.dispResult = dispResult
        self.score = score
        self.maxScore = maxScore
        self.timeUsed = timeUsed
        self.memUsed = memUsed
        self.details = details
        self.error = error
