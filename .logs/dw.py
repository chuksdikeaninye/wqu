%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 20:47:25
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 20:47:27
from static_grader import grader# Tue, 01 Jun 2021 20:47:30
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Tue, 01 Jun 2021 20:47:36
import pandas as pd
import numpy as np# Tue, 01 Jun 2021 20:47:36
# load the 2017 data
scripts = pd.read_csv('dw-data/201701scripts_sample.csv.gz')
scripts.head()# Tue, 01 Jun 2021 20:47:39
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('dw-data/practices.csv.gz', names=col_names, header=None)
practices.head()# Tue, 01 Jun 2021 20:47:39
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.head()# Tue, 01 Jun 2021 20:47:39
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.tail()# Tue, 01 Jun 2021 20:47:39
fields = ['items','nic','act_cost','quantity']
scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T #add .T to transpose
#count shows us the total number of rows# Tue, 01 Jun 2021 20:47:40
scripts[fields].sum() #computes the sum of each these columns# Tue, 01 Jun 2021 20:47:40
scripts[fields].sum().index #to get the index or column. # Tue, 01 Jun 2021 20:47:40
scripts[['act_cost','quantity']].sum() #computes the sum of each these columns# Tue, 01 Jun 2021 20:47:40
#create new data frame ; total, mean, std, 25%, 50%, 75% quartile
summary = pd.concat([scripts[fields].sum() ,scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T], axis = 1)# Tue, 01 Jun 2021 20:47:41
summary# Tue, 01 Jun 2021 20:47:41
summary.columns = ['total','mean', 'std','25%', '50%', '75%']# Tue, 01 Jun 2021 20:47:41
summary# Tue, 01 Jun 2021 20:47:41
for i in summary.itertuples():
    print (i[0], i[1:])# Tue, 01 Jun 2021 20:47:41
summary_stats = [(i[0], i[1:] )for i in summary.itertuples()]# Tue, 01 Jun 2021 20:47:41
summary_stats # Tue, 01 Jun 2021 20:47:41
# summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]# Tue, 01 Jun 2021 20:47:41
grader.score.dw__summary_statistics(summary_stats)# Tue, 01 Jun 2021 20:47:42
group_bnf = scripts.groupby('bnf_name')# Tue, 01 Jun 2021 20:47:42
type(group_bnf)# Tue, 01 Jun 2021 20:47:42
scripts.loc[group_bnf.groups['A2A Spacer']]# Tue, 01 Jun 2021 20:47:43
 item_totals = group_bnf.sum()['items']# Tue, 01 Jun 2021 20:47:43
group_bnf.sum()['items'].sort_values(ascending = False)[:1]# Tue, 01 Jun 2021 20:47:43
max_item = item_totals.idxmax()# Tue, 01 Jun 2021 20:47:43
max_item
# Tue, 01 Jun 2021 20:47:43
most_common_item = [(max_item, item_totals[max_item])]# Tue, 01 Jun 2021 20:47:44
most_common_item# Tue, 01 Jun 2021 20:47:44
# most_common_item = [("", 0)]# Tue, 01 Jun 2021 20:47:44
grader.score.dw__most_common_item(most_common_item)# Tue, 01 Jun 2021 20:47:45
scripts.head()# Tue, 01 Jun 2021 20:47:45
practices.head()# Tue, 01 Jun 2021 20:47:46
practices.sort_values('post_code').groupby('code').groups['A81001']# Tue, 01 Jun 2021 20:47:46
practices[ practices['code'] == 'A81001']# Tue, 01 Jun 2021 20:47:46
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()# Tue, 01 Jun 2021 20:47:46
unique_practices.head()# Tue, 01 Jun 2021 20:47:47
joined = scripts[['practice','bnf_name','items']].merge(unique_practices[['code','post_code']], how='left', left_on='practice' , right_on='code')[['bnf_name','items','post_code']]# Tue, 01 Jun 2021 20:47:48
joined.head()# Tue, 01 Jun 2021 20:47:48
post_item_totals = joined.groupby(['post_code','bnf_name']).sum().reset_index()# Tue, 01 Jun 2021 20:47:49
post_item_totals.head()# Tue, 01 Jun 2021 20:47:49
max_items = post_item_totals.sort_values('items', ascending=False).groupby('post_code').first()# Tue, 01 Jun 2021 20:47:49
max_items# Tue, 01 Jun 2021 20:47:49
post_item_totals.groupby('post_code')['items'].sum()# Tue, 01 Jun 2021 20:47:50
max_items['items']# Tue, 01 Jun 2021 20:47:50
max_items['items'] = max_items['items']/ post_item_totals.groupby('post_code')['items'].sum()# Tue, 01 Jun 2021 20:47:50
max_items = max_items.reset_index().sort_values('post_code')# Tue, 01 Jun 2021 20:47:50
max_items# Tue, 01 Jun 2021 20:47:50
[(item.post_code, item.bnf_name, item.items) for item in max_items.itertuples()]# Tue, 01 Jun 2021 20:47:50
items_by_region = [(item[1:]) for item in max_items.itertuples()][:100]# Tue, 01 Jun 2021 20:47:50
# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100# Tue, 01 Jun 2021 20:47:50
grader.score.dw__items_by_region(items_by_region)# Tue, 01 Jun 2021 20:47:50
max_items.to_csv('dw-data/max_items.csv') #we are saving the dataframe as a csv file# Tue, 01 Jun 2021 20:47:51
import dill# Tue, 01 Jun 2021 20:47:52
with open('dw-data/max_items.dill' , 'wb') as f:
    dill.dump(max_items, f) #dill and dump my max_items file into f

# Tue, 01 Jun 2021 20:47:53
with open('dw-data/max_items.dill' , 'rb') as f:
    new_max_items = dill.load(f)# Tue, 01 Jun 2021 20:47:54
new_max_items.head()# Tue, 01 Jun 2021 20:47:54
max_items == new_max_items# Tue, 01 Jun 2021 20:47:55
np.all(max_items == new_max_items)# Tue, 01 Jun 2021 20:47:55
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Tue, 01 Jun 2021 20:47:55
chem['NAME'].dtype# Tue, 01 Jun 2021 20:47:56
chem[['NAME']].info()# Tue, 01 Jun 2021 20:47:56
chem['NAME'].str.contains('|'.join(opioids), case=False)# Tue, 01 Jun 2021 20:47:56
'|'.join(opioids)# Tue, 01 Jun 2021 20:47:57
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()# Tue, 01 Jun 2021 20:47:57
opioid_codes# Tue, 01 Jun 2021 20:47:57
scripts['bnf_code'].isin(opioid_codes).sum()# Tue, 01 Jun 2021 20:47:57
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)# Tue, 01 Jun 2021 20:47:57
scripts.head()# Tue, 01 Jun 2021 20:47:58
scripts['opioid'].mean()# Tue, 01 Jun 2021 20:47:58
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()# Tue, 01 Jun 2021 20:47:58
opioids_per_practice# Tue, 01 Jun 2021 20:47:58
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()# Tue, 01 Jun 2021 20:47:59
standard_error_per_practice = np.sqrt(scripts['opioid'].var()/scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice# Tue, 01 Jun 2021 20:47:59
opioid_scores# Tue, 01 Jun 2021 20:47:59
opioid_scores.to_frame().rename(columns={0: 'z-score'})# Tue, 01 Jun 2021 20:48:00
unique_practices_by_name = practices.groupby('code')['name'].min().reset_index()
# Tue, 01 Jun 2021 20:48:03
unique_practices_by_name.head()# Tue, 01 Jun 2021 20:48:03
scripts['practice'].value_counts().to_frame().rename(columns={'practice': 'count'})# Tue, 01 Jun 2021 20:48:03
joined = unique_practices_by_name\
    .merge(opioid_scores.to_frame()\
    .rename(columns={0: 'z-score'}), left_on='code', right_index=True)\
    .merge(scripts['practice'].value_counts()\
           .to_frame().rename(columns={'practice': 'count'}), left_on='code', right_index=True)# Tue, 01 Jun 2021 20:48:03
anomalies = [i[1:] for i in joined.sort_values('z-score', ascending=False).itertuples() ][:100]#we are sorting the zscore values in descending order# Tue, 01 Jun 2021 20:48:03
anomalies# Tue, 01 Jun 2021 20:48:03
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100# Tue, 01 Jun 2021 20:48:04
grader.score.dw__script_anomalies(anomalies)# Tue, 01 Jun 2021 20:48:04
scripts16 = pd.read_csv('dw-data/201606scripts_sample.csv.gz')# Tue, 01 Jun 2021 20:48:08
bnf_totals_2016 = scripts16['bnf_name'].value_counts()# Tue, 01 Jun 2021 20:48:08
bnf_totals_2016# Tue, 01 Jun 2021 20:48:08
bnf_totals_2017 = scripts['bnf_name'].value_counts()# Tue, 01 Jun 2021 20:48:09
bnf_totals_2017# Tue, 01 Jun 2021 20:48:09
growth_rate = (bnf_totals_2017 - bnf_totals_2016) / bnf_totals_2016# Tue, 01 Jun 2021 20:48:09
growth_rate# Tue, 01 Jun 2021 20:48:09
growth_rate.rename('growth_rate')# Tue, 01 Jun 2021 20:48:09
pd.concat([growth_rate, bnf_totals_2016], axis=1)# Tue, 01 Jun 2021 20:48:09
pd.concat([growth_rate.rename('growth_rate'), bnf_totals_2016.rename('count')], axis=1).reset_index()# Tue, 01 Jun 2021 20:48:09
df = pd.concat([growth_rate.rename('growth_rate'), 
           bnf_totals_2016.rename('count')], axis=1).reset_index()\
           .rename(columns={'index': 'bnf_name'})# Tue, 01 Jun 2021 20:48:09
df = df[(df['count'] >= 50) & (~df['growth_rate'].isna())].sort_values('growth_rate', ascending=False) #~ MEANS not in python# Tue, 01 Jun 2021 20:48:09
len(df)# Tue, 01 Jun 2021 20:48:09
script_growth = pd.concat([df.head(50), df.tail(50)])# Tue, 01 Jun 2021 20:48:09
len(script_growth)# Tue, 01 Jun 2021 20:48:09
script_growth.head()# Tue, 01 Jun 2021 20:48:09
#script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100# Tue, 01 Jun 2021 20:48:09
script_growth = [item[1:] for item in script_growth.itertuples()]# Tue, 01 Jun 2021 20:48:10
script_growth# Tue, 01 Jun 2021 20:48:10
grader.score.dw__script_growth(script_growth)# Tue, 01 Jun 2021 20:48:24
len(scripts['bnf_code'])# Tue, 01 Jun 2021 20:53:08
p = 1/scripts['bnf_code'].nunique()# Tue, 01 Jun 2021 20:53:23
p# Tue, 01 Jun 2021 20:56:17
rare_codes = set(rates[rates < 0.1*p].index)# Tue, 01 Jun 2021 20:56:32
scripts['bnf_code'].count()# Tue, 01 Jun 2021 20:56:33
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()# Tue, 01 Jun 2021 20:56:35
rates# Tue, 01 Jun 2021 20:56:36
rare_codes = set(rates[rates < 0.1*p].index)# Tue, 01 Jun 2021 20:56:48
rare_codes = set(rates[rates < 0.1*p].index)# Tue, 01 Jun 2021 20:57:09
rare_codes# Tue, 01 Jun 2021 20:58:00
len(rare_codes)# Tue, 01 Jun 2021 20:59:59
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]# Tue, 01 Jun 2021 21:00:41
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]# Tue, 01 Jun 2021 21:01:01
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]# Tue, 01 Jun 2021 21:02:19
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]# Tue, 01 Jun 2021 21:03:02
len(scripts['bnf_code'])# Tue, 01 Jun 2021 21:03:03
scripts['bnf_code'].unique()# Tue, 01 Jun 2021 21:03:04
p = 1/scripts['bnf_code'].nunique()# Tue, 01 Jun 2021 21:03:05
p# Tue, 01 Jun 2021 21:03:06
set(scripts['bnf_code'])# Tue, 01 Jun 2021 21:03:08
len(set(scripts['bnf_code']))# Tue, 01 Jun 2021 21:03:10
p = 1 / len(set(scripts['bnf_code']))# Tue, 01 Jun 2021 21:03:12
p
# Tue, 01 Jun 2021 21:03:14
scripts['bnf_code'].value_counts()# Tue, 01 Jun 2021 21:03:15
scripts['bnf_code'].count()# Tue, 01 Jun 2021 21:03:17
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()# Tue, 01 Jun 2021 21:03:19
rates# Tue, 01 Jun 2021 21:03:20
rare_codes = set(rates[rates < 0.1*p].index)# Tue, 01 Jun 2021 21:03:21
rare_codes# Tue, 01 Jun 2021 21:03:23
len(rare_codes)# Tue, 01 Jun 2021 21:03:25
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]# Tue, 01 Jun 2021 21:05:55
rates = scripts['bnf_code'].value_counts(normalize=True)# Tue, 01 Jun 2021 21:06:11
rates# Tue, 01 Jun 2021 21:06:29
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]# Tue, 01 Jun 2021 21:10:13
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)# Tue, 01 Jun 2021 21:10:49
scripts.head# Tue, 01 Jun 2021 21:11:33
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('dw-data/practices.csv.gz', names=col_names, header=None)
practices.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.tail()
fields = ['items','nic','act_cost','quantity']
scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T #add .T to transpose
#count shows us the total number of rows
scripts[fields].sum() #computes the sum of each these columns
scripts[fields].sum().index #to get the index or column. 
scripts[['act_cost','quantity']].sum() #computes the sum of each these columns
#create new data frame ; total, mean, std, 25%, 50%, 75% quartile
summary = pd.concat([scripts[fields].sum() ,scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T], axis = 1)
summary
summary.columns = ['total','mean', 'std','25%', '50%', '75%']
summary
for i in summary.itertuples():
    print (i[0], i[1:])
summary_stats = [(i[0], i[1:] )for i in summary.itertuples()]
summary_stats 
# summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]
grader.score.dw__summary_statistics(summary_stats)
group_bnf = scripts.groupby('bnf_name')
type(group_bnf)
scripts.loc[group_bnf.groups['A2A Spacer']]
 item_totals = group_bnf.sum()['items']
group_bnf.sum()['items'].sort_values(ascending = False)[:1]
max_item = item_totals.idxmax()
max_item
most_common_item = [(max_item, item_totals[max_item])]
most_common_item
# most_common_item = [("", 0)]
grader.score.dw__most_common_item(most_common_item)
scripts.head()
practices.head()
practices.sort_values('post_code').groupby('code').groups['A81001']
practices[ practices['code'] == 'A81001']
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()
unique_practices.head()
joined = scripts[['practice','bnf_name','items']].merge(unique_practices[['code','post_code']], how='left', left_on='practice' , right_on='code')[['bnf_name','items','post_code']]
joined.head()
post_item_totals = joined.groupby(['post_code','bnf_name']).sum().reset_index()
post_item_totals.head()
max_items = post_item_totals.sort_values('items', ascending=False).groupby('post_code').first()
max_items
post_item_totals.groupby('post_code')['items'].sum()
max_items['items']
max_items['items'] = max_items['items']/ post_item_totals.groupby('post_code')['items'].sum()
max_items = max_items.reset_index().sort_values('post_code')
max_items
[(item.post_code, item.bnf_name, item.items) for item in max_items.itertuples()]
items_by_region = [(item[1:]) for item in max_items.itertuples()][:100]
# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
max_items.to_csv('dw-data/max_items.csv') #we are saving the dataframe as a csv file
import dill
with open('dw-data/max_items.dill' , 'wb') as f:
    dill.dump(max_items, f) #dill and dump my max_items file into f
with open('dw-data/max_items.dill' , 'rb') as f:
    new_max_items = dill.load(f)
new_max_items.head()
max_items == new_max_items
np.all(max_items == new_max_items)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
chem['NAME'].dtype
chem[['NAME']].info()
chem['NAME'].str.contains('|'.join(opioids), case=False)
'|'.join(opioids)
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes).sum()
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = np.sqrt(scripts['opioid'].var()/scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores
opioid_scores.to_frame().rename(columns={0: 'z-score'})
unique_practices_by_name = practices.groupby('code')['name'].min().reset_index()
unique_practices_by_name.head()
scripts['practice'].value_counts().to_frame().rename(columns={'practice': 'count'})
joined = unique_practices_by_name\
    .merge(opioid_scores.to_frame()\
    .rename(columns={0: 'z-score'}), left_on='code', right_index=True)\
    .merge(scripts['practice'].value_counts()\
           .to_frame().rename(columns={'practice': 'count'}), left_on='code', right_index=True)
anomalies = [i[1:] for i in joined.sort_values('z-score', ascending=False).itertuples() ][:100]#we are sorting the zscore values in descending order
anomalies
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('dw-data/201606scripts_sample.csv.gz')
bnf_totals_2016 = scripts16['bnf_name'].value_counts()
bnf_totals_2016
bnf_totals_2017 = scripts['bnf_name'].value_counts()
bnf_totals_2017
growth_rate = (bnf_totals_2017 - bnf_totals_2016) / bnf_totals_2016
growth_rate
growth_rate.rename('growth_rate')
pd.concat([growth_rate, bnf_totals_2016], axis=1)
pd.concat([growth_rate.rename('growth_rate'), bnf_totals_2016.rename('count')], axis=1).reset_index()
df = pd.concat([growth_rate.rename('growth_rate'), 
           bnf_totals_2016.rename('count')], axis=1).reset_index()\
           .rename(columns={'index': 'bnf_name'})
df = df[(df['count'] >= 50) & (~df['growth_rate'].isna())].sort_values('growth_rate', ascending=False) #~ MEANS not in python
len(df)
script_growth = pd.concat([df.head(50), df.tail(50)])
len(script_growth)
script_growth.head()
#script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100
script_growth = [item[1:] for item in script_growth.itertuples()]
script_growth
grader.score.dw__script_growth(script_growth)
len(scripts['bnf_code'])
p = 1/scripts['bnf_code'].nunique()
p
rare_codes = set(rates[rates < 0.1*p].index)
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
len(scripts['bnf_code'])
scripts['bnf_code'].unique()
p = 1/scripts['bnf_code'].nunique()
p
set(scripts['bnf_code'])
len(set(scripts['bnf_code']))
p = 1 / len(set(scripts['bnf_code']))
p
scripts['bnf_code'].value_counts()
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
rates = scripts['bnf_code'].value_counts(normalize=True)
rates
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)
scripts.head
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 21:15:10
scripts.head()# Tue, 01 Jun 2021 21:18:31
rare_cost_prop = scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()# Tue, 01 Jun 2021 21:19:40
rare_cost_prop# Tue, 01 Jun 2021 21:19:41
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('dw-data/practices.csv.gz', names=col_names, header=None)
practices.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.tail()
fields = ['items','nic','act_cost','quantity']
scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T #add .T to transpose
#count shows us the total number of rows
scripts[fields].sum() #computes the sum of each these columns
scripts[fields].sum().index #to get the index or column. 
scripts[['act_cost','quantity']].sum() #computes the sum of each these columns
#create new data frame ; total, mean, std, 25%, 50%, 75% quartile
summary = pd.concat([scripts[fields].sum() ,scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T], axis = 1)
summary
summary.columns = ['total','mean', 'std','25%', '50%', '75%']
summary
for i in summary.itertuples():
    print (i[0], i[1:])
summary_stats = [(i[0], i[1:] )for i in summary.itertuples()]
summary_stats 
# summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]
grader.score.dw__summary_statistics(summary_stats)
group_bnf = scripts.groupby('bnf_name')
type(group_bnf)
scripts.loc[group_bnf.groups['A2A Spacer']]
 item_totals = group_bnf.sum()['items']
group_bnf.sum()['items'].sort_values(ascending = False)[:1]
max_item = item_totals.idxmax()
max_item
most_common_item = [(max_item, item_totals[max_item])]
most_common_item
# most_common_item = [("", 0)]
grader.score.dw__most_common_item(most_common_item)
scripts.head()
practices.head()
practices.sort_values('post_code').groupby('code').groups['A81001']
practices[ practices['code'] == 'A81001']
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()
unique_practices.head()
joined = scripts[['practice','bnf_name','items']].merge(unique_practices[['code','post_code']], how='left', left_on='practice' , right_on='code')[['bnf_name','items','post_code']]
joined.head()
post_item_totals = joined.groupby(['post_code','bnf_name']).sum().reset_index()
post_item_totals.head()
max_items = post_item_totals.sort_values('items', ascending=False).groupby('post_code').first()
max_items
post_item_totals.groupby('post_code')['items'].sum()
max_items['items']
max_items['items'] = max_items['items']/ post_item_totals.groupby('post_code')['items'].sum()
max_items = max_items.reset_index().sort_values('post_code')
max_items
[(item.post_code, item.bnf_name, item.items) for item in max_items.itertuples()]
items_by_region = [(item[1:]) for item in max_items.itertuples()][:100]
# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
max_items.to_csv('dw-data/max_items.csv') #we are saving the dataframe as a csv file
import dill
with open('dw-data/max_items.dill' , 'wb') as f:
    dill.dump(max_items, f) #dill and dump my max_items file into f
with open('dw-data/max_items.dill' , 'rb') as f:
    new_max_items = dill.load(f)
new_max_items.head()
max_items == new_max_items
np.all(max_items == new_max_items)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
chem['NAME'].dtype
chem[['NAME']].info()
chem['NAME'].str.contains('|'.join(opioids), case=False)
'|'.join(opioids)
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes).sum()
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = np.sqrt(scripts['opioid'].var()/scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores
opioid_scores.to_frame().rename(columns={0: 'z-score'})
unique_practices_by_name = practices.groupby('code')['name'].min().reset_index()
unique_practices_by_name.head()
scripts['practice'].value_counts().to_frame().rename(columns={'practice': 'count'})
joined = unique_practices_by_name\
    .merge(opioid_scores.to_frame()\
    .rename(columns={0: 'z-score'}), left_on='code', right_index=True)\
    .merge(scripts['practice'].value_counts()\
           .to_frame().rename(columns={'practice': 'count'}), left_on='code', right_index=True)
anomalies = [i[1:] for i in joined.sort_values('z-score', ascending=False).itertuples() ][:100]#we are sorting the zscore values in descending order
anomalies
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('dw-data/201606scripts_sample.csv.gz')
bnf_totals_2016 = scripts16['bnf_name'].value_counts()
bnf_totals_2016
bnf_totals_2017 = scripts['bnf_name'].value_counts()
bnf_totals_2017
growth_rate = (bnf_totals_2017 - bnf_totals_2016) / bnf_totals_2016
growth_rate
growth_rate.rename('growth_rate')
pd.concat([growth_rate, bnf_totals_2016], axis=1)
pd.concat([growth_rate.rename('growth_rate'), bnf_totals_2016.rename('count')], axis=1).reset_index()
df = pd.concat([growth_rate.rename('growth_rate'), 
           bnf_totals_2016.rename('count')], axis=1).reset_index()\
           .rename(columns={'index': 'bnf_name'})
df = df[(df['count'] >= 50) & (~df['growth_rate'].isna())].sort_values('growth_rate', ascending=False) #~ MEANS not in python
len(df)
script_growth = pd.concat([df.head(50), df.tail(50)])
len(script_growth)
script_growth.head()
#script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100
script_growth = [item[1:] for item in script_growth.itertuples()]
script_growth
grader.score.dw__script_growth(script_growth)
len(scripts['bnf_code'])
p = 1/scripts['bnf_code'].nunique()
p
rare_codes = set(rates[rates < 0.1*p].index)
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
len(scripts['bnf_code'])
scripts['bnf_code'].unique()
p = 1/scripts['bnf_code'].nunique()
p
set(scripts['bnf_code'])
len(set(scripts['bnf_code']))
p = 1 / len(set(scripts['bnf_code']))
p
scripts['bnf_code'].value_counts()
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
rates = scripts['bnf_code'].value_counts(normalize=True)
rates
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)
scripts.head
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts.head()
rare_cost_prop = scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()
rare_cost_prop
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 21:20:20
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('dw-data/practices.csv.gz', names=col_names, header=None)
practices.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.tail()
fields = ['items','nic','act_cost','quantity']
scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T #add .T to transpose
#count shows us the total number of rows
scripts[fields].sum() #computes the sum of each these columns
scripts[fields].sum().index #to get the index or column. 
scripts[['act_cost','quantity']].sum() #computes the sum of each these columns
#create new data frame ; total, mean, std, 25%, 50%, 75% quartile
summary = pd.concat([scripts[fields].sum() ,scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T], axis = 1)
summary
summary.columns = ['total','mean', 'std','25%', '50%', '75%']
summary
for i in summary.itertuples():
    print (i[0], i[1:])
summary_stats = [(i[0], i[1:] )for i in summary.itertuples()]
summary_stats 
# summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]
grader.score.dw__summary_statistics(summary_stats)
group_bnf = scripts.groupby('bnf_name')
type(group_bnf)
scripts.loc[group_bnf.groups['A2A Spacer']]
 item_totals = group_bnf.sum()['items']
group_bnf.sum()['items'].sort_values(ascending = False)[:1]
max_item = item_totals.idxmax()
max_item
most_common_item = [(max_item, item_totals[max_item])]
most_common_item
# most_common_item = [("", 0)]
grader.score.dw__most_common_item(most_common_item)
scripts.head()
practices.head()
practices.sort_values('post_code').groupby('code').groups['A81001']
practices[ practices['code'] == 'A81001']
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()
unique_practices.head()
joined = scripts[['practice','bnf_name','items']].merge(unique_practices[['code','post_code']], how='left', left_on='practice' , right_on='code')[['bnf_name','items','post_code']]
joined.head()
post_item_totals = joined.groupby(['post_code','bnf_name']).sum().reset_index()
post_item_totals.head()
max_items = post_item_totals.sort_values('items', ascending=False).groupby('post_code').first()
max_items
post_item_totals.groupby('post_code')['items'].sum()
max_items['items']
max_items['items'] = max_items['items']/ post_item_totals.groupby('post_code')['items'].sum()
max_items = max_items.reset_index().sort_values('post_code')
max_items
[(item.post_code, item.bnf_name, item.items) for item in max_items.itertuples()]
items_by_region = [(item[1:]) for item in max_items.itertuples()][:100]
# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
max_items.to_csv('dw-data/max_items.csv') #we are saving the dataframe as a csv file
import dill
with open('dw-data/max_items.dill' , 'wb') as f:
    dill.dump(max_items, f) #dill and dump my max_items file into f
with open('dw-data/max_items.dill' , 'rb') as f:
    new_max_items = dill.load(f)
new_max_items.head()
max_items == new_max_items
np.all(max_items == new_max_items)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
chem['NAME'].dtype
chem[['NAME']].info()
chem['NAME'].str.contains('|'.join(opioids), case=False)
'|'.join(opioids)
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes).sum()
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = np.sqrt(scripts['opioid'].var()/scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores
opioid_scores.to_frame().rename(columns={0: 'z-score'})
unique_practices_by_name = practices.groupby('code')['name'].min().reset_index()
unique_practices_by_name.head()
scripts['practice'].value_counts().to_frame().rename(columns={'practice': 'count'})
joined = unique_practices_by_name\
    .merge(opioid_scores.to_frame()\
    .rename(columns={0: 'z-score'}), left_on='code', right_index=True)\
    .merge(scripts['practice'].value_counts()\
           .to_frame().rename(columns={'practice': 'count'}), left_on='code', right_index=True)
anomalies = [i[1:] for i in joined.sort_values('z-score', ascending=False).itertuples() ][:100]#we are sorting the zscore values in descending order
anomalies
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('dw-data/201606scripts_sample.csv.gz')
bnf_totals_2016 = scripts16['bnf_name'].value_counts()
bnf_totals_2016
bnf_totals_2017 = scripts['bnf_name'].value_counts()
bnf_totals_2017
growth_rate = (bnf_totals_2017 - bnf_totals_2016) / bnf_totals_2016
growth_rate
growth_rate.rename('growth_rate')
pd.concat([growth_rate, bnf_totals_2016], axis=1)
pd.concat([growth_rate.rename('growth_rate'), bnf_totals_2016.rename('count')], axis=1).reset_index()
df = pd.concat([growth_rate.rename('growth_rate'), 
           bnf_totals_2016.rename('count')], axis=1).reset_index()\
           .rename(columns={'index': 'bnf_name'})
df = df[(df['count'] >= 50) & (~df['growth_rate'].isna())].sort_values('growth_rate', ascending=False) #~ MEANS not in python
len(df)
script_growth = pd.concat([df.head(50), df.tail(50)])
len(script_growth)
script_growth.head()
#script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100
script_growth = [item[1:] for item in script_growth.itertuples()]
script_growth
grader.score.dw__script_growth(script_growth)
len(scripts['bnf_code'])
p = 1/scripts['bnf_code'].nunique()
p
rare_codes = set(rates[rates < 0.1*p].index)
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
len(scripts['bnf_code'])
scripts['bnf_code'].unique()
p = 1/scripts['bnf_code'].nunique()
p
set(scripts['bnf_code'])
len(set(scripts['bnf_code']))
p = 1 / len(set(scripts['bnf_code']))
p
scripts['bnf_code'].value_counts()
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
rates = scripts['bnf_code'].value_counts(normalize=True)
rates
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)
scripts.head
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts.head()
rare_cost_prop = scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()
rare_cost_prop
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 21:21:11
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)# Tue, 01 Jun 2021 21:21:21
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)# Tue, 01 Jun 2021 21:21:22
rare_cost_prop# Tue, 01 Jun 2021 21:25:49
relative_rare_cost_prop = rare_cost_prop - scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.['act_cost'].sum()# Tue, 01 Jun 2021 21:27:25
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('dw-data/practices.csv.gz', names=col_names, header=None)
practices.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.tail()
fields = ['items','nic','act_cost','quantity']
scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T #add .T to transpose
#count shows us the total number of rows
scripts[fields].sum() #computes the sum of each these columns
scripts[fields].sum().index #to get the index or column. 
scripts[['act_cost','quantity']].sum() #computes the sum of each these columns
#create new data frame ; total, mean, std, 25%, 50%, 75% quartile
summary = pd.concat([scripts[fields].sum() ,scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T], axis = 1)
summary
summary.columns = ['total','mean', 'std','25%', '50%', '75%']
summary
for i in summary.itertuples():
    print (i[0], i[1:])
summary_stats = [(i[0], i[1:] )for i in summary.itertuples()]
summary_stats 
# summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]
grader.score.dw__summary_statistics(summary_stats)
group_bnf = scripts.groupby('bnf_name')
type(group_bnf)
scripts.loc[group_bnf.groups['A2A Spacer']]
 item_totals = group_bnf.sum()['items']
group_bnf.sum()['items'].sort_values(ascending = False)[:1]
max_item = item_totals.idxmax()
max_item
most_common_item = [(max_item, item_totals[max_item])]
most_common_item
# most_common_item = [("", 0)]
grader.score.dw__most_common_item(most_common_item)
scripts.head()
practices.head()
practices.sort_values('post_code').groupby('code').groups['A81001']
practices[ practices['code'] == 'A81001']
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()
unique_practices.head()
joined = scripts[['practice','bnf_name','items']].merge(unique_practices[['code','post_code']], how='left', left_on='practice' , right_on='code')[['bnf_name','items','post_code']]
joined.head()
post_item_totals = joined.groupby(['post_code','bnf_name']).sum().reset_index()
post_item_totals.head()
max_items = post_item_totals.sort_values('items', ascending=False).groupby('post_code').first()
max_items
post_item_totals.groupby('post_code')['items'].sum()
max_items['items']
max_items['items'] = max_items['items']/ post_item_totals.groupby('post_code')['items'].sum()
max_items = max_items.reset_index().sort_values('post_code')
max_items
[(item.post_code, item.bnf_name, item.items) for item in max_items.itertuples()]
items_by_region = [(item[1:]) for item in max_items.itertuples()][:100]
# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
max_items.to_csv('dw-data/max_items.csv') #we are saving the dataframe as a csv file
import dill
with open('dw-data/max_items.dill' , 'wb') as f:
    dill.dump(max_items, f) #dill and dump my max_items file into f
with open('dw-data/max_items.dill' , 'rb') as f:
    new_max_items = dill.load(f)
new_max_items.head()
max_items == new_max_items
np.all(max_items == new_max_items)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
chem['NAME'].dtype
chem[['NAME']].info()
chem['NAME'].str.contains('|'.join(opioids), case=False)
'|'.join(opioids)
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes).sum()
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = np.sqrt(scripts['opioid'].var()/scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores
opioid_scores.to_frame().rename(columns={0: 'z-score'})
unique_practices_by_name = practices.groupby('code')['name'].min().reset_index()
unique_practices_by_name.head()
scripts['practice'].value_counts().to_frame().rename(columns={'practice': 'count'})
joined = unique_practices_by_name\
    .merge(opioid_scores.to_frame()\
    .rename(columns={0: 'z-score'}), left_on='code', right_index=True)\
    .merge(scripts['practice'].value_counts()\
           .to_frame().rename(columns={'practice': 'count'}), left_on='code', right_index=True)
anomalies = [i[1:] for i in joined.sort_values('z-score', ascending=False).itertuples() ][:100]#we are sorting the zscore values in descending order
anomalies
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('dw-data/201606scripts_sample.csv.gz')
bnf_totals_2016 = scripts16['bnf_name'].value_counts()
bnf_totals_2016
bnf_totals_2017 = scripts['bnf_name'].value_counts()
bnf_totals_2017
growth_rate = (bnf_totals_2017 - bnf_totals_2016) / bnf_totals_2016
growth_rate
growth_rate.rename('growth_rate')
pd.concat([growth_rate, bnf_totals_2016], axis=1)
pd.concat([growth_rate.rename('growth_rate'), bnf_totals_2016.rename('count')], axis=1).reset_index()
df = pd.concat([growth_rate.rename('growth_rate'), 
           bnf_totals_2016.rename('count')], axis=1).reset_index()\
           .rename(columns={'index': 'bnf_name'})
df = df[(df['count'] >= 50) & (~df['growth_rate'].isna())].sort_values('growth_rate', ascending=False) #~ MEANS not in python
len(df)
script_growth = pd.concat([df.head(50), df.tail(50)])
len(script_growth)
script_growth.head()
#script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100
script_growth = [item[1:] for item in script_growth.itertuples()]
script_growth
grader.score.dw__script_growth(script_growth)
len(scripts['bnf_code'])
p = 1/scripts['bnf_code'].nunique()
p
rare_codes = set(rates[rates < 0.1*p].index)
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
len(scripts['bnf_code'])
scripts['bnf_code'].unique()
p = 1/scripts['bnf_code'].nunique()
p
set(scripts['bnf_code'])
len(set(scripts['bnf_code']))
p = 1 / len(set(scripts['bnf_code']))
p
scripts['bnf_code'].value_counts()
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
rates = scripts['bnf_code'].value_counts(normalize=True)
rates
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)
scripts.head
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts.head()
rare_cost_prop = scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()
rare_cost_prop
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)
rare_cost_prop
relative_rare_cost_prop = rare_cost_prop - scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.['act_cost'].sum()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 21:27:39
relative_rare_cost_prop = rare_cost_prop\
              - scripts[scripts['rare']]['act_cost'].sum() / scripts['act_cost'].sum()# Tue, 01 Jun 2021 21:27:58
relative_rare_cost_prop# Tue, 01 Jun 2021 21:29:47
standard_errors = relative_rare_cost_prop.std()# Tue, 01 Jun 2021 21:29:58
standard_errors# Tue, 01 Jun 2021 21:30:47
rare_scores = relative_rare_cost_prop / standard_errors# Tue, 01 Jun 2021 21:31:03
rare_scores# Tue, 01 Jun 2021 21:32:27
rare_scores = (relative_rare_cost_prop / standard_errors).reset_index()# Tue, 01 Jun 2021 21:32:28
rare_scores# Tue, 01 Jun 2021 21:35:01
rare_scores = (relative_rare_cost_prop / standard_errors).reset_index().rename(columns={'act_cost':'z-score'})# Tue, 01 Jun 2021 21:35:09
rare_scores# Tue, 01 Jun 2021 21:37:34
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('dw-data/practices.csv.gz', names=col_names, header=None)
practices.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.tail()
fields = ['items','nic','act_cost','quantity']
scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T #add .T to transpose
#count shows us the total number of rows
scripts[fields].sum() #computes the sum of each these columns
scripts[fields].sum().index #to get the index or column. 
scripts[['act_cost','quantity']].sum() #computes the sum of each these columns
#create new data frame ; total, mean, std, 25%, 50%, 75% quartile
summary = pd.concat([scripts[fields].sum() ,scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T], axis = 1)
summary
summary.columns = ['total','mean', 'std','25%', '50%', '75%']
summary
for i in summary.itertuples():
    print (i[0], i[1:])
summary_stats = [(i[0], i[1:] )for i in summary.itertuples()]
summary_stats 
# summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]
grader.score.dw__summary_statistics(summary_stats)
group_bnf = scripts.groupby('bnf_name')
type(group_bnf)
scripts.loc[group_bnf.groups['A2A Spacer']]
 item_totals = group_bnf.sum()['items']
group_bnf.sum()['items'].sort_values(ascending = False)[:1]
max_item = item_totals.idxmax()
max_item
most_common_item = [(max_item, item_totals[max_item])]
most_common_item
# most_common_item = [("", 0)]
grader.score.dw__most_common_item(most_common_item)
scripts.head()
practices.head()
practices.sort_values('post_code').groupby('code').groups['A81001']
practices[ practices['code'] == 'A81001']
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()
unique_practices.head()
joined = scripts[['practice','bnf_name','items']].merge(unique_practices[['code','post_code']], how='left', left_on='practice' , right_on='code')[['bnf_name','items','post_code']]
joined.head()
post_item_totals = joined.groupby(['post_code','bnf_name']).sum().reset_index()
post_item_totals.head()
max_items = post_item_totals.sort_values('items', ascending=False).groupby('post_code').first()
max_items
post_item_totals.groupby('post_code')['items'].sum()
max_items['items']
max_items['items'] = max_items['items']/ post_item_totals.groupby('post_code')['items'].sum()
max_items = max_items.reset_index().sort_values('post_code')
max_items
[(item.post_code, item.bnf_name, item.items) for item in max_items.itertuples()]
items_by_region = [(item[1:]) for item in max_items.itertuples()][:100]
# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
max_items.to_csv('dw-data/max_items.csv') #we are saving the dataframe as a csv file
import dill
with open('dw-data/max_items.dill' , 'wb') as f:
    dill.dump(max_items, f) #dill and dump my max_items file into f
with open('dw-data/max_items.dill' , 'rb') as f:
    new_max_items = dill.load(f)
new_max_items.head()
max_items == new_max_items
np.all(max_items == new_max_items)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
chem['NAME'].dtype
chem[['NAME']].info()
chem['NAME'].str.contains('|'.join(opioids), case=False)
'|'.join(opioids)
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes).sum()
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = np.sqrt(scripts['opioid'].var()/scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores
opioid_scores.to_frame().rename(columns={0: 'z-score'})
unique_practices_by_name = practices.groupby('code')['name'].min().reset_index()
unique_practices_by_name.head()
scripts['practice'].value_counts().to_frame().rename(columns={'practice': 'count'})
joined = unique_practices_by_name\
    .merge(opioid_scores.to_frame()\
    .rename(columns={0: 'z-score'}), left_on='code', right_index=True)\
    .merge(scripts['practice'].value_counts()\
           .to_frame().rename(columns={'practice': 'count'}), left_on='code', right_index=True)
anomalies = [i[1:] for i in joined.sort_values('z-score', ascending=False).itertuples() ][:100]#we are sorting the zscore values in descending order
anomalies
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('dw-data/201606scripts_sample.csv.gz')
bnf_totals_2016 = scripts16['bnf_name'].value_counts()
bnf_totals_2016
bnf_totals_2017 = scripts['bnf_name'].value_counts()
bnf_totals_2017
growth_rate = (bnf_totals_2017 - bnf_totals_2016) / bnf_totals_2016
growth_rate
growth_rate.rename('growth_rate')
pd.concat([growth_rate, bnf_totals_2016], axis=1)
pd.concat([growth_rate.rename('growth_rate'), bnf_totals_2016.rename('count')], axis=1).reset_index()
df = pd.concat([growth_rate.rename('growth_rate'), 
           bnf_totals_2016.rename('count')], axis=1).reset_index()\
           .rename(columns={'index': 'bnf_name'})
df = df[(df['count'] >= 50) & (~df['growth_rate'].isna())].sort_values('growth_rate', ascending=False) #~ MEANS not in python
len(df)
script_growth = pd.concat([df.head(50), df.tail(50)])
len(script_growth)
script_growth.head()
#script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100
script_growth = [item[1:] for item in script_growth.itertuples()]
script_growth
grader.score.dw__script_growth(script_growth)
len(scripts['bnf_code'])
p = 1/scripts['bnf_code'].nunique()
p
rare_codes = set(rates[rates < 0.1*p].index)
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
len(scripts['bnf_code'])
scripts['bnf_code'].unique()
p = 1/scripts['bnf_code'].nunique()
p
set(scripts['bnf_code'])
len(set(scripts['bnf_code']))
p = 1 / len(set(scripts['bnf_code']))
p
scripts['bnf_code'].value_counts()
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
rates = scripts['bnf_code'].value_counts(normalize=True)
rates
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)
scripts.head
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts.head()
rare_cost_prop = scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()
rare_cost_prop
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)
rare_cost_prop
relative_rare_cost_prop = rare_cost_prop - scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.['act_cost'].sum()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
relative_rare_cost_prop = rare_cost_prop\
              - scripts[scripts['rare']]['act_cost'].sum() / scripts['act_cost'].sum()
relative_rare_cost_prop
standard_errors = relative_rare_cost_prop.std()
standard_errors
rare_scores = relative_rare_cost_prop / standard_errors
rare_scores
rare_scores = (relative_rare_cost_prop / standard_errors).reset_index()
rare_scores
rare_scores = (relative_rare_cost_prop / standard_errors).reset_index().rename(columns={'act_cost':'z-score'})
rare_scores
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 21:39:49
rare_scores['practice_name'] = rare_scores['practice'].apply(lambda code: unique_practices_by_name[code])# Tue, 01 Jun 2021 21:43:38
rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')# Tue, 01 Jun 2021 21:45:13
rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')[['code', 'name', 'z-score']]# Tue, 01 Jun 2021 21:47:04
rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')[['code', 'name', 'z-score']].sort_values('z-score', ascending=False)# Tue, 01 Jun 2021 21:49:32
rare_scores.head# Tue, 01 Jun 2021 21:49:48
rare_scores.head()# Tue, 01 Jun 2021 21:50:29
rare_scores = rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')[['code', 'name', 'z-score']].sort_values('z-score', ascending=False)# Tue, 01 Jun 2021 21:50:32
rare_scores.head()# Tue, 01 Jun 2021 21:52:47
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('dw-data/practices.csv.gz', names=col_names, header=None)
practices.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.head()
chem = pd.read_csv('dw-data/chem.csv.gz')
chem.tail()
fields = ['items','nic','act_cost','quantity']
scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T #add .T to transpose
#count shows us the total number of rows
scripts[fields].sum() #computes the sum of each these columns
scripts[fields].sum().index #to get the index or column. 
scripts[['act_cost','quantity']].sum() #computes the sum of each these columns
#create new data frame ; total, mean, std, 25%, 50%, 75% quartile
summary = pd.concat([scripts[fields].sum() ,scripts[fields].describe().loc[['mean', 'std','25%', '50%', '75%']].T], axis = 1)
summary
summary.columns = ['total','mean', 'std','25%', '50%', '75%']
summary
for i in summary.itertuples():
    print (i[0], i[1:])
summary_stats = [(i[0], i[1:] )for i in summary.itertuples()]
summary_stats 
# summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]
grader.score.dw__summary_statistics(summary_stats)
group_bnf = scripts.groupby('bnf_name')
type(group_bnf)
scripts.loc[group_bnf.groups['A2A Spacer']]
 item_totals = group_bnf.sum()['items']
group_bnf.sum()['items'].sort_values(ascending = False)[:1]
max_item = item_totals.idxmax()
max_item
most_common_item = [(max_item, item_totals[max_item])]
most_common_item
# most_common_item = [("", 0)]
grader.score.dw__most_common_item(most_common_item)
scripts.head()
practices.head()
practices.sort_values('post_code').groupby('code').groups['A81001']
practices[ practices['code'] == 'A81001']
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()
unique_practices.head()
joined = scripts[['practice','bnf_name','items']].merge(unique_practices[['code','post_code']], how='left', left_on='practice' , right_on='code')[['bnf_name','items','post_code']]
joined.head()
post_item_totals = joined.groupby(['post_code','bnf_name']).sum().reset_index()
post_item_totals.head()
max_items = post_item_totals.sort_values('items', ascending=False).groupby('post_code').first()
max_items
post_item_totals.groupby('post_code')['items'].sum()
max_items['items']
max_items['items'] = max_items['items']/ post_item_totals.groupby('post_code')['items'].sum()
max_items = max_items.reset_index().sort_values('post_code')
max_items
[(item.post_code, item.bnf_name, item.items) for item in max_items.itertuples()]
items_by_region = [(item[1:]) for item in max_items.itertuples()][:100]
# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
max_items.to_csv('dw-data/max_items.csv') #we are saving the dataframe as a csv file
import dill
with open('dw-data/max_items.dill' , 'wb') as f:
    dill.dump(max_items, f) #dill and dump my max_items file into f
with open('dw-data/max_items.dill' , 'rb') as f:
    new_max_items = dill.load(f)
new_max_items.head()
max_items == new_max_items
np.all(max_items == new_max_items)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
chem['NAME'].dtype
chem[['NAME']].info()
chem['NAME'].str.contains('|'.join(opioids), case=False)
'|'.join(opioids)
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes).sum()
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = np.sqrt(scripts['opioid'].var()/scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores
opioid_scores.to_frame().rename(columns={0: 'z-score'})
unique_practices_by_name = practices.groupby('code')['name'].min().reset_index()
unique_practices_by_name.head()
scripts['practice'].value_counts().to_frame().rename(columns={'practice': 'count'})
joined = unique_practices_by_name\
    .merge(opioid_scores.to_frame()\
    .rename(columns={0: 'z-score'}), left_on='code', right_index=True)\
    .merge(scripts['practice'].value_counts()\
           .to_frame().rename(columns={'practice': 'count'}), left_on='code', right_index=True)
anomalies = [i[1:] for i in joined.sort_values('z-score', ascending=False).itertuples() ][:100]#we are sorting the zscore values in descending order
anomalies
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('dw-data/201606scripts_sample.csv.gz')
bnf_totals_2016 = scripts16['bnf_name'].value_counts()
bnf_totals_2016
bnf_totals_2017 = scripts['bnf_name'].value_counts()
bnf_totals_2017
growth_rate = (bnf_totals_2017 - bnf_totals_2016) / bnf_totals_2016
growth_rate
growth_rate.rename('growth_rate')
pd.concat([growth_rate, bnf_totals_2016], axis=1)
pd.concat([growth_rate.rename('growth_rate'), bnf_totals_2016.rename('count')], axis=1).reset_index()
df = pd.concat([growth_rate.rename('growth_rate'), 
           bnf_totals_2016.rename('count')], axis=1).reset_index()\
           .rename(columns={'index': 'bnf_name'})
df = df[(df['count'] >= 50) & (~df['growth_rate'].isna())].sort_values('growth_rate', ascending=False) #~ MEANS not in python
len(df)
script_growth = pd.concat([df.head(50), df.tail(50)])
len(script_growth)
script_growth.head()
#script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100
script_growth = [item[1:] for item in script_growth.itertuples()]
script_growth
grader.score.dw__script_growth(script_growth)
len(scripts['bnf_code'])
p = 1/scripts['bnf_code'].nunique()
p
rare_codes = set(rates[rates < 0.1*p].index)
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] =  scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
len(scripts['bnf_code'])
scripts['bnf_code'].unique()
p = 1/scripts['bnf_code'].nunique()
p
set(scripts['bnf_code'])
len(set(scripts['bnf_code']))
p = 1 / len(set(scripts['bnf_code']))
p
scripts['bnf_code'].value_counts()
scripts['bnf_code'].count()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rates
rare_codes = set(rates[rates < 0.1*p].index)
rare_codes
len(rare_codes)
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
rates = scripts['bnf_code'].value_counts(normalize=True)
rates
scripts['rare'] = scripts['bnf_code'].isin[rare_codes]
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)
scripts.head
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts.head()
rare_cost_prop = scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()
rare_cost_prop
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)
rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.groupby('practice')['act_cost'].sum()).fillna(0)
rare_cost_prop
relative_rare_cost_prop = rare_cost_prop - scripts[scripts['rare']].groupby('practice')['act_cost'].sum() / scripts.['act_cost'].sum()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
relative_rare_cost_prop = rare_cost_prop\
              - scripts[scripts['rare']]['act_cost'].sum() / scripts['act_cost'].sum()
relative_rare_cost_prop
standard_errors = relative_rare_cost_prop.std()
standard_errors
rare_scores = relative_rare_cost_prop / standard_errors
rare_scores
rare_scores = (relative_rare_cost_prop / standard_errors).reset_index()
rare_scores
rare_scores = (relative_rare_cost_prop / standard_errors).reset_index().rename(columns={'act_cost':'z-score'})
rare_scores
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
rare_scores['practice_name'] = rare_scores['practice'].apply(lambda code: unique_practices_by_name[code])
rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')
rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')[['code', 'name', 'z-score']]
rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')[['code', 'name', 'z-score']].sort_values('z-score', ascending=False)
rare_scores.head
rare_scores.head()
rare_scores = rare_scores.merge( unique_practices_by_name, left_on='practice', right_on='code', how='left')[['code', 'name', 'z-score']].sort_values('z-score', ascending=False)
rare_scores.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Tue, 01 Jun 2021 21:53:17
rare_scripts = [item[1:] for item in rare_scores.itertuples()][:100]# Tue, 01 Jun 2021 21:54:00
rare_scripts[:10]# Tue, 01 Jun 2021 21:54:10
grader.score.dw__rare_scripts(rare_scripts)