class Row(object):
    """
    Class that represent single sudoku row
    """

    row: list = []

    def __init__(self, row_id: int):
        """
        Class constructor that represent single sudoku row

        :param row_id: Row identifier

        :type row_id: int
        """
        self.row_id = row_id

    def exist_in_row(self, number: int) -> bool:
        """
        Methods to check if a number exists in row value list

        :param number: Number to check
        :type number: int

        :return: `True` if number is present, `False` if number is not present
        :rtype: bool
        """
        return True if number in self.row else False
