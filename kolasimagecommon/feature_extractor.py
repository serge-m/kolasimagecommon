from typing import List

import numpy as np

from kolasimagecommon.descriptor import Descriptor


class FeatureExtractor:
    def calculate(self, image: np.ndarray) -> Descriptor:
        raise NotImplementedError


