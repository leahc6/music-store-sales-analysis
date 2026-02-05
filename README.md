## Music Store Sales Analysis
Data analysis project exploring music sales with Python and Power BI through data cleaning, modelling and visualisation.


### 📊Project Overview
This analysis explores sales performance and customer behaviour at digital music store, The Music Vault. 
The aim was to analyse the store’s performance by identifying key revenue drivers, understanding how purchasing patterns evolved over time and determining which types of music customers spent the most on. 
Python was used to clean and prepare the data, while Power BI facilitated data modelling, DAX calculations and interactive visualisations. Together, these tools transformed raw, transactional data into clear, actionable insights.
The final report presents a breakdown of top-performing artists, albums and genres, alongside key customer metrics, highlighting trends that support strategic decision-making.


### 📁Dataset Description
The dataset contains five years of transactional data from a digital music store, including both numerical and categorical data. It was sourced from a publicly available dataset on Kaggle and is structured across seven CSV files, linked by primary and foreign keys. The data consists of thousands of rows across invoices, invoice line items, customers, genres, tracks, albums and artists.


### ❓Key Business Questions
- Which artists, albums and genres generate the most revenue?
- How does revenue change over time? 
- Which countries have the highest number of customers? 
- How valuable is the average customer based on spend and total orders?
- What proportion of customers make repeat purchases?


### 📈Dashboard Overview
The Power BI dashboard consists of three pages: Overview, Music Performance and Customer Insights. Each page focuses on a specific analytical theme and uses interactive visuals to explore trends. 
The Overview page presents core KPIs and trend analysis to highlight overall business performance. The Music Performance page focuses on artists, genres and albums, using revenue-based visuals to identify top contributors. The Customer Insights page highlights customer activity, such as average spend, top customers by revenue and geographical distribution. 
Across the dashboard, filters and time-based sliders enable deeper exploration and allow users to focus on specific periods.


### 🔍Key Insights
- **The top 10 artists collectively account for over 30% of total revenue.** Iron Maiden, U2 and Metallica rank among the highest-earning artists; however, no individual artist dominates overall revenue.
- **Album revenue is evenly distributed,** with the top five albums contributing a similar share of revenue. No single album stands out as a major outlier in total revenue.
- **Rock is the strongest genre across all five years.** It consistently outperforms other genres by revenue generated. While Latin, Metal, Alternative & Punk and Jazz are among the top five genres by revenue, they remain significantly smaller in their yearly performance compared to Rock. -These five genres are also the most popular in terms of total orders.
- **Revenue does not always follow a consistent seasonal pattern.** However, peaks often occur between May and July, while the lowest performing months tend to fall between September and December. 
- **The USA and Canada have the highest number of customers.** Together they represent 36% of the customer base, with customers in these markets placing an average of 7 orders each. European countries also account for a large share of customers compared with other regions. 
- **Customer value is consistent across the dataset.** The average customer places seven orders, while spending approximately €39 per order. Customer retention is exceptionally strong, with 100% of customers making repeat purchases. There are no major outliers in spend or order volume, indicating a stable purchasing behaviour. 

### 💡Business Recommendations
**1. Expand the customer base in high-performing regions**
With only 59 customers over five years, increasing brand awareness is essential for long-term growth. Targeted marketing campaigns in top-performing markets, such as the USA and Canada, would attract new customers and accelerate growth.

**2. Leverage strong customer retention to drive insight and customer growth**
Repeat purchasing behaviour is excellent, indicating customer satisfaction with the store’s products and services. Conducting a short customer survey would help to understand what drives retention and where improvements could be made. Introducing referral incentives to loyal customers could help to expand the customer base.

**3. Target seasonal opportunities to stabilise revenue**
Revenue tends to decrease between September and December. Seasonal campaigns, promotions and limited discounts during this period would help boost sales and smooth out performance across the year.

**4. Diversify product offering to increase average order value**
All tracks are priced between €0.99 and €1.99, which limits revenue per order. Introducing higher value products, such as bundles, exclusive releases, premium editions or subscription packages could increase average order value and strengthen overall revenue.
