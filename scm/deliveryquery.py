from deliveryqueryresults import DeliveryQueryResults


class DeliverQuery:

    __safety_factors = {50.0: 0.0, 75.0: 0.67, 80.0: 0.84, 85.0: 1.04, 90.0: 1.28, 94.0: 1.56,
                        95.0: 1.65, 96.0: 1.75, 97.0: 1.88, 98.0: 2.05, 99.0: 2.33, 99.86: 3.0, 99.99: 4.0}

    def __init__(self, request):
        self.__demand_per_week = self.__initialize(request, 'd')
        self.__annual_demand = self.__initialize(request, 'ad')
        self.__no_of_orders = self.__initialize(request, 'npo')
        self.__cost_per_order = self.__initialize(request, 'cpo')
        self.__unit_cost = self.__initialize(request, 'uc')
        self.__carrying_cost = self.__initialize(request, 'cc')
        self.__order_quantity = self.__initialize(request, 'oq')
        self.__lead_time = self.__initialize(request, 'lt')
        self.__review_time = 52 - self.__lead_time
        self.__rejection_cost = self.__initialize(request, 'rc')
        self.__surplus_cost = self.__initialize(request, 'sc')
        self.__shortages_cost = self.__initialize(request, 'shc')
        self.__storage_capacity_jobsite = self.__initialize(request, 'stcj')
        self.__storage_capacity_warehouse = self.__initialize(request, 'stcw')
        self.__storage_capacity_subc = self.__initialize(request, 'stcs')
        self.__standard_deviation = self.__initialize(request, 'sd')
        self.__service_level_importance = self.__initialize(request, 'sli')
        self.__safety_stock = self.__safety_factors.get(self.__service_level_importance) * self.__standard_deviation
        self.__distance_jobsite = self.__initialize(request, 'dj')
        self.__distance_warehouse = self.__initialize(request, 'dwh')
        self.__distance_subc = self.__initialize(request, 'dsc')
        self.__transport_cost = self.__initialize(request, 'tc')
        self.__inventory_jobsite = self.__initialize(request, 'ij')
        self.__inventory_warehouse = self.__initialize(request, 'iw')
        self.__inventory_subc = self.__initialize(request, 'is')
        self.__delivery_results = DeliveryQueryResults()

    def __calculate_values_for_jobsite__(self):
        quantity_of_material = self.__storage_capacity_jobsite - self.__inventory_jobsite
        no_of_orders = self.__annual_demand / self.__no_of_orders
        annual_ordering_cost = no_of_orders * self.__cost_per_order
        avg_cycle_inv = self.__order_quantity / 2
        annual_holding_cost = avg_cycle_inv * self.__carrying_cost
        direct_cost = annual_holding_cost + annual_ordering_cost
        project_shortages = (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock) - self.__order_quantity
        project_shortages_cost = project_shortages * self.__shortages_cost
        surplus = self.__order_quantity - (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock)
        surplus_cost = surplus * self.__surplus_cost
        laid_down_cost = self.__unit_cost + (self.__distance_jobsite * self.__transport_cost)
        indirect_cost = project_shortages_cost + surplus_cost + laid_down_cost
        self.__delivery_results.add_to_quantity(quantity_of_material)
        self.__delivery_results.add_to_direct_cost(direct_cost)
        self.__delivery_results.add_to_indirect_cost(indirect_cost)

    def __calculate_values_for_subc__(self):
        quantity_of_material = self.__storage_capacity_subc - self.__inventory_subc
        no_of_orders = self.__annual_demand / self.__no_of_orders
        annual_ordering_cost = no_of_orders * self.__cost_per_order
        avg_cycle_inv = self.__order_quantity / 2
        annual_holding_cost = avg_cycle_inv * self.__carrying_cost
        direct_cost = annual_holding_cost + annual_ordering_cost
        project_shortages = (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock) - self.__order_quantity
        project_shortages_cost = project_shortages * self.__shortages_cost
        surplus = self.__order_quantity - (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock)
        surplus_cost = surplus * self.__surplus_cost
        laid_down_cost = self.__unit_cost + (self.__distance_subc * self.__transport_cost)
        indirect_cost = project_shortages_cost + surplus_cost + laid_down_cost
        self.__delivery_results.add_to_quantity(quantity_of_material)
        self.__delivery_results.add_to_direct_cost(direct_cost)
        self.__delivery_results.add_to_indirect_cost(indirect_cost)

    def __calculate_values_for_warehouse__(self):
        quantity_of_material = self.__storage_capacity_warehouse - self.__inventory_warehouse
        no_of_orders = self.__annual_demand / self.__no_of_orders
        annual_ordering_cost = no_of_orders * self.__cost_per_order
        avg_cycle_inv = self.__order_quantity / 2
        annual_holding_cost = avg_cycle_inv * self.__carrying_cost
        direct_cost = annual_holding_cost + annual_ordering_cost
        project_shortages = (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock) - self.__order_quantity
        project_shortages_cost = project_shortages * self.__shortages_cost
        surplus = self.__order_quantity - (((self.__lead_time + self.__review_time) * self.__demand_per_week) + self.__safety_stock)
        surplus_cost = surplus * self.__surplus_cost
        laid_down_cost = self.__unit_cost + (self.__distance_warehouse * self.__transport_cost)
        indirect_cost = project_shortages_cost + surplus_cost + laid_down_cost
        self.__delivery_results.add_to_quantity(quantity_of_material)
        self.__delivery_results.add_to_direct_cost(direct_cost)
        self.__delivery_results.add_to_indirect_cost(indirect_cost)

    def get_response_json(self):
        self.__calculate_values_for_jobsite__()
        self.__calculate_values_for_warehouse__()
        self.__calculate_values_for_subc__()
        return self.__delivery_results.get_response_json()

    def __initialize(self, request, parameter):
        value = request.args.get(parameter)
        if(value == None):
            return 0
        else:
            return float(value)


