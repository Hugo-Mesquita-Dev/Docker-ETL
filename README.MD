Pipeline de Dados com Docker, Spark e Airflow
https://img.shields.io/badge/license-MIT-blue.svg
https://img.shields.io/badge/Docker-%E2%89%A520.10.8-blue
https://img.shields.io/badge/Spark-3.5.0-red

Pipeline ETL completo para processamento de dados, com:
✅ Extração, Transformação e Carga (Spark)
✅ Orquestração (Airflow)
✅ Armazenamento (PostgreSQL)
✅ Visualização (Grafana + Metabase)
✅ Monitoramento (Prometheus)

🚀 Começando
Pré-requisitos
Docker 20+

Docker Compose 2.10+

4GB+ RAM disponível

bash
git clone https://github.com/seu-usuario/docker-etl-pipeline.git
cd docker-etl-pipeline
🛠️ Configuração
Estrutura de Arquivos:

text
.
├── data/
│   ├── input/          # Dados brutos (CSV/JSON)
│   └── output/         # Dados processados (Parquet)
├── airflow/
│   ├── dags/           # Pipelines do Airflow
│   └── plugins/        # Plugins customizados
├── grafana/
│   └── provisioning/   # Dashboards e fontes de dados
├── scripts/
│   └── etl_spark.py    # Código principal do ETL
├── docker-compose.yml  # Definição dos serviços
└── Dockerfile          # Imagem customizada do Spark
Inicie os containers:

bash
docker-compose up -d --build
🌐 Acesse as Ferramentas
Serviço	URL	Credenciais
Airflow	http://localhost:8080	admin/admin
Grafana	http://localhost:3001	admin/admin
Metabase	http://localhost:3000	Configurar 1º acesso
Prometheus	http://localhost:9090	-
🔄 Fluxo de Dados
Spark ETL processa dados de data/input/:

python
# scripts/etl_spark.py
df_vendas = spark.read.csv("/app/data/input/vendas.csv")
df_vendas.write.jdbc(url=DB_URL, table="vendas")
Airflow agenda execuções diárias:

python
# airflow/dags/spark_etl_dag.py
with DAG('etl_daily', schedule_interval='@daily'):
    run_spark = DockerOperator(task_id='run_spark_etl')
Grafana visualiza os dados:

sql
SELECT categoria, SUM(valor) FROM vendas GROUP BY 1
🛑 Comandos Úteis
Função	Comando
Reiniciar serviços	docker-compose restart
Ver logs	docker-compose logs -f
Parar tudo	docker-compose down
Limpar dados	docker-compose down -v
Executar ETL manual	docker-compose run spark-etl
📊 Dashboards Recomendados
Grafana:

Importe via ID:

10258 (Spark Monitoring)

9628 (PostgreSQL)

Metabase:

Crie questões SQL com:

sql
SELECT * FROM vendas WHERE data > NOW() - INTERVAL '7 days'
⁉️ Solução de Problemas
Erro comum: "Tabela vendas não existe"
bash
# Execute o ETL manualmente
docker-compose run spark-etl

# Verifique no PostgreSQL
docker-compose exec postgres psql -U postgres -d vendas_db -c "\dt"
Spark não inicia
bash
docker-compose logs spark-etl | grep ERROR
📄 Licença
MIT License - Consulte o arquivo LICENSE para detalhes.

Contribuições são bem-vindas!
🔧 Reporte issues ou envie PRs.

✨ Dica: Após o primeiro setup, acesse http://localhost:8080 para configurar as DAGs no Airflow!