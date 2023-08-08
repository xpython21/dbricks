# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select "Hello World!"
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')

print(files)

# COMMAND ----------

display(files)
