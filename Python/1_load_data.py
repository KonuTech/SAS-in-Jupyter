# coding: utf-8 # # This is the first in a series of examples provided to demonstrate the use of SAS Visual Data # Mining and Machine Learning actions to compose a program that follows a standard machine learning process of # - loading data, # - preparing the data, # - building models, and # - assessing and comparing those models # # The programs are written to execute in the CAS in-memory distributed computing engine in the SAS Viya environment. # # This first example showcases how to load local data into CAS # ### Import packages # In[1]: from swat import * # ### CAS Server connection details # In[2]: cashost='localhost' casport=5570 useremail='YOUR SAS PROFILE EMAIL' userpassword='YOUR SAS PROFILE PASSWORD' casauth='~/.authinfo' # ### Start CAS session # In[3]: sess = CAS(cashost, casport, useremail, userpassword, caslib="casuser") # ### Details for local data to be loaded into CAS # In[4]: indata_dir="/opt/sasinside/DemoData" indata="bank_raw" # ### Import table action set # In[5]: sess.loadactionset(actionset="table") # ### Load data into CAS # The data set used for this workflow is anonymized bank data consisting of observations taken # on a large financial services firm's accounts. Accounts in the data represent consumers of # home equity lines of credit, automobile loans, and other types of short- to medium-term credit # instruments. A campaign interval for the bank runs for half of a year, denoting all marketing # efforts that provide information about and motivate the purchase of the bank's financial services # products. # # - the bankraw data set is the original data in its raw form # - the bank data set is the resulting data set after applying appropriate data cleansing # # The target variable "b_tgt" quantifies account responses over the current campaign season (1 # for at least one purchase, 0 for no purchases) A description of all variables can be found in # the data dictionary for this data set available in "BankData" in your File Shortcuts. # # For execution in the CAS engine, data must be loaded from the local data set to a CAS table. # This code first checks to see if the specified CAS table exists and then loads data from local # data sets. # In[6]: if not sess.table.tableExists(table=indata).exists: tbl = sess.upload_file(indata_dir+"/"+indata+".sas7bdat", casout={"name":indata}) # In[7]: tbl.head() # ### End CAS session # In[8]: sess.close()