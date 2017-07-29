from typing import Iterable

import numpy as np

from kolasimagecommon.descriptor import Descriptor


class FeatureExtractor:
    def calculate(self, image: np.ndarray) -> Descriptor:
        raise NotImplementedError

    def descriptor_shape(self) -> Iterable[int]:
        raise NotImplementedError

