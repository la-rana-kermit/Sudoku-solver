class Cell(object):
    """
    Class that represent single sudoku cell

    :param candidates: Possible value candidate for cell
    :type candidates: List
    """
    candidates = []

    def __init__(self, column, sub_column, row, sub_row, subgrid_column, subgrid_row, value):
        """
        Class constructor that represent single sudoku cell

        :param column: Cell column identifier
        :param sub_column: Cell column in subgrid identifier
        :param row: Cell row identifier
        :param sub_row: Cell row in subgrid identifier
        :param subgrid_column: Cell subgrid column identifier
        :param subgrid_row: Cell subgrid row identifier
        :param value: Cell value

        :type column: int
        :type sub_column: int
        :type row: int
        :type sub_row: int
        :type subgrid_column: int
        :type subgrid_row: int
        :type value: int
        """
        self.column = column
        self.sub_column = sub_column
        self.row = row
        self.sub_row = sub_row
        self.subgrid_column = subgrid_column
        self.subgrid_row = subgrid_row
        self.value = value

    def add_candidate(self, new_candidate):
        """
        Method to add possible new candidate in candidates list

        :param new_candidate: Possible new candidate
        :type new_candidate: int
        """
        if not self.is_candidate(new_candidate):
            self.candidates.append(new_candidate)
            self.candidates.sort()

    def add_value(self, new_value):
        """
        Method to update value in cell and consequently empty candidates list

        :param new_value: New cell value
        :type new_value: int
        """
        if self.is_candidate(new_value):
            self.value = new_value
            self.candidates.clear()

    def is_candidate(self, possible_candidate):
        """
        Method to check if a possible candidate is in candidates list

        :param possible_candidate: Possible candidate
        :type possible_candidate: int

        :return: `True` if candidate is present, `False` if candidate is not present
        :rtype: bool
        """
        return True if possible_candidate in self.candidates else False

    def remove_candidate(self, candidate):
        """
        Method to remove existing candidate in candidates list

        :param candidate: Existing candidate
        :type candidate: int
        """
        if self.is_candidate(candidate):
            self.candidates.remove(candidate)
