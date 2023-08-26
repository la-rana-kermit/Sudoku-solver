from row import Row


class Subrow(Row):
    """
    Class that represent single sudoku subrow
    """
    row: list = []

    def __init__(self, row_id: int):
        """
        Class constructor that represent single sudoku subrow

        :param row_id: Row identifier

        :type row_id: int
        """
        super().__init__(row_id)
