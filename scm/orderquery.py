from orderqueryresults import OrderQueryResults
import math


class OrderQuery:

    __safety_factors = {50.0: 0.0, 75.0: 0.67, 80.0: 0.84, 85.0: 1.04, 90.0: 1.28, 94.0: 1.56,
                        95.0: 1.65, 96.0: 1.75, 97.0: 1.88, 98.0: 2.05, 99.0: 2.33, 99.86: 3.0, 99.99: 4.0}

    def __init__(self, request):
        self.__demand = self.__initialize(request, 'd')
        self.__annual_demand = self.__initialize(request, 'ad')
        self.__cost_per_order = self.__initialize(request, 'cpo')
        self.__carrying_cost = self.__initialize(request, 'cc')
        self.__estimated_quantity = self.__initialize(request, 'eq')
        self.__more_than_estimated_quantity = self.__initialize(request, 'meq')
        self.__less_than_estimated_quantity = self.__initialize(request, 'leq')
        self.__lead_time = self.__initialize(request, 'lt')
        self.__review_time = 52 - self.__lead_time
        self.__rejection_cost = self.__initialize(request, 'rc')
        self.__surplus_cost = self.__initialize(request, 'sc')
        self.__shortages_cost = self.__initialize(request, 'shc')
        self.__storage_capacity = self.__initialize(request, 'stc')
        self.__standard_deviation = self.__initialize(request, 'sd')
        self.__service_level_importance = self.__initialize(request, 'sli')
        self.__order_query_results = OrderQueryResults()
        self.__eoq = None
        self.__safety_stock = self.__safety_factors.get(self.__service_level_importance) * self.__standard_deviation

    def __calculate_with_estimated_quantity__(self):
        numorders = self.__annual_demand / self.__estimated_quantity
        averagecycleinv = self.__estimated_quantity / 2
        annualorderingcost = numorders * self.__cost_per_order
        annualcarryingcost = averagecycleinv * self.__carrying_cost
        self.__eoq = math.sqrt((2 * self.__annual_demand * annualorderingcost) / annualorderingcost)
        projectedshortages = (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock) - self.__estimated_quantity
        projectshortagescost = projectedshortages * self.__shortages_cost
        surplus = self.__estimated_quantity - (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock)
        surpluscost = surplus * self.__surplus_cost
        directcost = annualorderingcost + annualcarryingcost
        indirectcost = self.__shortages_cost + self.__surplus_cost + self.__rejection_cost
        self.__order_query_results.add_to_project_shortages(projectshortagescost)
        self.__order_query_results.add_to_surplus_cost(surpluscost)
        self.__order_query_results.add_to_direct_cost(directcost)
        self.__order_query_results.add_to_indirect_cost(indirectcost)

    def __calculate_with_more_than_estimated_quantity__(self):
        numorders = self.__annual_demand / self.__more_than_estimated_quantity
        averagecycleinv = self.__more_than_estimated_quantity / 2
        annualorderingcost = numorders * self.__cost_per_order
        annualcarryingcost = averagecycleinv * self.__carrying_cost
        self.__eoq = math.sqrt((2 * self.__annual_demand * annualorderingcost) / annualorderingcost)
        projectedshortages = (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock) - self.__more_than_estimated_quantity
        projectshortagescost = projectedshortages * self.__shortages_cost
        surplus = self.__more_than_estimated_quantity - (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock)
        surpluscost = surplus * self.__surplus_cost
        directcost = annualorderingcost + annualcarryingcost
        indirectcost = self.__shortages_cost + self.__surplus_cost + self.__rejection_cost
        self.__order_query_results.add_to_project_shortages(projectshortagescost)
        self.__order_query_results.add_to_surplus_cost(surpluscost)
        self.__order_query_results.add_to_direct_cost(directcost)
        self.__order_query_results.add_to_indirect_cost(indirectcost)

    def __calculate_with_less_than_estimated_quantity__(self):
        numorders = self.__annual_demand / self.__less_than_estimated_quantity
        averagecycleinv = self.__less_than_estimated_quantity / 2
        annualorderingcost = numorders * self.__cost_per_order
        annualcarryingcost = averagecycleinv * self.__carrying_cost
        self.__eoq = math.sqrt((2 * self.__annual_demand * annualorderingcost) / annualorderingcost)
        projectedshortages = (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock) - self.__less_than_estimated_quantity
        projectshortagescost = projectedshortages * self.__shortages_cost
        surplus = self.__less_than_estimated_quantity - (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock)
        surpluscost = surplus * self.__surplus_cost
        directcost = annualorderingcost + annualcarryingcost
        indirectcost = self.__shortages_cost + self.__surplus_cost + self.__rejection_cost
        self.__order_query_results.add_to_project_shortages(projectshortagescost)
        self.__order_query_results.add_to_surplus_cost(surpluscost)
        self.__order_query_results.add_to_direct_cost(directcost)
        self.__order_query_results.add_to_indirect_cost(indirectcost)

    def __calculate_with_economic_order_quantity__(self):
        numorders = self.__annual_demand / self.__eoq
        averagecycleinv = self.__eoq / 2
        annualorderingcost = numorders * self.__cost_per_order
        annualcarryingcost = averagecycleinv * self.__carrying_cost
        self.__eoq = math.sqrt((2 * self.__annual_demand * annualorderingcost) / annualorderingcost)
        projectedshortages = (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock) - self.__eoq
        projectshortagescost = projectedshortages * self.__shortages_cost
        surplus = self.__eoq - (((self.__lead_time + self.__review_time) * self.__demand) + self.__safety_stock)
        surpluscost = surplus * self.__surplus_cost
        directcost = annualorderingcost + annualcarryingcost
        indirectcost = self.__shortages_cost + self.__surplus_cost + self.__rejection_cost
        self.__order_query_results.add_to_project_shortages(projectshortagescost)
        self.__order_query_results.add_to_surplus_cost(surpluscost)
        self.__order_query_results.add_to_direct_cost(directcost)
        self.__order_query_results.add_to_indirect_cost(indirectcost)

    def get_response_json(self):
        self.__calculate_with_estimated_quantity__()
        self.__calculate_with_more_than_estimated_quantity__()
        self.__calculate_with_less_than_estimated_quantity__()
        self.__calculate_with_economic_order_quantity__()
        return self.__order_query_results.get_response_json()

    def __initialize(self, request, parameter):
        value = request.args.get(parameter)
        if(value == None):
            return 0
        else:
            return float(value)


