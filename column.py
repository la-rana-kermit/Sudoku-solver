class Column(object):
    """
    Class that represent single sudoku column
    """

    column: list = []

    def __init__(self, column: list):
        """
        Class constructor that represent single sudoku column

        :param column: Column identifier

        :type column: int
        """
        self.column = column

    def exist_in_column(self, number: int):
        """
        Methods to check if a number exists in column value list

        :param number: Number to check
        :type number: int
        """
        return True if number in self.column else False
