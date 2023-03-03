from abc import ABC, abstractmethod


class SearchParams:
    def __init__(self):
        pass


class LocomotiveFinder(ABC):

    @abstractmethod
    def find_by_locomotive_id(self, scac: str, locomotive_id: int, search_params: SearchParams):
        pass


class LocationLogRepository(LocomotiveFinder):
    def find_by_locomotive_id(self, scac: str, locomotive_id: int, search_params: SearchParams):
        pass


class StatusLogRepository:
    pass


llr = LocationLogRepository()