# 🚀 Docker-ETL Pipeline

![Docker](https://img.shields.io/badge/Docker-≥20.10.8-blue)
![Spark](https://img.shields.io/badge/Spark-3.5.0-red)
![Airflow](https://img.shields.io/badge/Airflow-2.5.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Pipeline de dados completo para processamento ETL com orquestração e monitoramento.

## 📦 Componentes

| Serviço       | Versão   | Função                          |
|---------------|----------|---------------------------------|
| Apache Spark  | 3.5.0    | Processamento distribuído       |
| Apache Airflow| 2.5.0    | Orquestração de pipelines       |
| PostgreSQL    | 13       | Armazenamento de dados          |
| Grafana       | Latest   | Visualização e dashboards       |
| Prometheus    | Latest   | Monitoramento                   |

## 🛠️ Configuração

### Pré-requisitos
- Docker 20+
- Docker Compose 2.10+
- 4GB+ de RAM

```bash
git clone https://github.com/Hugo-Mesquita-Dev/Docker-ETL.git
cd Docker-ETL
docker-compose up -d --build

🌐 Acessos
Serviço	URL	Credenciais
Airflow	http://localhost:8080	admin/admin
Grafana	http://localhost:3001	admin/admin
Metabase	http://localhost:3000	Configurar 1º uso
PostgreSQL	localhost:5432	postgres/senha123

🗂 Estrutura do Projeto
Docker-ETL/
├── data/
│   ├── input/          # Dados brutos (CSV/JSON)
│   └── output/         # Dados processados (Parquet)
├── airflow/
│   ├── dags/           # Pipelines do Airflow
│   └── plugins/        # Plugins customizados
├── grafana/
│   └── provisioning/   # Dashboards e datasources
├── scripts/
│   └── etl_spark.py    # Código principal do ETL
├── docker-compose.yml  # Definição dos serviços
└── Dockerfile          # Imagem customizada do Spark

🔄 Fluxo de Dados
Extração:

python
df = spark.read.csv("/app/data/input/vendas.csv")
Transformação:

python
df = df.withColumn("total", col("preco")*col("quantidade"))
Carga:

python
df.write.jdbc(url=DB_URL, table="vendas")

🛑 Comandos Úteis
Função	Comando
Reiniciar serviços	docker-compose restart
Ver logs	docker-compose logs -f
Parar tudo	docker-compose down
Limpar dados	docker-compose down -v

