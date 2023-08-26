from column import Column


class Subcolumn(Column):
    """
    Class that represent single sudoku subcolumn
    """
    column: list = []

    def __init__(self, column_id: int):
        """
        Class constructor that represent single sudoku subcolumn

        :param column_id: Column identifier

        :type column_id: int
        """
        super().__init__(column_id)
