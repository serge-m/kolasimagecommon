from typing import List
import numpy as np

from kolasimagecommon.subimage import SubImage

WIDTH_INDEX = 1


class SubimageExtractorException(Exception):
    pass


class SubimageExtractor:
    def extract(self, image: np.ndarray) -> List[SubImage]:
        raise NotImplementedError


