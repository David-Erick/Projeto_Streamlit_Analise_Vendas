

```markdown
# 📊 Dashboard Interativo de Análise de Vendas com Streamlit

## 🔎 Visão Geral e Valor do Projeto

Este projeto consiste em um **dashboard interativo de Business Intelligence (BI)** desenvolvido com **Streamlit**, voltado para **análise estratégica de vendas** a partir de dados reais do dataset *Superstore Sales Forecasting* (Kaggle).

O objetivo principal é **transformar dados brutos em insights acionáveis**, permitindo a visualização clara de:
- desempenho de vendas,
- mix de produtos,
- impacto logístico,
- concentração geográfica,
- comportamento por categoria e subcategoria.

O dashboard foi projetado seguindo **boas práticas de engenharia de dados, visualização e UX**, sendo adequado tanto para **análises acadêmicas** quanto para **uso corporativo** e **portfólio profissional**.

---

## 🎯 Problema que o Projeto Resolve

Empresas frequentemente possuem grandes volumes de dados de vendas, mas enfrentam dificuldades para:
- interpretar rapidamente o desempenho do negócio,
- identificar produtos e regiões estratégicas,
- avaliar impacto logístico nas vendas,
- comunicar resultados de forma clara para tomada de decisão.

Este projeto resolve esse problema ao fornecer uma **interface visual, intuitiva e interativa**, eliminando a dependência de análises manuais ou relatórios estáticos.

---

## 🧠 Principais Funcionalidades

- 📈 KPIs estratégicos (faturamento, produtos distintos, cidades atendidas)
- 🏆 Ranking dos produtos com maior faturamento
- 📦 Análise do mix de categorias e subcategorias
- 🚚 Avaliação do impacto do modo de envio
- 🏙️ Análise da concentração geográfica das vendas
- 🎨 Design moderno com CSS customizado
- 🔄 Estrutura modular e escalável

---

## 🗂️ Estrutura do Projeto

```

Projeto_Streamlit_Analise_Vendas/
│
├── app.py                         # Página principal do dashboard
├── pages/
│   └── 2_🧠_Insights_e_Performance.py
│
├── src/
│   ├── data_loader.py             # Carregamento e padronização dos dados
│   ├── filters.py                 # Filtros globais do dashboard
│   └── kpis.py                    # Cálculo de indicadores
│
├── data/
│   └── superstore.csv             # Dataset de vendas (Kaggle)
│
├── venv/                          # Ambiente virtual Python
│
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação

````

---

## 📊 Dataset Utilizado

- **Nome:** Superstore Sales Forecasting  
- **Fonte:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting  

O dataset contém informações sobre:
- pedidos,
- datas de compra e envio,
- categorias e subcategorias,
- produtos,
- vendas,
- regiões e cidades.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **Streamlit** – interface e interatividade
- **Pandas** – manipulação e análise de dados
- **Plotly Express** – visualizações interativas
- **CSS customizado** – design moderno
- **Virtual Environment (venv)** – isolamento de dependências

---

## 🧪 Boas Práticas Implementadas

- Padronização automática dos nomes das colunas
- Separação de responsabilidades (data loader, filtros, KPIs)
- Código modular e reutilizável
- Visualizações claras e orientadas a decisão
- Design focado em UX e leitura executiva
- Uso de dados reais

---

## 🚀 Como Executar o Projeto Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Projeto_Streamlit_Analise_Vendas.git
cd Projeto_Streamlit_Analise_Vendas
````

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o dashboard

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no navegador.

---

## 📌 Possíveis Extensões Futuras

* 🔮 Forecast de vendas (Prophet / ARIMA)
* 📊 Análise de rentabilidade
* 🎯 Segmentação de clientes
* 🧩 Filtros globais entre páginas
* ☁️ Deploy no Streamlit Cloud
* 📱 Responsividade avançada
* 📄 Exportação de relatórios

---

## 👨‍💻 Autor

**David Erick**
Graduando em Sistemas de Informação
Interesses: Gestão de Projetos/Produtos, Ciência de Dados, Business Intelligence, IoT, Analytics e Engenharia de Software, 

---
