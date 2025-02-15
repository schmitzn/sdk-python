from datetime import datetime
from typing import List, Optional

from lemon.base import Client
from lemon.market_data.model import GetTradesResponse
from lemon.types import Sorting


class Trades:
    def __init__(self, client: Client):
        self._client = client

    def get_latest(
        self,
        isin: List[str],
        mic: Optional[str] = None,
        decimals: Optional[bool] = None,
        epoch: Optional[bool] = None,
        sorting: Optional[Sorting] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> GetTradesResponse:
        resp = self._client.get(
            "trades/latest",
            params={
                "isin": isin,
                "mic": mic,
                "decimals": decimals,
                "epoch": epoch,
                "sorting": sorting,
                "limit": limit,
                "page": page,
            },
        )
        return GetTradesResponse._from_data(
            data=resp.json(),
            t_type=float if decimals else int,
            k_type=int if epoch else datetime.fromisoformat,  # type: ignore
            client=self._client,
        )
