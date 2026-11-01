# Python for AI

Practice code from learning Python, with the aim of using it for AI and data work.

`hello.py` works through the basics in order: strings, conditionals, loops, lists and dictionaries, functions and the standard library. It then calls the Open-Meteo weather API with `requests`, loads a week of Paris temperatures into a pandas DataFrame, plots them with matplotlib and saves the data to CSV. The last part covers classes and inheritance.

## Running it

```bash
pip install -r requirements.txt
python hello.py
```

The weather section needs an internet connection. It writes `weather_chart.png` and `data/paris_weather.csv`.
