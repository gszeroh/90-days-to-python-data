# 🐍 90 Days to Python for Data Science, AI & Data Engineering

A comprehensive, hands-on 90-day curriculum to take you from Python beginner to a proficient data professional. Each day includes theory, code examples, exercises, and mini-projects.

---

## 📋 Table of Contents

- [How to Use This Repository](#how-to-use-this-repository)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Curriculum Overview](#curriculum-overview)
- [Phase 1: Python Fundamentals (Days 1–20)](#phase-1-python-fundamentals-days-120)
- [Phase 2: Data Science Foundations (Days 21–40)](#phase-2-data-science-foundations-days-2140)
- [Phase 3: Machine Learning & AI (Days 41–60)](#phase-3-machine-learning--ai-days-4160)
- [Phase 4: Deep Learning & Advanced AI (Days 61–75)](#phase-4-deep-learning--advanced-ai-days-6175)
- [Phase 5: Data Engineering (Days 76–90)](#phase-5-data-engineering-days-7690)
- [Resources](#resources)
- [Contributing](#contributing)

---

## How to Use This Repository

1. **Follow the days in order** — each day builds on the previous one.
2. **Each day's folder** contains:
   - `README.md` — Theory, concepts, and explanations
   - `examples.py` or Jupyter notebook — Code examples
   - `exercises.py` — Practice exercises (with solutions in `solutions.py`)
3. **Spend 2–3 hours per day** for best results.
4. **Build the mini-projects** — they solidify your understanding.
5. **Track your progress** using the checklist below.

---

## Prerequisites

- A computer with internet access
- Basic computer literacy
- Curiosity and commitment to learn!

---

## Setup

```bash
# Clone this repository
git clone https://github.com/gszeroh/90-days-to-python-data.git
cd 90-days-to-python-data

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Curriculum Overview

| Phase | Days | Topics | Key Skills |
|-------|------|--------|------------|
| **1** | 1–20 | Python Fundamentals | Syntax, data structures, OOP, file I/O, testing |
| **2** | 21–40 | Data Science Foundations | NumPy, Pandas, Matplotlib, Seaborn, statistics, EDA |
| **3** | 41–60 | Machine Learning & AI | Scikit-learn, supervised/unsupervised ML, NLP, time series |
| **4** | 61–75 | Deep Learning & Advanced AI | TensorFlow/PyTorch, CNNs, RNNs, Transformers, LLMs |
| **5** | 76–90 | Data Engineering | SQL, ETL, Airflow, Spark, cloud platforms, capstone project |

---

## Phase 1: Python Fundamentals (Days 1–20)

> **Goal:** Master Python programming from the ground up.

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| [Day 01](phase1/day01/) | Python Setup & Hello World | Installing Python, IDEs, first program, REPL |
| [Day 02](phase1/day02/) | Variables & Data Types | int, float, str, bool, type conversion |
| [Day 03](phase1/day03/) | Strings Deep Dive | String methods, formatting, f-strings, slicing |
| [Day 04](phase1/day04/) | Operators & Expressions | Arithmetic, comparison, logical, bitwise operators |
| [Day 05](phase1/day05/) | Control Flow — Conditionals | if/elif/else, ternary operator, match-case |
| [Day 06](phase1/day06/) | Control Flow — Loops | for, while, break, continue, range, enumerate |
| [Day 07](phase1/day07/) | Functions — Basics | def, parameters, return values, scope |
| [Day 08](phase1/day08/) | Functions — Advanced | *args, **kwargs, lambda, closures, decorators |
| [Day 09](phase1/day09/) | Lists & Tuples | CRUD operations, slicing, list comprehensions |
| [Day 10](phase1/day10/) | Dictionaries & Sets | dict methods, set operations, comprehensions |
| [Day 11](phase1/day11/) | File I/O | Reading/writing files, CSV, JSON, context managers |
| [Day 12](phase1/day12/) | Error Handling | try/except/finally, custom exceptions, logging |
| [Day 13](phase1/day13/) | Modules & Packages | import system, creating packages, pip, virtual envs |
| [Day 14](phase1/day14/) | Object-Oriented Programming — Basics | Classes, objects, __init__, self, attributes |
| [Day 15](phase1/day15/) | OOP — Inheritance & Polymorphism | Inheritance, super(), method overriding, abstract classes |
| [Day 16](phase1/day16/) | OOP — Advanced | Dunder methods, properties, dataclasses, slots |
| [Day 17](phase1/day17/) | Iterators & Generators | __iter__, __next__, yield, generator expressions |
| [Day 18](phase1/day18/) | Regular Expressions | re module, patterns, groups, substitution |
| [Day 19](phase1/day19/) | Testing & Debugging | unittest, pytest, debugging techniques, pdb |
| [Day 20](phase1/day20/) | 🏗️ **Mini-Project: CLI Task Manager** | Build a command-line task management application |

---

## Phase 2: Data Science Foundations (Days 21–40)

> **Goal:** Master the core data science toolkit in Python.

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| [Day 21](phase2/day21/) | NumPy — Arrays & Operations | ndarray, shape, dtype, vectorized operations |
| [Day 22](phase2/day22/) | NumPy — Indexing & Broadcasting | Fancy indexing, boolean masks, broadcasting rules |
| [Day 23](phase2/day23/) | NumPy — Linear Algebra & Statistics | dot product, matrix operations, statistical functions |
| [Day 24](phase2/day24/) | Pandas — Series & DataFrames | Creating, indexing, selecting data, dtypes |
| [Day 25](phase2/day25/) | Pandas — Data Loading & Inspection | read_csv, read_excel, read_json, info(), describe() |
| [Day 26](phase2/day26/) | Pandas — Data Cleaning | Missing values, duplicates, type conversion, string ops |
| [Day 27](phase2/day27/) | Pandas — Data Transformation | apply, map, replace, rename, assign |
| [Day 28](phase2/day28/) | Pandas — Grouping & Aggregation | groupby, agg, transform, pivot_table, crosstab |
| [Day 29](phase2/day29/) | Pandas — Merging & Joining | merge, join, concat, append strategies |
| [Day 30](phase2/day30/) | Pandas — Time Series | DatetimeIndex, resample, rolling windows, shifts |
| [Day 31](phase2/day31/) | Matplotlib — Fundamentals | Figure, Axes, plot types, customization |
| [Day 32](phase2/day32/) | Matplotlib — Advanced Visualizations | Subplots, annotations, styles, 3D plots |
| [Day 33](phase2/day33/) | Seaborn — Statistical Visualization | Distribution, categorical, regression, heatmaps |
| [Day 34](phase2/day34/) | Plotly — Interactive Visualizations | Interactive charts, dashboards, plotly express |
| [Day 35](phase2/day35/) | Statistics — Descriptive Statistics | Mean, median, mode, variance, distributions |
| [Day 36](phase2/day36/) | Statistics — Probability & Distributions | Probability theory, normal/binomial/Poisson distributions |
| [Day 37](phase2/day37/) | Statistics — Hypothesis Testing | t-tests, chi-square, p-values, confidence intervals |
| [Day 38](phase2/day38/) | Statistics — Correlation & Regression Basics | Pearson, Spearman, simple linear regression |
| [Day 39](phase2/day39/) | Exploratory Data Analysis (EDA) | Complete EDA workflow, profiling, storytelling |
| [Day 40](phase2/day40/) | 🏗️ **Mini-Project: COVID/Sales Data Dashboard** | End-to-end EDA with visualizations and insights |

---

## Phase 3: Machine Learning & AI (Days 41–60)

> **Goal:** Build, evaluate, and deploy machine learning models.

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| [Day 41](phase3/day41/) | ML Fundamentals | ML types, bias-variance, train/test split, cross-validation |
| [Day 42](phase3/day42/) | Feature Engineering | Encoding, scaling, binning, feature creation |
| [Day 43](phase3/day43/) | Linear Regression | OLS, gradient descent, regularization (Ridge/Lasso) |
| [Day 44](phase3/day44/) | Logistic Regression | Binary/multiclass classification, sigmoid, decision boundary |
| [Day 45](phase3/day45/) | Decision Trees | Splitting criteria, pruning, feature importance |
| [Day 46](phase3/day46/) | Random Forests & Ensemble Methods | Bagging, boosting, Random Forest, AdaBoost |
| [Day 47](phase3/day47/) | Gradient Boosting | XGBoost, LightGBM, CatBoost, hyperparameter tuning |
| [Day 48](phase3/day48/) | Support Vector Machines | Kernels, margin, SVM for classification and regression |
| [Day 49](phase3/day49/) | K-Nearest Neighbors | Distance metrics, choosing K, curse of dimensionality |
| [Day 50](phase3/day50/) | Model Evaluation & Selection | Confusion matrix, ROC/AUC, precision/recall, F1, GridSearchCV |
| [Day 51](phase3/day51/) | Unsupervised Learning — Clustering | K-Means, DBSCAN, hierarchical clustering, silhouette score |
| [Day 52](phase3/day52/) | Dimensionality Reduction | PCA, t-SNE, UMAP, feature selection methods |
| [Day 53](phase3/day53/) | Natural Language Processing — Basics | Tokenization, stemming, lemmatization, bag of words, TF-IDF |
| [Day 54](phase3/day54/) | NLP — Text Classification | Sentiment analysis, Naive Bayes, text pipelines |
| [Day 55](phase3/day55/) | NLP — Word Embeddings | Word2Vec, GloVe, spaCy, working with embeddings |
| [Day 56](phase3/day56/) | Time Series Analysis | Trend, seasonality, ARIMA, SARIMA, Prophet |
| [Day 57](phase3/day57/) | Recommendation Systems | Collaborative filtering, content-based, hybrid approaches |
| [Day 58](phase3/day58/) | ML Pipelines & Deployment | scikit-learn pipelines, joblib, Flask/FastAPI serving |
| [Day 59](phase3/day59/) | MLflow & Experiment Tracking | Experiment logging, model registry, reproducibility |
| [Day 60](phase3/day60/) | 🏗️ **Mini-Project: End-to-End ML Pipeline** | Complete ML project from data to deployed API |

---

## Phase 4: Deep Learning & Advanced AI (Days 61–75)

> **Goal:** Understand and build deep learning models and work with modern AI.

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| [Day 61](phase4/day61/) | Neural Network Fundamentals | Perceptrons, activation functions, backpropagation |
| [Day 62](phase4/day62/) | TensorFlow & Keras — Getting Started | Tensors, Sequential API, compiling, training |
| [Day 63](phase4/day63/) | PyTorch — Getting Started | Tensors, autograd, nn.Module, training loop |
| [Day 64](phase4/day64/) | Building Deep Neural Networks | Hidden layers, dropout, batch normalization |
| [Day 65](phase4/day65/) | Convolutional Neural Networks (CNNs) | Convolution, pooling, architectures (LeNet, VGG, ResNet) |
| [Day 66](phase4/day66/) | CNN — Image Classification Project | Transfer learning, data augmentation, fine-tuning |
| [Day 67](phase4/day67/) | Recurrent Neural Networks (RNNs) | Vanilla RNN, LSTM, GRU, sequence modeling |
| [Day 68](phase4/day68/) | Attention & Transformers | Self-attention, multi-head attention, positional encoding |
| [Day 69](phase4/day69/) | Hugging Face Transformers | Pre-trained models, pipelines, tokenizers, fine-tuning |
| [Day 70](phase4/day70/) | Large Language Models (LLMs) | GPT architecture, prompt engineering, few-shot learning |
| [Day 71](phase4/day71/) | LLM APIs & LangChain | OpenAI API, LangChain chains, agents, RAG basics |
| [Day 72](phase4/day72/) | Generative AI — Image Generation | Diffusion models, Stable Diffusion, DALL-E concepts |
| [Day 73](phase4/day73/) | Model Optimization | Quantization, pruning, ONNX, TensorRT |
| [Day 74](phase4/day74/) | Responsible AI & Ethics | Bias, fairness, explainability (SHAP/LIME), AI safety |
| [Day 75](phase4/day75/) | 🏗️ **Mini-Project: AI-Powered App** | Build an app using LLMs/deep learning (chatbot, classifier, etc.) |

---

## Phase 5: Data Engineering (Days 76–90)

> **Goal:** Build robust data pipelines and work with big data tools.

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| [Day 76](phase5/day76/) | SQL Fundamentals | SELECT, WHERE, JOIN, GROUP BY, subqueries |
| [Day 77](phase5/day77/) | Advanced SQL | Window functions, CTEs, query optimization, indexing |
| [Day 78](phase5/day78/) | Python & Databases | SQLAlchemy, psycopg2, ORM patterns, connection pooling |
| [Day 79](phase5/day79/) | NoSQL Databases | MongoDB (pymongo), Redis, document vs. key-value stores |
| [Day 80](phase5/day80/) | ETL Fundamentals | Extract, Transform, Load patterns, data quality |
| [Day 81](phase5/day81/) | Apache Airflow — Basics | DAGs, operators, scheduling, task dependencies |
| [Day 82](phase5/day82/) | Apache Airflow — Advanced | XComs, sensors, hooks, dynamic DAGs, best practices |
| [Day 83](phase5/day83/) | Apache Spark — Basics | RDDs, DataFrames, SparkSQL, PySpark setup |
| [Day 84](phase5/day84/) | Apache Spark — Advanced | Spark ML, streaming, partitioning, optimization |
| [Day 85](phase5/day85/) | Data Warehousing Concepts | Star schema, slowly changing dimensions, OLAP vs. OLTP |
| [Day 86](phase5/day86/) | Cloud Data Platforms | AWS (S3, Redshift, Glue), GCP (BigQuery), Azure basics |
| [Day 87](phase5/day87/) | Docker for Data Projects | Dockerfiles, containers, docker-compose, reproducibility |
| [Day 88](phase5/day88/) | Data Quality & Governance | Great Expectations, data contracts, lineage, cataloging |
| [Day 89](phase5/day89/) | CI/CD for Data Pipelines | GitHub Actions, testing pipelines, dbt basics |
| [Day 90](phase5/day90/) | 🏗️ **Capstone Project: Full Data Platform** | End-to-end: ingest → transform → store → analyze → visualize |

---

## 📊 Progress Tracker

### Phase 1: Python Fundamentals
- [ ] Day 01 — Python Setup & Hello World
- [ ] Day 02 — Variables & Data Types
- [ ] Day 03 — Strings Deep Dive
- [ ] Day 04 — Operators & Expressions
- [ ] Day 05 — Control Flow — Conditionals
- [ ] Day 06 — Control Flow — Loops
- [ ] Day 07 — Functions — Basics
- [ ] Day 08 — Functions — Advanced
- [ ] Day 09 — Lists & Tuples
- [ ] Day 10 — Dictionaries & Sets
- [ ] Day 11 — File I/O
- [ ] Day 12 — Error Handling
- [ ] Day 13 — Modules & Packages
- [ ] Day 14 — OOP — Basics
- [ ] Day 15 — OOP — Inheritance & Polymorphism
- [ ] Day 16 — OOP — Advanced
- [ ] Day 17 — Iterators & Generators
- [ ] Day 18 — Regular Expressions
- [ ] Day 19 — Testing & Debugging
- [ ] Day 20 — Mini-Project: CLI Task Manager

### Phase 2: Data Science Foundations
- [ ] Day 21 — NumPy — Arrays & Operations
- [ ] Day 22 — NumPy — Indexing & Broadcasting
- [ ] Day 23 — NumPy — Linear Algebra & Statistics
- [ ] Day 24 — Pandas — Series & DataFrames
- [ ] Day 25 — Pandas — Data Loading & Inspection
- [ ] Day 26 — Pandas — Data Cleaning
- [ ] Day 27 — Pandas — Data Transformation
- [ ] Day 28 — Pandas — Grouping & Aggregation
- [ ] Day 29 — Pandas — Merging & Joining
- [ ] Day 30 — Pandas — Time Series
- [ ] Day 31 — Matplotlib — Fundamentals
- [ ] Day 32 — Matplotlib — Advanced Visualizations
- [ ] Day 33 — Seaborn — Statistical Visualization
- [ ] Day 34 — Plotly — Interactive Visualizations
- [ ] Day 35 — Statistics — Descriptive Statistics
- [ ] Day 36 — Statistics — Probability & Distributions
- [ ] Day 37 — Statistics — Hypothesis Testing
- [ ] Day 38 — Statistics — Correlation & Regression Basics
- [ ] Day 39 — Exploratory Data Analysis (EDA)
- [ ] Day 40 — Mini-Project: Data Dashboard

### Phase 3: Machine Learning & AI
- [ ] Day 41 — ML Fundamentals
- [ ] Day 42 — Feature Engineering
- [ ] Day 43 — Linear Regression
- [ ] Day 44 — Logistic Regression
- [ ] Day 45 — Decision Trees
- [ ] Day 46 — Random Forests & Ensemble Methods
- [ ] Day 47 — Gradient Boosting
- [ ] Day 48 — Support Vector Machines
- [ ] Day 49 — K-Nearest Neighbors
- [ ] Day 50 — Model Evaluation & Selection
- [ ] Day 51 — Unsupervised Learning — Clustering
- [ ] Day 52 — Dimensionality Reduction
- [ ] Day 53 — NLP — Basics
- [ ] Day 54 — NLP — Text Classification
- [ ] Day 55 — NLP — Word Embeddings
- [ ] Day 56 — Time Series Analysis
- [ ] Day 57 — Recommendation Systems
- [ ] Day 58 — ML Pipelines & Deployment
- [ ] Day 59 — MLflow & Experiment Tracking
- [ ] Day 60 — Mini-Project: End-to-End ML Pipeline

### Phase 4: Deep Learning & Advanced AI
- [ ] Day 61 — Neural Network Fundamentals
- [ ] Day 62 — TensorFlow & Keras
- [ ] Day 63 — PyTorch
- [ ] Day 64 — Building Deep Neural Networks
- [ ] Day 65 — CNNs
- [ ] Day 66 — CNN Image Classification Project
- [ ] Day 67 — RNNs
- [ ] Day 68 — Attention & Transformers
- [ ] Day 69 — Hugging Face Transformers
- [ ] Day 70 — Large Language Models
- [ ] Day 71 — LLM APIs & LangChain
- [ ] Day 72 — Generative AI
- [ ] Day 73 — Model Optimization
- [ ] Day 74 — Responsible AI & Ethics
- [ ] Day 75 — Mini-Project: AI-Powered App

### Phase 5: Data Engineering
- [ ] Day 76 — SQL Fundamentals
- [ ] Day 77 — Advanced SQL
- [ ] Day 78 — Python & Databases
- [ ] Day 79 — NoSQL Databases
- [ ] Day 80 — ETL Fundamentals
- [ ] Day 81 — Apache Airflow — Basics
- [ ] Day 82 — Apache Airflow — Advanced
- [ ] Day 83 — Apache Spark — Basics
- [ ] Day 84 — Apache Spark — Advanced
- [ ] Day 85 — Data Warehousing Concepts
- [ ] Day 86 — Cloud Data Platforms
- [ ] Day 87 — Docker for Data Projects
- [ ] Day 88 — Data Quality & Governance
- [ ] Day 89 — CI/CD for Data Pipelines
- [ ] Day 90 — Capstone Project

---

## Resources

### Books
- *Python Crash Course* by Eric Matthes
- *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* by Aurélien Géron
- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Python for Data Analysis* by Wes McKinney

### Online Platforms
- [Kaggle](https://www.kaggle.com/) — Datasets and competitions
- [LeetCode](https://leetcode.com/) — Coding practice
- [Real Python](https://realpython.com/) — Tutorials
- [fast.ai](https://www.fast.ai/) — Deep learning courses

### Documentation
- [Python Official Docs](https://docs.python.org/3/)
- [NumPy Docs](https://numpy.org/doc/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Scikit-learn Docs](https://scikit-learn.org/stable/)
- [TensorFlow Docs](https://www.tensorflow.org/api_docs)
- [PyTorch Docs](https://pytorch.org/docs/)

---

## Contributing

Contributions are welcome! If you find errors or want to improve the content:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Learning! 🚀 Remember: Consistency beats intensity. Show up every day!**
