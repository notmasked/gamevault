# GameVault

GameVault is a Python command-line application that uses Pandas to explore and analyze a dataset of 10,000 video games.

## Features

* Search games by name
* Browse top-rated games
* Browse games by genre
* Browse games by release year
* Sort games by rating and release year
* Load games in batches
* Random game selection
* Handles missing data in the dataset
* Uses Pandas for data filtering, sorting, and analysis

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the source code.
3. Install the required dependency:

```bash
pip install pandas
```

4. Open a terminal in the project folder.
5. Run:

```bash
python main.py
```

## Usage

* Search for games by entering part or all of a game's name.
* Browse the highest-rated games.
* Browse games by genre.
* Browse games by release year in ascending or descending order.
* Load more results when browsing large lists.
* Generate a random game to discover something to play.

## Project Structure

```text
gamevault/
│
├── main.py
├── README.md
├── LICENSE
│
└── data/
    └── games_data_10k.csv
```

## Files

* `main.py` – Main GameVault application
* `data/games_data_10k.csv` – 10,000-game dataset used by the application
* `README.md` – Project documentation
* `LICENSE` – MIT License

## Author

**Harshad Sawant**

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
