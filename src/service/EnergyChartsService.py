from src.utils.metric import create_metric
from src.utils.apiClient import ApiClient


class EnergyChartsService:
    def __init__(self):
        self.energy_data = ""
        self.api_client = ApiClient("https://api.energy-charts.info/v1/")

    def collect_data(self):
        '''
        Collect the data
        :return:
        '''

        # https://api.energy-charts.info/#/prices/day_ahead_price_price_get

        current_data = {}

        return current_data

    async def fetch_energy_data(self):
        """
        Fetch energy data from
        :return:
        """
        key = "a"
        value = "b"
        data = self.collect_data()
        metric = create_metric("energycharts", data, key, value)
        self.energy_data = '\n'.join(metric)
