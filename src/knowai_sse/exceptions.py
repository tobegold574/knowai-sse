class SSEError(Exception):
    pass


class LLMTimeoutError(SSEError):
    pass


class LLMParseError(SSEError):
    pass


class PromptBuildError(SSEError):
    pass
