# %% [markdown]
# # CS634-101 Midterm Project - Apriori Algorithm
# 
# **Author** : *Joshua Kobuskie*

# %% [markdown]
# ## Part 1 Details
# 1. Create 10 (or any number of, not less than 5) items usually seen in
# Amazon, K-mart, or any other supermarkets (e.g. diapers, clothes, etc.).
# 2. Create a database of at least 20 transactions each containing some of these
# items. Save the transaction in a CSV file.
# 3. Repeat (1) by creating 4 additional, different databases each containing at
# least 20 transactions.
# 4. Note: You can create these transactions and datasets manually, download
# them from the net, or use the examples I will provide. In any case, add a
# note to your report where and how you built your data sets.
# 5. The items and transaction must not be random so that your code is
# deterministic

# %% [markdown]
# ### Data Initialization: ###
# Prior to beginning the program, transactional data was initialized for each store. A dataset was created for each of the retail stores represented and this data is saved into CSV files for future use. The "amazonTransactions.csv", "bestBuyTransactions.csv", "kMartTransactions.csv", "nikeTransactions.csv", "genericTransactions.csv", "customTransactions.csv", and "walmartTransactions.csv" files must be present in the current directory in order for the program to run properly. Datasets 1 through 6 have been created based on the examples provided. Dataset 7 has been built using GenAI, and contains 1000 transactions with 30 unique items to simulate Walmart transactional data.

# %% [markdown]
# ## Part 2 Details
# * Implement the brute force method to generate frequent items and generate
# association rules.
# * The brute force method for finding frequent itemsets works as follows.
# Enumerate and generate all possible 1-itemsets and 2-itemsets. There are
# 30 items, so there are 435 possible 2-itemsets totally. Check to see whether
# each possible 1-itemset/2-itemset is frequent. Then enumerate and generate
# all possible 3-itemsets. There are 4060 possible 3-itemsets totally. Check to
# see whether each possible 3-itemset is :frequent. Keep on doing so until
# you see none of the possible k-itemsets is :frequent for some k, at which
# point the brute force method terminates without generating (k+1)-itemsets.

# %% [markdown]
# ### Input Selection and Validation: ###
# Upon start, the user is welcomed to the Apriori Algorithm on the command line and prompted to enter the following user specified variables.

# %% [markdown]
# ### Determination of Dataset: ###
# The user is provided with a list of datasets and is prompted to enter an integer value between 1 and 7 on the command line to select the corresponding dataset. If a value outside of this range or a non-integer value is entered, an error is created and the program terminates.

# %%
# The data set selection, support, and confidence must be user-specified parameters

# Start and take in user input

print("CS634-101 Apriori Midterm Project - Joshua Kobuskie")

dataSelect = input("Please select a dataset by number: \n1. Amazon \n2. Best Buy \n3. K-Mart \n4. Nike \n5. Generic \n6. Custom\n7. Walmart\n")

# Confirm selection is valid
try:
    dataSelect = int(dataSelect)
    if dataSelect not in range(1,8):
        print("Invalid input. Please restart and enter a valid dataset number.")
        raise SystemExit
except ValueError:
    print("Invalid input. Please restart and enter a valid dataset number.")
    raise SystemExit

datasets = ["Amazon", "Best Buy", "K-Mart", "Nike", "Generic", "Custom", "Walmart"]

print("You have selected dataset {}: {}".format(dataSelect, datasets[dataSelect-1]))

# %% [markdown]
# ### Determination of Support: ###
# The user is prompted to enter an integer value between 1 and 100 on the command line to select the minimum support. If a value outside of this range or a non-integer value is entered, an error is created and the program terminates.

# %%
support = input("Please select the minimum support level in % (value 1 to 100):\n")

# Confirm selection is valid
try:
    support = int(support)
    if support not in range(1,101):
        print("Invalid input. Please restart and enter a valid support level.")
        raise SystemExit
except ValueError:
    print("Invalid input. Please restart and enter a valid support level.")
    raise SystemExit

print("You have selected a minimum support level of {}%".format(support))

# %% [markdown]
# ### Determination of Confidence: ###
# The user is prompted to enter an integer value between 1 and 100 on the command line to select the minimum confidence. If a value outside of this range or a non-integer value is entered, an error is created and the program terminates.

# %%
confidence = input("Please select the minimum confidence level in % (value 1 to 100):\n")

# Confirm selection is valid
try:
    confidence = int(confidence)
    if confidence not in range(1,101):
        print("Invalid input. Please restart and enter a valid confidence level.")
        raise SystemExit
except ValueError:
    print("Invalid input. Please restart and enter a valid confidence level.")
    raise SystemExit

print("You have selected a minimum confidence level of {}%".format(confidence))

# %% [markdown]
# ### Data Loading and Preprocessing: ###
# The support and confidence levels entered by the user are converted into a float representing the percentage of support and confidence required. The selected dataset is loaded from the corresponding CSV file, and each transaction is read into an array for future traversal. The set of unique items is generated from the array of transactions by traversing all transactions and adding each unique item to the set. A frequent itemsets dictionary is also initialized to store the frequent itemsets and the support for each itemset.

# %% [markdown]
# ### Timing: ###
# To time the execution of each algorithm, the time library was used. The start time is recorded when preprocessing has been completed and the algorithm begins identifying frequent itemsets and association rules. The stop time is then determined for both the frequent itemset identification and the association rule identification at the end of printing the frequent itemsets and at the end of printing the association rules, respectively. The time to determine frequent itemsets and the time to determine association rules is then calculated as the difference between the stop and start times, and this is calculated for each of the three algorithms and printed to the user on the command line.

# %%
# Open selected sets and transactions
import itertools
import time
import csv

support /= 100
confidence /= 100

transactions = ["amazonTransactions.csv", "bestBuyTransactions.csv", "kMartTransactions.csv", "nikeTransactions.csv", "genericTransactions.csv", "customTransactions.csv", "walmartTransactions.csv"]

with open(transactions[dataSelect-1], mode ='r') as file:
  csvFile = csv.reader(file)
  curTrans = []
  for line in csvFile:
    curTrans.append(line)

# All implementations will start with the data in curTrans
# Begin timing from here for comparison
bruteFreqTime = time.time()

# Having the starting sets is redundant. Removing and just find unique items in transactions

curSet = set()
for trans in curTrans:
  for item in trans:
    # Will only add if the item has not been encountered yet since it is a set
    curSet.add(item)

frequentItems = {}

# %% [markdown]
# ### Iterate over Candidate Itemsets of Size K: ###
# Using a brute force method, candidate itemsets of size K will be created, starting with K=1 and increasing by 1 during each iteration. Candidate itemset generation is repeated only if at least 1 frequent itemset was found for the previous value of K and the candidate itemset size does not exceed the number of unique items. 
# 
# * ### Computer Combinations: ###
# Using the itertools library, the candidate set of K-itemsets is created by calculating the combinations of the unique itemset of the specified size K. Each combination is then searched for within the transactional array, and its frequency is calculated.
# 
# * ### Check Support and Store Frequency: ###
# If the frequency divided by the total number of transactions for a given candidate itemset is greater than or equal to the support value specified by the user, the itemset is considered to be frequent and the itemset and support level are stored in the frequent itemsets dictionary as a key-value pair. If a frequent itemset is found, the looping parameter will also be updated to ensure exploration of the next set of candidate itemsets of size K+1.
# 
# * ### Update Candidate Set Size to K+1: ###
# After checking all candidate itemsets of size K, the candidate set size will be incremented by 1 from K to K+1. The program begins the iteration process again, performing the same evaluation to determine if any frequent itemsets were found during the prior iteration. If no frequent itemsets were found, the program will terminate and not explore any larger K-itemsets based on the Apriori Principle.
# 

# %%
# Check all sizes of combinations until one is not found or reach max len
# Originally was going to limit the size of the combinations as being checked, but upon review realized that this was not truly brute force
# Removed optimization

found = 1
i = 1
while (i <= len(curSet) and found > 0):
  found = 0

  # For each combination of size i
  for combination in itertools.combinations(curSet, i):
    # Count support of combination by iterating through the transactions
    count = 0

    for trans in curTrans:
      # Cast combination to a set to use the issubset function
      # Check if combination occurs in transaction and incriment count
      if set(combination).issubset(trans):
        count += 1
    
    if count/len(curTrans) >= support:
      # Save frequent items
      frequentItems[combination] = count/len(curTrans)
      # Found at least one frequent item in this size of combinations
      found += 1

  # Check next combination size
  i += 1

# %% [markdown]
# ### Print Frequent Itemsets: ###
# For each itemset identified as frequent and stored in the frequent itemsets dictionary, the frequent itemset and support value for that itemset are printed to the user on the command line.

# %%
print("\nBrute Force Frequent Itemsets\n")

for i, (items, supp) in enumerate(frequentItems.items()):
    print("Frequent Itemset {}: [{}]\nSupport: {:0.2f}%\n".format(i+1, ", ".join(items), supp*100))

# Frequent items generated, end timing
bruteFreqTime = time.time() - bruteFreqTime

print("Generated Brute Force Frequent Itemsets in {} seconds".format(bruteFreqTime))

# %% [markdown]
# ### Iterate over Frequent Itemsets to Find Association Rules: ###
# An association rules array is initialized to store association rules as discovered. The stored frequent itemsets previously discovered are now iterated over for all itemsets with at least 2 unique items. 
# 
# * ### Generate Increasing Large Combinations as an Antecedent for each Itemset: ###
# Each frequent itemset is composed of unique items. All subsets of the current frequent itemset being evaluated will be generated, starting with subsets of size 1 and increasing until one less than the size of the frequent itemset. Each subset generated will represent the antecedent in the association rules to be tested. For each antecedent, which must be a frequent itemset previously explored due to the Apriori Principle, the support of the itemset can be divided by the support of the antecedent by finding their associated values in the frequent itemsets dictionary. The resulting value is the confidence of the association rule.
# 
# * ### Check Confidence and Store Association Rules: ###
# If the confidence of the association rule is greater than or equal to the user specified confidence level, the consequent can be calculated by removing the antecedent from the itemset, and the association rule is stored as the antecedent, consequent, confidence, and support in a tuple.
# 

# %%
bruteRuleTime = time.time()

associationRules = []

for itemset in frequentItems:
    if len(itemset) > 1:

        # For all subsets of the itemset
        for i in range(1, len(itemset)):
            for ant in itertools.combinations(itemset, i):
                # Check confidence
                if frequentItems[itemset]/frequentItems[ant] >= confidence:
                    cons = tuple(set(itemset) - set(ant))
                    # Store antecedent, consequent, confidence, support
                    associationRules.append((ant, cons, frequentItems[itemset]/frequentItems[ant], frequentItems[itemset]))

# %% [markdown]
# ### Print Association Rules: ###
# For each association rule identified and stored in the association rules array, the antecedent, consequent, confidence, and support is printed to the user on the command line.

# %%
print("\nBrute Force Association Rules\n")

for i in range(len(associationRules)):
    print("Association Rule {}: [{}] -> [{}]\nConfidence: {:0.2f}%\nSupport: {:0.2f}%\n".format(i+1, ", ".join(associationRules[i][0]), ", ".join(associationRules[i][1]), associationRules[i][2]*100, associationRules[i][3]*100))

# Association rules generated, end timing
bruteRuleTime = time.time() - bruteRuleTime
print("Generated Brute Force Association Rules in {} seconds".format(bruteRuleTime))
print("#"*64)

# %% [markdown]
# ## Part 3 Details
# Use an existing Apriori implementation from Python libraries/packages to
# verify the results from your brute force algorithm implementation.
# * Use Python existing package for fpgrowth (as known as fp-tree algorithm)
# to generate the items and rules.
# * Compare the results from your brute-force, Apriori, and FP-Tree/Growth.
# * Do the three algorithms produce the same results?
# * Report the timing performance for all three algorithms as well.
# * Which one is faster?
# So, for all three algorithms, generate and print out all the association rules and
# the input transactions for each of the 5 transactional databases you created/used.
# The data set selection, support, and confidence must be user-specified
# parameters, so the output should show different rules with respect to different
# databases and different support/confidence.
# Make sure to show multiple support and confidence results for each data set.
# You should prompt the user only once for the input and reuse for the three
# algorithms in each run.
# The items and transactions must be clear and easy to identify. Your
# program should show the performance time for each algorithm.

# %% [markdown]
# ### Results and Evaluation: ###
# The accuracy of my brute force implementation is verified by comparing the results of two library-based implementations of the Apriori and FP-growth algorithm to determine frequent itemsets and association rules. The time taken to execute each of these methods is then compared to illustrate the differences in execution time for each implementation.
# 
# * ### Existing Libraries used to Validate: ###
# The mlxtend library was used to validate the results of my brute force implementation. The same dataset, support, and confidence as previously specified by the user are used to inform the Apriori and FP-Growth algorithms and recalculate the frequent itemsets. This information is then passed to the mlxtend association rule function to determine the association rules for both the Apriori and FP-Growth algorithms. The same print output is generated by iterating through the output of each algorithm.
# 
# * ### Difference in Data Representation: ###
# A notable difference in the implementation of my brute force algorithm and the mlxtend implementations is the use of a pandas dataframe. My implementation of the brute force algorithm relies on a 2D array to represent the transactions, where the mlxtend algorithms take in a pandas dataframe. To create this dataframe, the transactions were first encoded and transformed to ensure equal dimensions in each transaction in the dataframe. This difference does not impact the data itself, but does change how it is represented and stored. The use of a pandas dataframe may have an influence on the timing of these algorithms as compared to the use of a 2D array.
# 

# %%
import mlxtend
import mlxtend.frequent_patterns
import mlxtend.preprocessing
import pandas as pd

transEncoder = mlxtend.preprocessing.TransactionEncoder()
transEncoderArr = transEncoder.fit(curTrans).transform(curTrans)
transDF = pd.DataFrame(transEncoderArr, columns=transEncoder.columns_)

# Begin timing from here for comparison
aprioriFreqTime = time.time()

aprioriFreqItems = mlxtend.frequent_patterns.apriori(transDF, min_support=support, use_colnames=True)

print("\nApriori Frequent Itemsets\n")

for index, row in aprioriFreqItems.iterrows():
    print("Frequent Itemset {}: [{}]\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["itemsets"]), row["support"]*100))

aprioriFreqTime =  time.time() - aprioriFreqTime

print("Generated Apriori Frequent Itemsets in {} seconds".format(aprioriFreqTime))

# %%
aprioriRulesTime = time.time()

if not aprioriFreqItems.empty:
    aprioriRules = mlxtend.frequent_patterns.association_rules(aprioriFreqItems, metric="confidence", min_threshold=confidence)
else:
    aprioriRules = pd.DataFrame(columns=["antecedents", "consequents", "confidence", "support"])

print("\nApriori Association Rules\n")

for index, row in aprioriRules.iterrows():
    print("Association Rule {}: [{}] -> [{}]\nConfidence: {:0.2f}%\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["antecedents"]), ", ".join(row["consequents"]), row["confidence"]*100, row["support"]*100))

aprioriRulesTime = time.time() - aprioriRulesTime

print("Generated Apriori Association Rules in {} seconds".format(aprioriRulesTime))
print("#"*64)

# %%
# Begin timing from here for comparison
fpFreqTime = time.time()

fpFreqItems = mlxtend.frequent_patterns.fpgrowth(transDF, min_support=support, use_colnames=True)

print("\nFP-Growth Frequent Itemsets\n")

for index, row in fpFreqItems.iterrows():
    print("Frequent Itemset {}: [{}]\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["itemsets"]), row["support"]*100))

fpFreqTime =  time.time() - fpFreqTime

print("Generated FP-Growth Frequent Itemsets in {} seconds".format(fpFreqTime))

# %%
fpRulesTime = time.time()

if not fpFreqItems.empty:
    fpRules = mlxtend.frequent_patterns.association_rules(fpFreqItems, metric="confidence", min_threshold=confidence)
else:
    fpRules = pd.DataFrame(columns=["antecedents", "consequents", "confidence", "support"])

print("\nFP-Growth Association Rules\n")

for index, row in fpRules.iterrows():
    print("Association Rule {}: [{}] -> [{}]\nConfidence: {:0.2f}%\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["antecedents"]), ", ".join(row["consequents"]), row["confidence"]*100, row["support"]*100))

fpRulesTime = time.time() - fpRulesTime

print("Generated FP-Growth Association Rules in {} seconds".format(fpRulesTime))
print("#"*64)

# %% [markdown]
# ## Part 4 Details
# Github & Jupyter Notebook.
# * After you finish your code in development and testing
# and make sure it works, and prepare the report (meaning
# all heavy lifting job is done ), Create a Github
# repository in https://github.com/. Your account must be
# with your NJIT email not your personal email (unless if
# you have to, but indicate that in your report as well).
# * Load your project to the repository.
# * Create Jupyter notebook for your work to show the
# output, for more info visit https://jupyter.org/
# * Give me ya54@njit.edu access as a collaborator to your
# repository. (If we have a grader, you give him/her access
# too).
# * Add Github link to your repository to your report.


