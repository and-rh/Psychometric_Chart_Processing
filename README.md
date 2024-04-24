Claro, aquí te proporciono el contenido del archivo README con los formatos de Markdown adecuados para títulos y subtítulos. Los títulos y subtítulos están organizados utilizando diferentes niveles de "#" para representar la jerarquía de la sección.

### Contenido del README.md con Formato Markdown

---

# Psychrometric Chart Generator

## Introduction

This repository contains a Python script designed to generate psychrometric charts for different datasets. Each chart visualizes the relationship between dry bulb temperature, humidity ratio, and comfort zones based on provided climate data in CSV files. The script is intended for use in climate studies, HVAC system analysis, or any field where understanding air properties is essential.

## Requirements

To run this script, you will need Python installed on your machine along with several libraries. Here's what you need to install:

- Python 3.7 or higher
- Pandas
- Matplotlib
- Numpy
- Psychrolib

You can install these dependencies using pip:

```bash
pip install pandas matplotlib numpy
pip install psychrolib
```

## Installation

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/psychrometric-chart-generator.git
cd psychrometric-chart-generator
```

## Usage

To use this script, you must have CSV files with specific columns named 'temperature' and 'humidity' where:
- `temperature` should be in degrees Celsius.
- `humidity` should be the relative humidity percentage.

### Steps to Run the Script:

1. Place your CSV files in a directory.
2. Update the `file_paths` list in the script with the paths to your CSV files.
3. Run the script using:

```bash
python psychrometric_chart_generator.py
```

The script will generate a PDF file for each dataset, containing the psychrometric chart with a comfort zone visualization, and save it in the same directory as the source file.

### Example

Suppose you have a CSV file named `climate_data.csv` in the directory `/data`. Update the script:

```python
file_paths = [
    '/data/climate_data.csv'
]
```

After running the script, you will find a PDF file named `climate_chart.pdf` in the `/data` directory.

## Contributing

Contributions to this project are welcome. You can contribute by:

- Enhancing the script's functionality.
- Adding features to handle different data formats.
- Improving the visualization.

Please create a pull request to contribute.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details or visit [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
