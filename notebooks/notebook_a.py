# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Notebooks Integration
# MAGIC This notebook test how databricks joins two differente notebooks and its variables references.

# COMMAND ----------

name = "Carla"

# COMMAND ----------

print(f"Hello {name}")

# COMMAND ----------

# MAGIC %run ./notebook_b

# COMMAND ----------

# MAGIC %md
# MAGIC The `full_name` variable was defined in `notebook_b`.

# COMMAND ----------

print(f"Welcome back {full_name}")

# COMMAND ----------


