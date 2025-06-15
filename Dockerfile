FROM apache/spark:3.5.0

# Configurações de ambiente
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV IVY2_HOME=/tmp/.ivy2
ENV _JAVA_OPTIONS=-Duser.home=/tmp

# Configuração como root
USER root

# 1. Cria estrutura de diretórios
RUN mkdir -p /app/data/output && \
    mkdir -p $IVY2_HOME && \
    chmod -R 777 /app && \
    chmod -R 777 $IVY2_HOME

# 2. Instala o driver JDBC do PostgreSQL
RUN mkdir -p /opt/spark/jars && \
    curl -o /tmp/postgresql-42.6.0.jar \
    https://jdbc.postgresql.org/download/postgresql-42.6.0.jar && \
    mv /tmp/postgresql-42.6.0.jar /opt/spark/jars/ && \
    chmod 644 /opt/spark/jars/postgresql-42.6.0.jar

# 3. Configuração do workspace
WORKDIR /app

# 4. Cópia dos arquivos (como usuário spark)
USER 1000
COPY --chown=1000:1000 scripts ./scripts
COPY --chown=1000:1000 data/input ./data/input