![Banner com o texto Machine Learning Engineer, Sistemas de IA reproduzíveis e inspecionáveis, MLOps, RAG e Computer Vision](assets/profile-hero.png)

# Fabio Figueiredo

**Machine Learning Engineer · AI Engineer · Cientista de Dados Sênior**

Eu gosto de projetos em que outra pessoa consegue abrir o repositório e entender o que foi
executado, como foi medido e onde estão os limites.

Meu foco hoje está na parte que conecta modelagem e software: MLOps, RAG e visão computacional.

[Portfólio](https://fabiofigueiredo.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/fabio-ffigueiredo-datascience/) · [E-mail](mailto:fabio.f.figueiredo@gmail.com)

## Projetos que mostram como eu trabalho

### VisionOps Realtime: detecção e tracking em movimento

[![Trecho de uma rodovia com veículos detectados pelo YOLO11n e quatro IDs temporais mantidos pelo ByteTrack](assets/visionops-tracking.gif)](https://github.com/fabioffigueiredo/visionops-realtime)

Neste recorte, o YOLO11n detecta veículos e o ByteTrack associa quatro deles ao longo dos frames.
As outras caixas permanecem como detecções do frame. Limitei os IDs para não esconder a estrada.

É uma demonstração local sobre vídeo licenciado. Não mede acurácia, throughput de vídeo ou
capacidade de uma estrada em produção.

[Ver código, testes e limites](https://github.com/fabioffigueiredo/visionops-realtime)

### PRISMA: uma resposta que deixa rastro

[![Interface do PRISMA em modo Demo com uma resposta sobre dados fictícios, gráfico de atribuição e aviso de escopo](assets/prisma-auditable-rag.png)](https://github.com/fabioffigueiredo/FinRAG_Prisma/tree/e1b8cf5ed865)

Uma pergunta entra. A resposta volta com fontes. No modo Demo determinístico, o fluxo registra as
fontes recuperadas, o motor usado, a latência e um hash da consulta.

É uma prova de conceito pública com dados fictícios. Não é produto em produção nem recomendação
financeira.

[Ver o commit usado na demonstração](https://github.com/fabioffigueiredo/FinRAG_Prisma/tree/e1b8cf5ed865)

### MLOps: um gate que não inventa evidência

[![Painel real do experimento MLOps com o gate de promoção bloqueado e cinco evidências marcadas como ausentes](assets/mlops-promotion-gate.png)](https://github.com/fabioffigueiredo/pd_operacionalizao_modelos_mlops/tree/1ada3456dd7c905498505adb619d1632bc169d46)

A função desta interface é responder se existe evidência suficiente para promover um modelo. Ela
lê `reports/metrics_extended.csv` por um contrato tipado, apresenta as métricas registradas e
mantém o gate bloqueado quando a evidência não sustenta uma decisão.

No snapshot versionado, RF com PCA versus o baseline resulta em **Recall +0,0559**,
**Precision -0,0298**, **FP +405** e **FN -112**. O ganho de recall encontra mais positivos, mas
vem acompanhado de mais falsos positivos. Sem custo e threshold, esse trade-off não define uma
promoção.

O gate está **bloqueado** porque faltam cinco evidências: custo de falso positivo, custo de falso
negativo, threshold escolhido, validação temporal e plano de monitoramento.

Por baixo da função, a arquitetura conecta CSV versionado, validação de schema, gráficos em
Streamlit e runs rastreadas no MLflow. O projeto é acadêmico: não aprova ou recusa crédito e não
foi validado para produção.

[Ver o código e as evidências no commit usado](https://github.com/fabioffigueiredo/pd_operacionalizao_modelos_mlops/tree/1ada3456dd7c905498505adb619d1632bc169d46)

## Projeto complementar

### FinNLP: do endpoint à resposta

Um cenário fictício percorre `POST /api/analyze`, `PipelineService` e uma resposta JSON com
sentimento, entidades, tópico e textos similares. A interface mostra o caminho executado sem
tratar a demonstração como produto financeiro.

[Ver o FinNLP](https://github.com/fabioffigueiredo/finnlp_performance_attribution/tree/a145e0f)

## Como eu construo

- **Código executável:** a interface precisa apontar para um caminho que outra pessoa consiga revisar.
- **Métrica com protocolo:** um número público precisa informar ambiente, método e o que ele não mede.
- **Limite visível:** experimento, demonstração e produção não são tratados como a mesma coisa.

## Direção técnica

Python · FastAPI · scikit-learn · MLflow · RAG/LLM evaluation · Computer Vision · MLOps · testes · governança de dados

## Formação

Pós-graduação em Inteligência Artificial, Machine Learning e Deep Learning pelo Instituto Infnet,
concluída em 2026.

## Contato

[Portfólio](https://fabiofigueiredo.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/fabio-ffigueiredo-datascience/) · [E-mail](mailto:fabio.f.figueiredo@gmail.com)
