import numpy as np
from collections import Iterable


class Descriptor:
    def __init__(self, vector: np.ndarray):
        assert isinstance(vector, np.ndarray) or isinstance(vector, Iterable), "vector must be a numpy array"
        self._vector = np.array(vector)

    @property
    def vector(self) -> np.ndarray:
        return self._vector

    @property
    def vector_as_lists(self) -> Iterable:
        return self._vector.tolist()

    def __eq__(self, other):
        if isinstance(other, Descriptor):
            return np.array_equal(self.vector, other.vector)
        raise NotImplementedError("Comparison not implemented for a given type")



