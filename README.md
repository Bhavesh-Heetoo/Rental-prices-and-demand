# NYC Airbnb Dataset Analysis
# Overview
The project aims to analyze rental rates and demand trends across New York City’s boroughs using Airbnb listing data. This project will focus on identifying price variations, rental availability, and demand patterns at the borough and neighborhood levels The results will be accessible through a Flask API and visualized using Pandas DataFrames and GeoPandas for mapping.


# Dataset
The dataset utilized in this investigation includes Airbnb data found from Kaggle. This data set includes the listing ID, price, neighborhood, host name and final review.

# Analysis 
Does higher age increase the risk of stroke?
- A bar chart that displays the stroke occurence between varying age groups.This graph visually comfirms higher age does increase the risk of stroke occurrence.
- A line graph that displays the stroke occurrences distributed by age group. Storke occurrences seem to increase significantly as people age.
- A bar chart that illustrates the probability of stroke across diffrent age groups in percentages.
  
Hypertension and heart disease impact on stroke?
- A pie chart to study health status for individuals who had stroke. From the health status distribution for stroke chart we can see more than half of people who had stroke also suffer hypertension and heart disease (57.4% of stroke population), and only 5.3% of individuals who had stroke is healthy.
- A bar chart which counts the number of stroke and non-stroke individuals for each health status. The chance of stroke for healthy individuals is much lower than individuals who have either heart disease or hypertension.

Does smoking have an impact on the likelihood of suffering a stroke?
- Used two pie charts to show the different groups smoking status between stroke and nonstroke.
- Used two bar charts to show how many suffered stroke. 
- the p value could be calculated, 0.760, meaning it is higher than 0.05, making the data statistically insignificant. 

How do different types of work (Private, Self-employed, Govt_job, Never _worked) affect stroke risk?
- A bar chart shows the number of people in diffrent work types , categorized by stroke status. The result indicate that private and self-employed types have higher stroke occurences.
- A pie chart to distinctly analyse the different work types and their relation to stroke. The chart suggests that the private sector jobs are more susceptible to stroke, followed by self employed jobs. This indicates that more research could be conducted for further causal relationships to be seen.

Does living in an urban or rural area affect stroke likelihood?
- A pie chart displays the stroke occurrence between people living in urban and rual areas. The close distribution suggests that the occurrence of strokes is relatively balanced between urban and rual residence types.
- A bar graph to determine the difference in living in a rural or urban area and its relation to stroke occurence. The bar graph successfully demonstrates an increase in stroke occurence amongst those who live in urban areas, when compared to rural. The difference however is not significant, therefore a definitive conclusion cannot be made, and more research must be carried out.

What is the relationship between BMI and stroke occurrence?
-	A bar chart of BMI categories demonstrated that most stroke patients are “Overweight” (75 cases). The results clearly demonstrated the danger associated with higher BMI values, particularly in overweight. 
-	A comparison of male and female stroke patients found that woman have higher BMIs in the “Overweight” and “Obese Class I” categories, rendering them more susceptible to stroke. This gap emphasizes the need of focusing weight control programs on women in these groups. 
-	The trend study of BMI across age groups revealed that BMI in stroke patients decreases with age. Younger stroke patients (aged 40-50) had considerably greater BMI levels than elderly patients (aged 80-90). This shows that early intervention in BMI management among young individuals may minimize stroke risk.

How do glucose levels vary across patients with stroke?
-	A scatter plot study revealed that glucose levels in stroke patients grow with age, peaking at 140 mg/dl for individuals aged 70 to 80. 
-	Box plot analysis found multiple glucose outliers, some of which exceeded 150 mg/dl, indicating undetected diabetes or poor glucose management in certain stroke patients.


# Visualizations
Several key charts were generated to support the analysis:
- Bar Chart
- Line Chart
- Pie Chart
- Scatter Plot
- Box Plot

# How to Run
   1. Clone the repository:
       1. Open your terminal (Git Bash, Command Prompt, or any Git client).
       2. Use the cd command to navigate to the directory where you want to clone the repository.
       3. Run the following command to clone the repository: git clone link_provided
  2. Ensure Pandas, Matplotlib, SciPy, and NumPy is installed on your machine.
     - Install Pandas using pip if it's not already installed (pip install pandas).
     - Install Matplotlib using pip if it's not already installed (pip install matplotlib).
     - Install SciPy using pip if it's not already installed (pip install scipy).
     - Install NumPy using pip if it's not already installed (pip install numpy).
  3. Open the cloned file in the Visual Studio Code:
       1. Go to file > Open Folder and navigate to the folder where you cloned the repository.
       2. Select the folder to open in VS code.
  4. Run the Jupyter Notebook
     1. Open the notebook file (cleaned_stroke_df.ipynb) in VS code or Jupyter.
     2. Run the cells to perform the Analysis.
    
# References 
Fedesoriano. “Stroke Prediction Dataset.” Kaggle, 26 Jan. 2021, www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data. 


