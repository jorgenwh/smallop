import typing


class Shape():
    def __init__(self, *args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"Shape arguments must be integers, not {type(arg)}")

        self.shape = list(args)

    def __str__(self):
        return f"Shape{self.shape}"


ShapeType = typing.Union[
        int, 
        typing.List[int], 
        typing.Tuple[int, ...],
        Shape,
]

DataType = typing.Union[
        typing.List[float],
]

class Tensor():
    def __init__(self, data: DataType = [], shape: ShapeType = 0):
        self.data = data
        self.shape = Shape(shape)

    @property
    def shape(self) -> Shape:
        return self.shape

    def __str__(self):
        return f"Tensor({self.data}, {self.shape})"

    def __repr__(self):
        return self.__str__()

