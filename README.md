
# NYC Airbnb Analysis 

## Overview

This project analyzes rental prices and demand across neighborhoods in New York City using data from Airbnb. We will focus on extracting insights such as price distributions and room types in different boroughs and neighborhoods. The project includes two main components:

1. **Database Design**: Performed in a Jupyter Notebook to clean, transform, and analyze the Airbnb dataset.
2. **Data and Delivery(Flask API/Pandas)**:A flask API was created for querying the processed data, allowing users to filter by price ranges, boroughs, neighborhoods, and room types.

The purpose for our project is to help users better understand the NYC Airbnb market and identify trends in rental prices and availability.

---

## Database Overview and Choice

The project uses a **PostgreSQL** database to store the cleaned and processed data.

why PostgreSQL was chosen?

- Scalability: PostgreSQL is robust and scalable, making it a reliable choice for handling large datasets like Airbnb listings
- Features: PostgreSQL offers efficient querying , for operations like filtering by price or neighborhood.
- Relational Structure: PostgreSQL relational model is well-suited to handle structured data  like our Airbnb dataset.



### Why We Chose the Airbnb Dataset

We selected the [Airbnb dataset](https://www.kaggle.com/datasets/ebrahimelgazar/new-york-city-airbnb-market?select=airbnb_price.csv) because it provides comprehensive data on rental properties in New York City, including:

- **Details**: The dataset includes boroughs, neighborhoods, listing prices, and room types, enabling in-depth analysis of rental trends.
- **Relevance**: With the growing popularity of Airbnb in NYC, understanding the market is highly relevant.
- **Insights/Analysis**: By combining price data with geospatial analysis, we can uncover patterns in rental costs and demand across NYC.

### Database Schema

The database contains two main tables:

1. **`prices`**** Table**:

   - `listing_id` (Primary Key): Unique ID for each listing.
   - `listing_price`: Numeric price of the listing.
   - `borough`: Borough of NYC where the listing is located.
   - `neighborhood`: Neighborhood of the listing.

2. **`room_type`**** Table**:

   - `listing_id` (Primary Key): Unique ID for each listing.
   - `room_type`: Type of room (e.g., Private Room, Entire Home).

---

## How to Run the Code

### 1. Clone the Repository

1. Open your terminal (Git Bash, Command Prompt, or any Git client).
2. Navigate to where you want to clone the project.
3. Run the following command:
   ```bash
   git clone <repository_url>
   ```

### 2. Setting Up the Environment

#### **Create a Virtual Environment**

1. Run the following in the terminal to create a virtual environment:
   ```bash
   conda create -n dev python=3.10 anaconda -y
   ```
2. Activate the virtual environment:
     ```bash
     conda activate dev
     ```
   

#### **Install Libraries**

After activating the virtual environment, install the required libraries:

```bash
pip install flask
pip install sqlalchemy
pip install psycopg2
pip install pandas
pip install geopandas
pip install matplotlib
pip install numpy
```

### 3. Running the Jupyter Notebook

1. Open the `Maincode.ipynb` file for database design.
2. Follow the instructions in the notebook to:
   - Load and clean the data.
   - Transform the data for insertion into the PostgreSQL database.
   - Perform a breif analysis of the data.

---

### 4. Running the Flask API

1. Ensure the PostgreSQL database is running and the data has been inserted.
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Access the API  using your web browser :
   - **Home Page**: `http://127.0.0.1:5000/`
   - **All Prices**: `http://127.0.0.1:5000/api/prices`
   - **Filter by Price**: `http://127.0.0.1:5000/api/prices/filter?min_price=100&max_price=500`
   - **Filter by Borough**: `http://127.0.0.1:5000/api/prices/borough/Brooklyn`
   - **Room Types**: `http://127.0.0.1:5000/api/room_types`
   - **Filter by Neighborhood**: `http://127.0.0.1:5000/api/prices/neighborhood/<neighborhood>`


---

### Ethical Considerations

1. **Data Integrity**:
   - The Airbnb dataset used in this project is sourced from Kaggle, ensuring it is publicly available and complies with data-sharing policies.

2. **Privacy**:
   - No personally identifiable information  is included in the dataset. The analysis focuses solely on variables like prices, room types, and neighborhood information.

3. **Educational Purpose**:
   - The project is intended for educational purposes only, aimed at demonstrating data engineering and analysis techniques.
   - The insights derived should not be used for commercial purposes.

4. **Respect for Data Usage Policies**:
   - The project complies with Airbnb’s data usage guidelines. It refrains from scraping data that is not publicly available.


### Findings from dataset

**1. Highest Rental Price:**
- Listing ID: `36455809`
- Listing Price: `$7500.0`
- Borough: `Staten Island`
- Neighborhood: `Woodside

**2. Median Rental Price for Each Borough:**
| Borough       | Median Price |
|---------------|--------------|
| Bronx         | $670.0       |
| Brooklyn      | $7500.0      |
| Manhattan     | $5100.0      |
| Queens        | $2600.0      |
| Staten Island | $300.0       |

**3. Lowest Priced Rental by Borough:**
| Borough       | Lowest Price |
|---------------|--------------|
| Bronx         | $0.0         |
| Brooklyn      | $0.0         |
| Manhattan     | $10.0        |
| Queens        | $10.0        |
| Staten Island | $13.0        |

**4. Average Rental Price By Room Type:**
| Room Type         | Average Price |
|-------------------|----------------|
| Entire Home/Apt   | $197.17        |
| Private Room      | $81.64         |
| Shared Room       | $53.47         |


### References

- Airbnb dataset: [https://www.kaggle.com/datasets/ebrahimelgazar/new-york-city-airbnb-market?select=airbnb\_price.csv](https://www.kaggle.com/datasets/ebrahimelgazar/new-york-city-airbnb-market?select=airbnb_price.csv)



