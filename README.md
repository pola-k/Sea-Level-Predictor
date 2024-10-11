# Sea Level Predictor

In this project, we will analyze global average sea level change data since 1880 and use it to predict future sea level changes up to the year 2050. We will use Python, Pandas, Matplotlib, and the `linregress` function from Scipy for statistical modeling and data visualization.

## Project Overview

The project is designed to predict sea level rise using linear regression models based on historical data from the **"epa-sea-level.csv"** dataset.

### Steps:
1. **Data Import**: Use Pandas to import the data from the CSV file.
2. **Scatter Plot**: Create a scatter plot using Matplotlib to visualize the relationship between the years and the CSIRO Adjusted Sea Level.
3. **Linear Regression (1880 - 2050)**: Use all available data to perform a linear regression and predict sea levels through the year 2050.
4. **Linear Regression (2000 - 2050)**: Perform another linear regression, but only using data from the year 2000 onwards to make a prediction through 2050.
5. **Plot Customization**: Add labels for the x and y axes and a title to the plot.

### Example Plot

The plot will show two lines of best fit:
- One for the entire dataset (1880-2050).
- One for the subset starting from 2000 (2000-2050).

### How to Run the Script
1. Make sure you have installed the required libraries by running:
```bash
pip install pandas matplotlib scipy
```
2. Download the dataset **"epa-sea-level.csv"** and place it in the same directory as the Python script.
3. Run the script using:
```bash
python sea_level_predictor.py
```

### Explanation of Code
1. **Data Import**: We load the dataset using Pandas and create a scatter plot of Year vs. Sea Level.
2. **Linear Regression (1880-2050)**: We use `linregress` to calculate the slope and intercept of the line of best fit for the entire dataset. We plot this line from 1880 to 2050.
3. **Linear Regression (2000-2050)**: We repeat the process using data from 2000 onwards to generate a second line of best fit.
4. **Plot Customization**: The plot is labeled, titled, and saved as an image.

## Conclusion

This project predicts future sea level changes based on historical trends. By performing linear regression on different segments of the data, we can forecast how the rate of sea level rise may change in the future.

### Example Output

The plot will feature:
- A red line showing the overall trend from 1880 to 2050.
- A purple line showing the trend from 2000 to 2050.

Both lines allow us to estimate sea level rise under different time periods and provide insights into future environmental challenges.

This approach combines data science and environmental analysis, offering valuable predictions for sea level changes over time.
