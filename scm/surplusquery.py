from flask import jsonify


class SurplusQuery:

    __safety_factors = {50.0: 0.0, 75.0: 0.67, 80.0: 0.84, 85.0: 1.04, 90.0: 1.28, 94.0: 1.56,
                        95.0: 1.65, 96.0: 1.75, 97.0: 1.88, 98.0: 2.05, 99.0: 2.33, 99.86: 3.0, 99.99: 4.0}

    def __init__(self, request):
        self.__demand_per_day = self.__initialize(request, 'dd')
        self.__demand_per_week = self.__initialize(request, 'dw')
        self.__annual_demand = self.__initialize(request, 'ad')
        self.__cost_per_order = self.__initialize(request, 'cpo')
        self.__carrying_cost = self.__initialize(request, 'cc')
        self.__order_quantity = self.__initialize(request, 'oq')
        self.__lead_time = self.__initialize(request, 'lt')
        self.__review_time = 52 - self.__lead_time
        self.__rejection_cost = self.__initialize(request, 'rc')
        self.__damage_cost = self.__initialize(request, 'dc')
        self.__unavailability = self.__initialize(request, 'up')
        self.__rejection = self.__initialize(request, 'rp')
        self.__unavailability_cost = self.__initialize(request, 'uac')
        self.__inventory_cost = self.__initialize(request, 'ic')
        self.__surplus_cost = self.__initialize(request, 'sc')
        self.__shortages_cost = self.__initialize(request, 'shc')
        self.__storage_capacity = self.__initialize(request, 'stc')
        self.__standard_deviation = self.__initialize(request, 'sd')
        self.__service_level_importance = self.__initialize(request, 'sli')
        self.__safety_stock = self.__safety_factors.get(self.__service_level_importance) * self.__standard_deviation

    def __calculate_values__(self):
        surplus = self.__order_quantity - (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock)
        inv_cost = surplus * self.__inventory_cost
        project_shortages = (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock) - self.__order_quantity
        unav_cost = self.__unavailability * self.__order_quantity * self.__unavailability_cost
        rej_cost = self.__rejection * self.__order_quantity * self.__rejection_cost
        return jsonify(sq=surplus, ic=inv_cost, sh=project_shortages, uc=unav_cost, rc=rej_cost)

    def get_response_json(self):
        return self.__calculate_values__()

    def __initialize(self, request, parameter):
        value = request.args.get(parameter)
        if(value == None):
            return 0
        else:
            return float(value)


