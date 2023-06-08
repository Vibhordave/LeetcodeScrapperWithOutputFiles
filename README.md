# DataProcessingAndQuerying Branch

# Description
The data_processing_and_querying branch implements the TF-IDF algorithm to process the scraped data along with input data and find closely related questions based on a query.

# Usage
1. Run the prepare.py script in the DataProcessingAndQuerying branch to process the given raw data and generate intermediate text files required for TF-IDF calculations. The output is stored in the TF_IDF_data branch.
2. Execute the query.py script to enter a query and retrieve the closely related questions. The script uses the TF-IDF algorithm to calculate the relevance scores and presents the most relevant questions.
