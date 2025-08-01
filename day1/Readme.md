
1. Different types of charts

| Plot Type        | Purpose                                   | Example                      |
| ---------------- | ----------------------------------------- | ---------------------------- |
| Histogram        | Distribution of numeric variable          | Age distribution             |
| Bar Chart        | Count/mean of categories                  | Passenger count per Pclass   |
| Line Plot        | Trend over time                           | Stock price per day          |
| Box Plot         | Compare distributions                     | Age by Survived              |
| Violin Plot      | Detailed distribution view                | Fare by Pclass               |
| Scatter Plot     | Correlation between 2 variables           | Age vs Fare                  |
| Heatmap          | Matrix of correlations or intensities     | Numeric feature correlations |
| Pie Chart        | Show parts of a whole                     | Gender proportions           |
| Pair Plot        | All numeric relationships (multi-scatter) | Age, Fare, SibSp             |
| Stacked Bar Plot | Composition of subgroups within groups    | Survival within each Pclass  |




3. Data pipeline 

            Raw CSV
              ↓
     ┌────────────────────┐
     │ Load with Pandas   │ ← (pd.read_csv)
     └────────────────────┘
              ↓
     ┌────────────────────┐
     │ Handle missing     │ ← (fillna, dropna)
     └────────────────────┘
              ↓
     ┌────────────────────┐
     │ Encode categoricals│ ← (LabelEncoder, OneHot)
     └────────────────────┘
              ↓
     ┌────────────────────┐
     │ Scale numeric data │ ← (MinMaxScaler, StandardScaler)
     └────────────────────┘
              ↓
     ┌────────────────────┐
     │ Output clean data  │ → Ready for model or EDA
     └────────────────────┘
