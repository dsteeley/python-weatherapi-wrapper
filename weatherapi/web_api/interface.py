import datetime as dt
from typing import Union

import requests

from weatherapi.constants import Parameters, Endpoints
import logger

class APINotCalledException(Exception):
    pass


class APICaller:
    def __init__(self, api_key):
        self.key = api_key

    def get_history(
        self,
        latitude: float,
        longitude: float,
        day: dt.date,
        hour: Union[int, None] = None,
    ) -> dict:
        request_parameters = self._build_parameters_dict(
            latitude=latitude, longitude=longitude, day=day, hour=hour
        )
        return self._call_api(Endpoints.history, params=request_parameters).json()

    def get_forecast(
        self,
        latitude: float,
        longitude: float,
        day: dt.date,
        hour: Union[int, None] = None,
    ) -> dict:
        request_parameters = self._build_parameters_dict(
                latitude=latitude, longitude=longitude, day=day, hour=hour
            )
        return self._call_api(Endpoints.forecast, params=request_parameters).json()

    def _call_api(self, endpoint, parameters):
        response = requests.get(endpoint, params=parameters)
        if not response.status_code == 200:
            raise APINotCalledException(response.text)
        logger.debug(f"Get weatherapi response {response.json()}")
        return response

    def _build_parameters_dict(self, latitude, longitude, day, hour=None) -> dict:
        parameters = {
            Parameters.key: self.key,
            Parameters.location: f"{latitude},{longitude}",
            Parameters.date: day.strftime("%Y-%m-%d"),
        }
        if hour is not None:
            parameters.update({Parameters.hour: hour})
        logger.debug(f"Build parameters dict {parameters}")
        return parameters
