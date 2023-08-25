class Cell(object):
    """
    Class that represent single sudoku cell

    :param candidates: Possible value candidate for cell
    :type candidates: List
    """
    candidates: list = []

    def __init__(self, column_id: int, sub_column_id: int, row_id: int, sub_row_id: int, subgrid_column_id: int, subgrid_row_id: int, value: int):
        """
        Class constructor that represent single sudoku cell

        :param column_id: Cell column identifier
        :param sub_column_id: Cell column in subgrid identifier
        :param row_id: Cell row identifier
        :param sub_row_id: Cell row in subgrid identifier
        :param subgrid_column_id: Cell subgrid column identifier
        :param subgrid_row_id: Cell subgrid row identifier
        :param value: Cell value

        :type column_id: int
        :type sub_column_id: int
        :type row_id: int
        :type sub_row_id: int
        :type subgrid_column_id: int
        :type subgrid_row_id: int
        :type value: int
        """
        self.column_id = column_id
        self.sub_column_id = sub_column_id
        self.row_id = row_id
        self.sub_row_id = sub_row_id
        self.subgrid_column_id = subgrid_column_id
        self.subgrid_row_id = subgrid_row_id
        self.value = value

    def add_candidate(self, new_candidate: int):
        """
        Method to add possible new candidate in candidates list

        :param new_candidate: Possible new candidate
        :type new_candidate: int
        """
        if not self.is_candidate(new_candidate):
            self.candidates.append(new_candidate)
            self.candidates.sort()

    def add_value(self, new_value: int):
        """
        Method to update value in cell and consequently empty candidates list

        :param new_value: New cell value
        :type new_value: int
        """
        if self.is_candidate(new_value):
            self.value = new_value
            self.candidates.clear()

    def is_candidate(self, possible_candidate) -> bool:
        """
        Method to check if a possible candidate is in candidates list

        :param possible_candidate: Possible candidate
        :type possible_candidate: int

        :return: `True` if candidate is present, `False` if candidate is not present
        :rtype: bool
        """
        return True if possible_candidate in self.candidates else False

    def remove_candidate(self, candidate: int):
        """
        Method to remove existing candidate in candidates list

        :param candidate: Existing candidate
        :type candidate: int
        """
        if self.is_candidate(candidate):
            self.candidates.remove(candidate)
