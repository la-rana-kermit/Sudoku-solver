class Column(object):
    """
    Class that represent single sudoku column
    """

    column: list = []

    def __init__(self, column_id: int):
        """
        Class constructor that represent single sudoku column

        :param column_id: Column identifier

        :type column_id: int
        """
        self.column_id = column_id

    def exist_in_column(self, number: int):
        """
        Methods to check if a number exists in column value list

        :param number: Number to check
        :type number: int
        """
        return True if number in self.column else False
