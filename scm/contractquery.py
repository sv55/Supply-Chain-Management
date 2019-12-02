from contractqueryresults import ContractQueryResults


class ContractQuery:

    __safety_factors = {50.0: 0.0, 75.0: 0.67, 80.0: 0.84, 85.0: 1.04, 90.0: 1.28, 94.0: 1.56,
                        95.0: 1.65, 96.0: 1.75, 97.0: 1.88, 98.0: 2.05, 99.0: 2.33, 99.86: 3.0, 99.99: 4.0}

    def __init__(self, request):
        self.__demand = self.__initialize(request, 'd')
        self.__annual_demand = self.__initialize(request, 'ad')
        self.__no_of_orders = self.__initialize(request, 'npo')
        self.__unit_cost = self.__initialize(request, 'uc')
        self.__cost_per_order_local = self.__initialize(request, 'cpol')
        self.__cost_per_order_nonlocal = self.__initialize(request, 'cpon')
        self.__cost_per_order_vmi = self.__initialize(request, 'cpov')
        self.__carrying_cost_local = self.__initialize(request, 'ccl')
        self.__carrying_cost_nonlocal = self.__initialize(request, 'ccn')
        self.__carrying_cost_vmi = self.__initialize(request, 'ccv')
        self.__order_quantity = self.__initialize(request, 'oq')
        self.__lead_time_local = self.__initialize(request, 'ltl')
        self.__lead_time_nonlocal = self.__initialize(request, 'ltn')
        self.__lead_time_vmi = self.__initialize(request, 'ltv')
        self.__review_time_local = 52 - self.__lead_time_local
        self.__review_time_nonlocal = 52 - self.__lead_time_nonlocal
        self.__review_time_vmi = 52 - self.__lead_time_vmi
        self.__availability_local = self.__initialize(request, 'al')
        self.__availability_nonlocal = self.__initialize(request, 'an')
        self.__availability_vmi = self.__initialize(request, 'av')
        self.__availability_cost_local = self.__initialize(request, 'acl')
        self.__availability_cost_nonlocal = self.__initialize(request, 'acn')
        self.__availability_cost_vmi = self.__initialize(request, 'acv')
        self.__backorders_local = self.__initialize(request, 'bol')
        self.__backorders_nonlocal = self.__initialize(request, 'bon')
        self.__backorders_vmi = self.__initialize(request, 'bov')
        self.__uncertainity_local = self.__initialize(request, 'ucl')
        self.__uncertainity_nonlocal = self.__initialize(request, 'ucn')
        self.__uncertainity_vmi = self.__initialize(request, 'ucv')
        self.__rejection_cost = self.__initialize(request, 'rc')
        self.__surplus_cost = self.__initialize(request, 'sc')
        self.__transportation_cost = self.__initialize(request, 'tc')
        self.__shortages_cost = self.__initialize(request, 'shc')
        self.__storage_capacity = self.__initialize(request, 'stc')
        self.__standard_deviation = self.__initialize(request, 'sd')
        self.__service_level_importance = self.__initialize(request, 'sli')
        self.__contract_query_resutls = ContractQueryResults()
        self.__safety_stock = self.__safety_factors.get(self.__service_level_importance) * self.__standard_deviation
        self.__distance_local = self.__initialize(request, 'dl')
        self.__distance_nonlocal = self.__initialize(request, 'dn')
        self.__distance_vmi = self.__initialize(request, 'dv')

    def __calculate_for_local__(self):
        projected_shortages = (((self.__lead_time_local + self.__review_time_local) * self.__demand) + self.__safety_stock) - self.__order_quantity
        projected_shrotages_cost = projected_shortages * self.__shortages_cost
        quantity = (self.__demand * (self.__lead_time_local + self.__review_time_local)) + self.__safety_stock
        ordering_cost = self.__no_of_orders * self.__cost_per_order_local
        carrying_cost = quantity * self.__carrying_cost_local
        direct_cost = ordering_cost + carrying_cost
        unav_cost = self.__availability_cost_local * self.__availability_local * self.__order_quantity
        laiddown_cost = self.__unit_cost + (self.__distance_local * self.__transportation_cost)
        indirect_cost = projected_shrotages_cost + unav_cost + laiddown_cost
        quality = 'None'
        if self.__lead_time_local < 2 and self.__backorders_local < 10 and self.__uncertainity_local < 10:
            quality = 'Excellent'
        if self.__lead_time_local < 5 and self.__backorders_local < 50 and self.__uncertainity_local < 20:
            quality = 'Good'
        if self.__lead_time_local < 5 and self.__backorders_local < 50 and self.__uncertainity_local > 20:
            quality = 'Bad'
        self.__contract_query_resutls.add_to_shortages(projected_shortages)
        self.__contract_query_resutls.add_to_shortages_cost(projected_shrotages_cost)
        self.__contract_query_resutls.add_to_quantity(quantity)
        self.__contract_query_resutls.add_to_direct_cost(direct_cost)
        self.__contract_query_resutls.add_to_indirect_cost(indirect_cost)
        self.__contract_query_resutls.add_to_perf(quality)

    def __calculate_for_vmi__(self):
        projected_shortages = (((self.__lead_time_vmi + self.__review_time_vmi) * self.__demand) + self.__safety_stock) - self.__order_quantity
        projected_shrotages_cost = projected_shortages * self.__shortages_cost
        quantity = (self.__demand * (self.__lead_time_vmi + self.__review_time_vmi)) + self.__safety_stock
        ordering_cost = self.__no_of_orders * self.__cost_per_order_vmi
        carrying_cost = quantity * self.__carrying_cost_vmi
        direct_cost = ordering_cost + carrying_cost
        unav_cost = self.__availability_cost_vmi * self.__availability_vmi * self.__order_quantity
        laiddown_cost = self.__unit_cost + (self.__distance_vmi * self.__transportation_cost)
        indirect_cost = projected_shrotages_cost + unav_cost + laiddown_cost
        quality = 'None'
        if self.__lead_time_vmi < 2 and self.__backorders_vmi < 10 and self.__uncertainity_vmi < 10:
            quality = 'Excellent'
        if self.__lead_time_vmi < 5 and self.__backorders_vmi < 50 and self.__uncertainity_vmi < 20:
            quality = 'Good'
        if self.__lead_time_vmi < 5 and self.__backorders_vmi < 50 and self.__uncertainity_vmi > 20:
            quality = 'Bad'
        self.__contract_query_resutls.add_to_shortages(projected_shortages)
        self.__contract_query_resutls.add_to_shortages_cost(projected_shrotages_cost)
        self.__contract_query_resutls.add_to_quantity(quantity)
        self.__contract_query_resutls.add_to_direct_cost(direct_cost)
        self.__contract_query_resutls.add_to_indirect_cost(indirect_cost)
        self.__contract_query_resutls.add_to_perf(quality)

    def __calculate_for_nonlocal__(self):
        projected_shortages = (((self.__lead_time_nonlocal + self.__review_time_nonlocal) * self.__demand) + self.__safety_stock) - self.__order_quantity
        projected_shrotages_cost = projected_shortages * self.__shortages_cost
        quantity = (self.__demand * (self.__lead_time_nonlocal + self.__review_time_nonlocal)) + self.__safety_stock
        ordering_cost = self.__no_of_orders * self.__cost_per_order_nonlocal
        carrying_cost = quantity * self.__carrying_cost_nonlocal
        direct_cost = ordering_cost + carrying_cost
        unav_cost = self.__availability_cost_nonlocal * self.__availability_nonlocal * self.__order_quantity
        laiddown_cost = self.__unit_cost + (self.__distance_nonlocal * self.__transportation_cost)
        indirect_cost = projected_shrotages_cost + unav_cost + laiddown_cost
        quality = 'None'
        if self.__lead_time_nonlocal < 2 and self.__backorders_nonlocal < 10 and self.__uncertainity_nonlocal < 10:
            quality = 'Excellent'
        if self.__lead_time_nonlocal < 5 and self.__backorders_nonlocal < 50 and self.__uncertainity_nonlocal < 20:
            quality = 'Good'
        if self.__lead_time_nonlocal < 5 and self.__backorders_nonlocal < 50 and self.__uncertainity_nonlocal > 20:
            quality = 'Bad'
        self.__contract_query_resutls.add_to_shortages(projected_shortages)
        self.__contract_query_resutls.add_to_shortages_cost(projected_shrotages_cost)
        self.__contract_query_resutls.add_to_quantity(quantity)
        self.__contract_query_resutls.add_to_direct_cost(direct_cost)
        self.__contract_query_resutls.add_to_indirect_cost(indirect_cost)
        self.__contract_query_resutls.add_to_perf(quality)

    def get_response_json(self):
        self.__calculate_for_local__()
        self.__calculate_for_nonlocal__()
        self.__calculate_for_vmi__()
        return self.__contract_query_resutls.get_response_json()

    def __initialize(self, request, parameter):
        value = request.args.get(parameter)
        if(value == None):
            return 0
        else:
            return float(value)


