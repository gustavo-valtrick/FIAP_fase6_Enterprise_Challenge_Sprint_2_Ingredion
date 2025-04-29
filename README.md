
# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## 🌾 Previsão de Produtividade Agrícola com NDVI via Plataforma SATVeg

### 👨‍🎓 Integrantes:
- Gustavo di Primio Valtrick de Almeida - RM559575  
- Iago Cotta Locatelli Guinatti - RM559655  
- Pedro Scofield da Cunha - RM560589  
- Rodrigo Mastropietro - RM560081  
- Tiago de Andrade Bastos - RM560467  

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 📜 Descrição

Este projeto tem como objetivo desenvolver um modelo de inteligência artificial capaz de prever a produtividade agrícola com base em séries temporais do índice de vegetação NDVI (Normalized Difference Vegetation Index), obtidas via a plataforma SATVeg da Embrapa.  

A pesquisa se concentrou na região de Mogi Mirim, no estado de São Paulo, devido à sua expressiva relevância agrícola e à boa disponibilidade de dados históricos. A abordagem envolveu:  
- Coleta de dados de NDVI e produtividade,
- Pré-processamento das séries temporais,
- Extração de componentes sazonais e tendências,
- Treinamento e avaliação de modelos de regressão baseados em Random Forest.

Foi utilizada uma filtragem de qualidade mínima de 0.8 para garantir confiabilidade nos dados de NDVI. A interpolação temporal e a decomposição dos dados permitiram extrair as variáveis mais informativas para o modelo.  

A análise estatística revelou uma forte correlação (0,91) entre o NDVI e a produtividade agrícola, especialmente nos meses de abril, julho, outubro, novembro e dezembro — considerados períodos críticos para a previsão. O modelo construído mostrou bom desempenho na validação, e as visualizações geradas facilitaram a compreensão das previsões em comparação aos valores reais.

O projeto é uma etapa do programa PBL (Project-Based Learning) e explora dados reais com aplicação prática no contexto de agricultura de precisão, sustentabilidade e uso de dados remotos.

---

## 📈 Informações da Etapa 2 (Extração e Análise de Variáveis-Chave)

- **Variáveis-chave selecionadas**:
  - NDVI diário médio (após filtragem de qualidade ≥ 0.8).
  - Produtividade agrícola diária.
  - Mês do ano (captura de efeitos sazonais).
  - Qualidade do pixel (assegura confiabilidade dos dados).

- **Processamento**:
  - Filtragem de NDVI por qualidade.
  - Cálculo da média espacial diária.
  - Interpolação para preencher lacunas.
  - Junção dos dados de NDVI e produtividade por data.

- **Análise de Correlação**:
  - Correlação global entre NDVI e produtividade: **0,91** (forte positiva).
  - **Meses críticos** com alta correlação positiva: abril (0,49), julho (0,46), outubro (0,41), novembro (0,57), dezembro (0,43).
  - **Meses de correlação negativa**: agosto (-0,99), setembro (-0,85) (associados a senescência ou colheita).

- **Segmentação de Áreas de Cultivo**:
  - Seleção de áreas específicas via pontos ou polígonos no SATVeg.
  - Cálculo da média de NDVI em polígonos.
  - Aplicação de filtros de qualidade para foco em regiões agrícolas.

**Conclusão**:  
O NDVI mostrou-se um preditor robusto da produtividade agrícola. A análise temporal, combinada à segmentação espacial, permite a construção de modelos de previsão mais precisos e a tomada de decisões agrícolas mais informadas.

---

## 📁 Estrutura de pastas

```plaintext
Sprint_2/
│
├── assets/                  # Imagens e elementos gráficos usados no projeto
│
├── document/                # Documentação do projeto
│   ├── Challenge_Ingredion–SPRINT_1.pdf
│   └── SPRINT 2 - ETAPA 2.pdf
│
├── src/                     # Código-fonte principal
│   ├── preprocessing.py
│   ├── modelo_IA.py
│   └── teste_modelo.py
│
├── data/
│   ├── raw/                 # Dados brutos (.csv da plataforma SATVeg e IEA)
│   └── processed/           # Dados tratados após pré-processamento
│
├── .idea/                   # Configurações do projeto (IDE PyCharm)
│
└── README.md                # Guia geral e explicações sobre o projeto
```

---

## 🔧 Como executar o código

### ✅ Pré-requisitos:
- Python 3.12
- IDE recomendada: PyCharm ou VS Code
- Instalar as seguintes bibliotecas:
  ```bash
  pip install pandas numpy matplotlib scikit-learn statsmodels
  ```

### ▶️ Execução por fases:

#### **Fase 1: Pré-processamento**
1. Certifique-se de que os arquivos `.csv` estejam na pasta `data/raw/`.
2. Execute o script de pré-processamento:
   ```bash
   python preprocessing.py --input_dir data/raw --output_dir data/processed
   ```

#### **Fase 2: Treinamento e Avaliação do Modelo**
3. Execute o script `modelo_IA.py` ou `teste_modelo.py`:
   ```bash
   python modelo_IA.py
   # ou
   python teste_modelo.py
   ```

#### **Fase 3 (opcional): Visualização dos resultados**
- `teste_modelo.py` gera gráficos comparando valores reais e previstos de produtividade.

---

## 🗃 Histórico de lançamentos

- 0.5.0 - 29/04/2025 ✨ Finalização do modelo e relatório Sprint 2  
- 0.4.0 - 20/04/2025 🧪 Avaliação e validação de modelo  
- 0.3.0 - 15/04/2025 🧹 Pré-processamento de dados  
- 0.2.0 - 08/04/2025 📥 Coleta e estruturação dos dados NDVI e produtividade  
- 0.1.0 - 01/04/2025 🔍 Exploração da plataforma SATVeg e definição de escopo  

---

## 📋 Licença

MODELO GIT FIAP por FIAP está licenciado sob Attribution 4.0 International.  
Para mais informações, consulte a licença oficial em: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
