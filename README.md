# Vickrey Auction Simulator

A Python Flask application for simulating a Vickrey auction with a graphical user interface.

## Installation

Follow these steps to set up and run the Vickrey Auction Simulator on your local machine:

### Prerequisites

- Python 3.6 or higher installed on your system.
- pip package manager installed.

### Install

First, clone this GitHub repository to your local machine using the following command:
Navigate to the project directory
Create a virtual environment (optional but recommended)
Install the required dependencies


```bash
git clone https://github.com/Platob/Viky.git
cd Viky
python -m venv venv
pip install -r requirements.txt
```

### Run

To start the Vickrey Auction Simulator, run the following command:
```bash
python app.py
```


You should see a message indicating that the Flask development server is running. By default, the application can be accessed at http://localhost:5000 in your web browser.

---

## Usage

1. Open your web browser and go to http://localhost:5000.

2. On the home page, you can see the list of items currently on auction. You can also add new items by providing an item name and a reserve price.

3. Click on an item to view its details and submit bids. The item's name, reserve price, and bid list will be displayed. You can submit multiple bids for the same item.

4. You can navigate back to the home page to view all the items and their details.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
