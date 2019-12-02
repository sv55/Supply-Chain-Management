from flask import jsonify


class DeliveryQueryResults:

    def __init__(self):
        self.__quantity = []
        self.__direct_cost = []
        self.__indirect_cost = []

    def add_to_quantity(self, value):
        self.__quantity.append(value)

    def add_to_direct_cost(self, value):
        self.__direct_cost.append(value)

    def add_to_indirect_cost(self, value):
        self.__indirect_cost.append(value)

    def get_response_json(self):
        return jsonify(jq=self.__quantity.pop(0),
                       jdc=self.__direct_cost.pop(0), jidc=self.__indirect_cost.pop(0),
                       wq=self.__quantity.pop(0),
                       wdc=self.__direct_cost.pop(0), widc=self.__indirect_cost.pop(0),
                       sq=self.__quantity.pop(0),
                       sdc=self.__direct_cost.pop(0), sidc=self.__indirect_cost.pop(0))
