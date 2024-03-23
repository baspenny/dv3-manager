import structlog
from structlog import PrintLogger, ReturnLogger


def get_logger() -> ReturnLogger:
    logger = structlog.get_logger()

    def set_severity(_logger: PrintLogger, __log_method, event_dict):
        event_dict["severity"] = __log_method.upper()
        return event_dict

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            set_severity,
            structlog.processors.EventRenamer("message"),
            structlog.processors.JSONRenderer(),
        ]
    )
    return logger
