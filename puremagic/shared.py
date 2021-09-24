from collections import namedtuple

__all__ = ["Detected", "DetectorWorkflowError", "PureMagic", "PureMagicWithConfidence", "PureError"]

MAGIC_INFO_TYPES = (
    "byte_match",
    "offset",
    "extension",
    "mime_type",
    "name",
)

PureMagic = namedtuple("PureMagic", MAGIC_INFO_TYPES)  # type: ignore
PureMagicWithConfidence = namedtuple("PureMagicWithConfidence", (MAGIC_INFO_TYPES + ("confidence",)))  # type: ignore
Detected = namedtuple("Detected", ["match", "type", "subtypes"])


class PureError(LookupError):
    """Do not have that type of file in our databanks"""

class DetectorWorkflowError(PureError):
    """Internal logic error"""
