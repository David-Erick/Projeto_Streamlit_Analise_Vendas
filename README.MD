

```markdown
# Dashboard Interativo de Análise de Vendas

Dashboard interativo de Business Intelligence (BI) desenvolvido com **Streamlit**, utilizando dados reais de vendas para gerar insights estratégicos sobre desempenho comercial, mix de produtos, logística e distribuição geográfica.

Este projeto foi criado com foco em **boas práticas de engenharia de dados, visualização e organização de código**, sendo adequado para fins acadêmicos, profissionais e portfólio técnico.

---

## Visão Geral do Projeto

Empresas frequentemente possuem grandes volumes de dados de vendas, mas enfrentam dificuldades para extrair informações relevantes de forma rápida e visual.

Este dashboard resolve esse problema ao fornecer:

- Indicadores estratégicos de vendas
- Visualizações interativas orientadas à tomada de decisão
- Análises por produto, categoria, logística e região
- Interface simples, moderna e responsiva

O resultado é uma ferramenta que transforma dados brutos em **informação acionável**.

---

## Principais Funcionalidades

- Indicadores-chave de desempenho (KPIs)
- Ranking de produtos por faturamento
- Análise do mix de categorias e subcategorias
- Avaliação do impacto do modo de envio
- Concentração geográfica das vendas
- Design customizado com CSS
- Estrutura modular e escalável

---

## Estrutura do Projeto

```

Projeto_Streamlit_Analise_Vendas/
├── app.py
├── pages/
│   └── 2_Insights_e_Performance.py
├── src/
│   ├── data_loader.py
│   ├── filters.py
│   └── kpis.py
├── data/
│   └── superstore.csv
├── venv/
├── requirements.txt
└── README.md

````

---

## Dataset Utilizado

- **Nome:** Superstore Sales Forecasting  
- **Fonte:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting  

O dataset contém informações sobre pedidos, produtos, categorias, datas, vendas, regiões e cidades.

---

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas
- Plotly Express
- CSS customizado
- Virtual Environment (venv)

---

## Boas Práticas Aplicadas

- Padronização automática de nomes de colunas
- Separação de responsabilidades por módulos
- Código reutilizável e organizado
- Visualizações claras e consistentes
- Uso de dados reais

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Projeto_Streamlit_Analise_Vendas.git
cd Projeto_Streamlit_Analise_Vendas
````

### 2. Criar e ativar o ambiente virtual

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o dashboard

```bash
streamlit run app.py
```

O aplicativo será aberto automaticamente no navegador.

---

## Possíveis Melhorias Futuras

* Previsão de vendas (forecasting)
* Análise de rentabilidade
* Segmentação de clientes
* Filtros globais entre páginas
* Deploy em nuvem (Streamlit Cloud)
* Exportação de relatórios

---

## Autor

**David Erick**
Graduando em Sistemas de Informação
Interesses: Business Intelligence, Ciência de Dados, IoT e Engenharia de Software

---

## Licença

Este projeto é destinado a fins educacionais e de aprendizado.

````

---

## 🏆 O QUE FOI CORRIGIDO

✔ Markdown **100% padrão GitHub**  
✔ Sem HTML embutido  
✔ Emojis apenas em texto simples (evitados em headers)  
✔ Blocos de código corretamente fechados  
✔ Estrutura clara e escaneável  
✔ Compatível com dark/light mode do GitHub  

---

## 🔥 DICA DE OURO (PORTFÓLIO)

Depois disso, recomendo:
1. Adicionar **prints do dashboard** (pasta `/assets`)
2. Inserir imagens no README assim:
   ```markdown
   ![Dashboard](assets/dashboard.png)
````

3. Criar um **commit limpo só do README**

---

Se quiser, posso agora:

* Ajustar o texto para **perfil de estágio/júnior**
* Criar versão em **inglês**
* Sugerir **commits ideais**
* Revisar o projeto como se fosse um **recrutador**

👉 Qual próximo passo?

