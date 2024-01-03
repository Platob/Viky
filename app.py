from flask import Flask, render_template, request, redirect, url_for
from viky.model import Item

app = Flask(__name__)

# Initialize data storage for bids and auction item
auction_items: dict[str, Item] = {
    "toto": Item("toto", 100)
}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_item = Item(name=request.form['item_name'], price=float(request.form['reserve_price']))
        auction_items[new_item.name] = new_item

    return render_template('home.html', items=auction_items.values())


@app.route('/item/<name>', methods=['GET', 'POST'])
def item_page(name):
    item = auction_items.get(name)
    if not item:
        return "Item not found", 404

    if request.method == 'POST':
        owner = request.form['owner']
        bid = float(request.form['bid'])
        item.add_bid(owner=owner, price=bid)

    winner = item.winning_price()

    if winner:
        owner, bid = winner
    else:
        owner, bid = None, None

    return render_template('item.html', item=item, owner=owner, bid=bid)


@app.route('/item/<name>/reset', methods=['GET', 'POST'])
def item_reset(name):
    item = auction_items.get(name)
    if not item:
        return "Item not found", 404

    item.bids.clear()

    return redirect(url_for('item_page', name=name))


@app.route('/add_item', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    reserve_price = float(request.form['reserve_price'])
    auction_items[item_name] = Item(item_name, reserve_price)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
