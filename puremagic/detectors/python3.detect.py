from typing import Optional, List
from pathlib import Path
import ast

from puremagic.shared import Detected, DetectorWorkflowError

name = "python3"
required = ["text"]


def detect(file_content: Optional[str, bytes] = None, content_type: str = "", chain: Optional[List[Detected]] = None) -> Detected:
    for detector in chain:
        if detector.type == "text":
            if not detector.match:
                return Detected(match=False, type=name, subtypes=[])
            break
    else:
        raise DetectorWorkflowError('"text" detector was not run before python3')


def supported() -> bool:
    return True
