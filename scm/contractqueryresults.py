from flask import jsonify


class ContractQueryResults:

    def __init__(self):
        self.__shortages = []
        self.__shortages_cost = []
        self.__quantity = []
        self.__direct_cost = []
        self.__indirect_cost = []
        self.__perf = []

    def add_to_shortages(self, value):
        self.__shortages.append(value)

    def add_to_shortages_cost(self, value):
        self.__shortages_cost.append(value)

    def add_to_quantity(self, value):
        self.__quantity.append(value)

    def add_to_direct_cost(self, value):
        self.__direct_cost.append(value)

    def add_to_indirect_cost(self, value):
        self.__indirect_cost.append(value)

    def add_to_perf(self, value):
        self.__perf.append(value)

    def get_response_json(self):
        return jsonify(ls = self.__shortages.pop(0), lsc = self.__shortages_cost.pop(0), lq = self.__quantity.pop(0),
                       ldc = self.__direct_cost.pop(0), lic = self.__indirect_cost.pop(0), lp = self.__perf.pop(0),
                       ns=self.__shortages.pop(0), nsc=self.__shortages_cost.pop(0), nq=self.__quantity.pop(0),
                       ndc=self.__direct_cost.pop(0), nic=self.__indirect_cost.pop(0), np=self.__perf.pop(0),
                       vs=self.__shortages.pop(0), vsc=self.__shortages_cost.pop(0), vq=self.__quantity.pop(0),
                       vdc=self.__direct_cost.pop(0), vic=self.__indirect_cost.pop(0), vp=self.__perf.pop(0))
