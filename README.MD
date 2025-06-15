
# 🚀 Projeto Docker-ETL: Pipeline de Dados com Spark, Airflow e Grafana

Este projeto implementa um pipeline de dados completo usando:

- ⚙️ **Spark** para processamento ETL
- 🎯 **Airflow** para orquestração
- 🗄️ **PostgreSQL** como banco de dados
- 📊 **Grafana** e **Metabase** para visualização
- 📈 **Prometheus** para monitoramento

Tudo containerizado com **Docker** para fácil reprodução e escalabilidade.

---

## 📋 Pré-requisitos

- Docker Engine **20+**
- Docker Compose **2.10+**
- **4GB+** de RAM disponível

---

## 🚀 Instalação

Clone o repositório:

```bash
git clone [URL_DO_SEU_REPO]
cd Docker-ETL
```

Inicie os containers:

```bash
docker-compose up -d --build
```

Acesse as ferramentas:

- **Airflow:** [http://localhost:8080](http://localhost:8080) — *Login:* `admin` / *Senha:* `admin`
- **Grafana:** [http://localhost:3001](http://localhost:3001) — *Login:* `admin` / *Senha:* `admin`
- **Metabase:** [http://localhost:3000](http://localhost:3000) — *(configurar no primeiro acesso)*
- **Prometheus:** [http://localhost:9090](http://localhost:9090)

---

## 🛠️ Estrutura do Projeto

```
Docker-ETL/
├── data/               # Dados de entrada/saída
│   ├── input/          # CSVs/JSONs de origem
│   └── output/         # Dados processados (Parquet)
├── airflow/            # DAGs e configurações
├── grafana/            # Dashboards e datasources
├── scripts/            # Códigos Spark
├── docker-compose.yml  # Orquestração dos serviços
└── Dockerfile          # Imagem customizada do Spark
```

---

## 🔄 Fluxo de Dados

- **Extração:**
  - Spark lê os arquivos `data/input/vendas_2023.csv` e `produtos.json`.

- **Transformação:**
  - Limpeza, joins e agregações realizadas (ver arquivo `scripts/etl_spark.py`).

- **Carga:**
  - Grava os dados em:
    - Banco **PostgreSQL** (tabela `vendas`)
    - Arquivos **Parquet** em `data/output/`

- **Visualização:**
  - Dashboards no **Grafana** e **Metabase**.

---

## ⚙️ Configuração Avançada

### 🔧 Variáveis de Ambiente

Edite o arquivo `docker-compose.yml` para ajustar:

```yaml
environment:
  POSTGRES_PASSWORD: senha123       # 🔒 Altere para produção!
  AIRFLOW__CORE__FERNET_KEY: sua_chave_aqui
```

### ➕ Adicionar Novas DAGs

Coloque seus workflows no diretório:

```
airflow/dags/
```

### 📈 Monitoramento Customizado

Edite o arquivo `prometheus.yml` para adicionar novas métricas ou targets.

---

## 🛑 Comandos Úteis

| Função               | Comando                                        |
|----------------------|------------------------------------------------|
| Reiniciar serviços   | `docker-compose restart`                      |
| Ver logs             | `docker-compose logs -f [serviço]`            |
| Parar tudo           | `docker-compose down`                         |
| Limpar dados         | `docker-compose down -v`                      |

---

## 📊 Dashboards Recomendados

### 🔹 **Grafana**

- **Spark:** ID `10258`
- **PostgreSQL:** ID `9628`

### 🔸 **Metabase**

Crie questões SQL como:

```sql
SELECT * 
FROM vendas 
WHERE data > NOW() - INTERVAL '7 days';
```

---

## ⁉️ Solução de Problemas

### ⚠️ Erro no Spark

```bash
docker-compose exec spark-etl tail -n 50 /opt/spark/logs/spark.log
```

### ⚠️ Airflow não inicia

```bash
docker-compose exec airflow airflow db check
```

### ⚠️ Grafana sem dados

Verifique se o datasource **Prometheus** está configurado corretamente:

```
URL: http://prometheus:9090
```

---

## 📄 Licença

📝 MIT License — Use livremente para projetos pessoais e comerciais.

Contribuições são bem-vindas!  
👉 Envie PRs ou abra issues no GitHub.

---

## 🔗 Links Úteis

- [Documentação Spark](https://spark.apache.org/docs/latest/)
- [Guia Airflow](https://airflow.apache.org/docs/)

---

**Happy Coding! 🚀**
