!pip install pyspark
# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split
import matplotlib.pyplot as plt

# Create a SparkSession
spark = SparkSession.builder \
    .appName("SocialNetworkAnalysis") \
    .getOrCreate()

# Load your cleaned dataset into a Spark DataFrame
df = spark.read.csv("sns_addiction.csv", header=True, inferSchema=True)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
df.show(5)

# Print the schema of the DataFrame
print("Schema of the DataFrame:")
df.printSchema()

# Demographic Information
# Age distribution
print("Age distribution:")
age_distribution = df.groupBy("age").count().orderBy("age")
age_distribution.show()

# Gender distribution
print("Gender distribution:")
gender_distribution = df.groupBy("gender").count().orderBy("count", ascending=False)
gender_distribution.show()

# Feelings Towards Social Media
# Count of feelings after using social media
print("Feelings after using social media:")
feelings_count = df.groupBy("feelings_after_use").count().orderBy("count", ascending=False)
feelings_count.show()

# Count of respondents experiencing FOMO
print("Experience of FOMO (Fear of Missing Out):")
fomo_count = df.groupBy("fomo_experience").count().orderBy("count", ascending=False)
fomo_count.show()

# Count of respondents feeling addicted to social media
print("Feeling addicted to social media:")
addiction_count = df.groupBy("feel_addicted").count().orderBy("count", ascending=False)
addiction_count.show()

# Impact on Daily Life
# Count of respondents prioritizing social media over other activities
print("Prioritizing social media over other activities:")
prioritization_count = df.groupBy("prioritize_social_media").count().orderBy("count", ascending=False)
prioritization_count.show()

# Count of respondents finding it difficult to reduce social media usage
print("Difficulty in reducing social media usage:")
difficulty_count = df.groupBy("difficulty_reducing_usage").count().orderBy("count", ascending=False)
difficulty_count.show()

# Count of respondents experiencing negative consequences due to social media usage
print("Negative consequences due to social media usage:")
negative_consequences_count = df.groupBy("negative_consequences").count().orderBy("count", ascending=False)
negative_consequences_count.show()

# Self-Assessment
# Average social media addiction rating
print("Average social media addiction rating:")
average_addiction_rating = df.selectExpr("avg(addiction_rating)").collect()[0][0]
print("   ", average_addiction_rating)

# Reasons for Using Social Media
print("Reasons for using social media:")
reasons_for_using_social_media = df.groupBy("reasons_for_using_social_media").count().orderBy("count", ascending=False)
reasons_for_using_social_media.show()

# Usage of Social Media Platforms
print("Usage of social media platforms:")
# Split the column containing multiple platform selections into an array
df_with_platforms = df.withColumn("platforms_array", split(col("social_media_platforms_used"), ", "))
# Explode the array to create a new row for each platform
df_exploded = df_with_platforms.select(explode("platforms_array").alias("platform"))
# Count the occurrences of each platform
platform_count = df_exploded.groupBy("platform").count().orderBy("count", ascending=False)
platform_count.show()

# Visualize Age Distribution
print("Visualizing Age Distribution...")
age_distribution_pd = age_distribution.toPandas()
plt.bar(age_distribution_pd["age"], age_distribution_pd["count"])
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution")
plt.show()

# Visualize Gender Distribution
print("Visualizing Gender Distribution...")
gender_distribution_pd = gender_distribution.toPandas()
plt.bar(gender_distribution_pd["gender"], gender_distribution_pd["count"])
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")
plt.show()

# Visualize Feelings After Using Social Media
print("Visualizing Feelings After Using Social Media...")
feelings_count_pd = feelings_count.toPandas()
plt.bar(feelings_count_pd["feelings_after_use"], feelings_count_pd["count"])
plt.xlabel("Feelings After Using Social Media")
plt.ylabel("Count")
plt.title("Feelings After Using Social Media")
plt.xticks(rotation=45)
plt.show()

# Visualize Experience of FOMO
print("Visualizing Experience of FOMO...")
fomo_count_pd = fomo_count.toPandas()
plt.bar(fomo_count_pd["fomo_experience"], fomo_count_pd["count"])
plt.xlabel("Experience of FOMO")
plt.ylabel("Count")
plt.title("Experience of FOMO")
plt.show()

# Visualize Reasons for Using Social Media
print("Visualizing Reasons for Using Social Media...")
reasons_for_using_social_media_pd = reasons_for_using_social_media.toPandas()
plt.bar(reasons_for_using_social_media_pd["reasons_for_using_social_media"], reasons_for_using_social_media_pd["count"])
plt.xlabel("Reasons for Using Social Media")
plt.ylabel("Count")
plt.title("Reasons for Using Social Media")
plt.xticks(rotation=90)
plt.show()

# Stop the SparkSession
spark.stop()

