# 🚀 Airflow ETL Pipeline

An end-to-end ETL pipeline built using Apache Airflow for orchestrating, scheduling, and monitoring data workflows.

---

## 📌 Project Overview

This project demonstrates how to automate ETL workflows using Apache Airflow.

The pipeline performs:

- Data Extraction
- Data Transformation
- Data Loading
- Workflow Automation
- Task Monitoring

---

## 🛠️ Tech Stack

- Python
- Apache Airflow
- Pandas
- Docker
- PostgreSQL
- SQL

---

## 📂 Project Structure

```bash
airflow_pipeline/
│
├── dags/                 # Airflow DAG definitions
├── scripts/              # ETL scripts
├── data/                 # Raw and processed datasets
├── logs/                 # Airflow logs
├── plugins/              # Custom plugins/operators
├── docker-compose.yml    # Docker services configuration
├── requirements.txt      # Python dependencies
└── README.md
```

---

## ⚙️ Pipeline Workflow

### 1️⃣ Extract
- Read data from multiple sources
- Validate source availability

### 2️⃣ Transform
- Clean missing values
- Remove duplicates
- Convert data types
- Apply business rules

### 3️⃣ Load
- Load transformed data into the target database
- Validate inserted records

### 4️⃣ Orchestration
- Schedule workflows using Airflow
- Retry failed tasks automatically
- Monitor execution from Airflow UI

---

## 🐳 Running the Project with Docker

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ahmedtarikalrefaay/airflow_pipeline.git
cd airflow_pipeline
```

### 2️⃣ Start Services

```bash
docker compose up -d
```

### 3️⃣ Open Airflow UI

```bash
http://localhost:8080
```

### Default Credentials

```bash
Username: airflow
Password: airflow
```

---

## ▶️ Running the DAG

1. Open Airflow UI
2. Enable the DAG
3. Trigger the pipeline
4. Monitor tasks from Graph View

---

## 📊 Features

- ✅ Automated ETL Pipeline
- ✅ Dockerized Environment
- ✅ Airflow DAG Scheduling
- ✅ Logging & Monitoring
- ✅ Retry & Failure Handling
- ✅ Modular Architecture

---

## 🔧 Future Improvements

- Kafka Integration
- Spark Processing
- Data Validation Layer
- Kubernetes Deployment
- CI/CD Integration

---

## 🤝 Contributing

Contributions are welcome.

### Steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Ahmed Tarik Alrefaay**

### GitHub
https://github.com/ahmedtarikalrefaay

### Repository
https://github.com/ahmedtarikalrefaay/airflow_pipeline
