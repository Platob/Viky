__all__ = [
    "Item"
]

from typing import Optional


class Item:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.bids: dict[str, set[float]] = {}

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Item(name="%s")' % self.name

    def add_bid(self, owner: str, price: float):
        bids = self.bids.get(owner, set())
        bids.add(price)
        self.bids[owner] = bids

    def owner_bids(self, exclude_owner: str = None):
        # ventilate all bids by owner
        for (owner, bids) in self.bids.items():
            if owner != exclude_owner:
                for bid in bids:
                    yield owner, bid

    def winning_bidder(self, exclude_owner: str = None) -> Optional[tuple[str, float]]:
        winner = None
        max_price = self.price

        for (owner, bid) in self.owner_bids(exclude_owner=exclude_owner):
            if bid > max_price:
                winner = (owner, bid)
                max_price = bid

        return winner

    def winning_price(self) -> Optional[tuple[str, float]]:
        winner = self.winning_bidder()

        if winner:
            # Return the best price with the best bidder name
            new_winner = self.winning_bidder(exclude_owner=winner[0])
            if new_winner:
                return winner[0], new_winner[1]
        return None
