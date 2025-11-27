# My_Notebooks
My Jupyter Notebooks in Python

Hi Team,
Here is a quick status update and the plan for the upcoming week regarding the ADD Project.
Current Status:
•	We now have access to both transaction and KYC profile data on Databricks.
•	I have created an intermediate table to speed up analysis since we cannot save processed data as parquet files.
•	The current KYC profile data contains a large number of missing or blank values. Gemma has already raised a Jira ticket for this.
•	We have presented the transaction data distribution across all customer types to Kris & team. The transaction data currently includes some outliers, which we will need to address later.
•	As discussed in yesterday’s call, we need to present customer tiers across each customer type.
•	The KYC team is expecting a first cut of customer tiers for at least one customer type by next week.
•	Since the KYC profile data has multiple missing data, the team has suggested starting with tiers based solely on transaction data, focusing on highlighting variability in the transaction distributions.
•	We will refine and update the tiers using KYC attributes at a later stage once that data quality improves.
•	The overall idea is to first demonstrate that the transaction data shows enough variability to justify creating different tiers and have the first draft of tears available. Once we confirm that variability for a specific customer type, we can then proceed to design the tiers and later integrate KYC-driven attributes.

Next steps:
•	Vrushali: Please take the lead on the strategic direction of this work. Anjuman and Shreyansh will handle development—ensure they stay aligned and prepare a few slides summarizing the created tiers for our next Wednesday connect.
•	Anjuman & Shreyansh: Please have the initial tiers ready for at least one customer type by Monday at the latest. Get feedback from the team and refine accordingly.
•	Vrushali: Please start drafting the slide deck and storyline so you can easily update it once the final tier data is available.

More details on how to create the Tiers based on transaction data:
Overall, our goal is to statistically validate the internal structure of the transaction data. If the data is tight (unimodal and low-variance) or it’s tiered (multimodal or heavy-tailed).
We can start the analysis, something like this – this is just directional, feel free to update accordingly.
1.	Basic overview: 
a.	Check Mean, variance, skewness & kurtosis. Although current transaction data is nearly log-normal so just the high skew does not necessarily imply distinct tiers
b.	Asthere are outliers in data, we can also check Median Absolute Deviation (MAD) and can check ratio of Standard deviation and MAD (SD/MAD). Higher value confirms that the perceived variance is driven by tail outliers rather than the central cluster.
c.	We might have to manually remove the outlier and recalculate the metrics and these extreme outlier will impact all the above and following metric. 
d.	We can also check Coefficient of Variation (CV), defined as the ratio of the standard deviation to the mean or Gini Coefficient 
e.	These should give you fair idea how does transaction data behaves but we would still need to figure out if there are Tiers in the data.
f.	I read somewhere that Hartigan’s Dip Test is specifically designed to distinguish between a single skewed distribution and a multimodal distribution, so will suggest to try that.   
I have added some of the way we can get the understanding of data distribution, but feel free to use whatever work best for you and wouldn’t suggest to spend much time here.
Also include some distribution plot to show the transaction distribution
2.	Deriving the Tiers based on transaction data
a.	We can use Gaussian Mixture Models (GMM) – we have tried this last time and it generated pretty intuitive results.
i.	Please insure we are doing all the data pre-processing is done before generating tiers mostly near zero transactions and extremes 
ii.	We would need to provide numbers of Tiers (k) and you can use Silverman’s Bandwidth Test for identifying the right value of k or just simple visualization can help.
iii.	You can also try Automatic Tier Selection using Bayesian GMM and Dirichlet Process
b.	Once the Tiers are created we should again show the mean, std and other metrics on generated tiers.

