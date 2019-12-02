from flask import jsonify


class OrderQueryResults:

    def __init__(self):
        self.__project_shortages = []
        self.__surplus_cost = []
        self.__direct_cost = []
        self.__indirect_cost = []

    def add_to_project_shortages(self, value):
        self.__project_shortages.append(value)

    def add_to_surplus_cost(self, value):
        self.__surplus_cost.append(value)

    def add_to_direct_cost(self, value):
        self.__direct_cost.append(value)

    def add_to_indirect_cost(self, value):
        self.__indirect_cost.append(value)

    def get_response_json(self):
        return jsonify(ps=self.__project_shortages.pop(0), sc=self.__surplus_cost.pop(0),
                       dc=self.__direct_cost.pop(0), idc=self.__indirect_cost.pop(0),
                       mps=self.__project_shortages.pop(0), msc=self.__surplus_cost.pop(0),
                       mdc=self.__direct_cost.pop(0), midc=self.__indirect_cost.pop(0),
                       lps=self.__project_shortages.pop(0), lsc=self.__surplus_cost.pop(0),
                       ldc=self.__direct_cost.pop(0), lidc=self.__indirect_cost.pop(0),
                       eps=self.__project_shortages.pop(0), esc=self.__surplus_cost.pop(0),
                       edc=self.__direct_cost.pop(0), eidc=self.__indirect_cost.pop(0))
