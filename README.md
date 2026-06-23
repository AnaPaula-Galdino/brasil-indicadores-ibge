# 📊 Indicadores Populacionais do Brasil — Análise do Censo IBGE 2022

Análise exploratória **nível executivo** dos dados populacionais das 27 Unidades da
Federação, com base no **Censo Demográfico 2022 do IBGE**. O projeto transforma os
dados oficiais em **6 visualizações profissionais**, um **dashboard interativo** e uma
**análise executiva em PDF** — pronta para leitura de gestores e tomadores de decisão.

> 📄 **[Análise Executiva (PDF)](Analise_Executiva_IBGE.pdf)** &nbsp;|&nbsp; 📈 Dashboard interativo em `docs/index.html`
> (após habilitar GitHub Pages: `https://anapaula-galdino.github.io/brasil-indicadores-ibge/`)

---

## 🎯 Objetivo

Responder, com dados oficiais, perguntas estratégicas:

- Como a população brasileira se distribui entre estados e regiões?
- Quais territórios mais cresceram (e quais estagnaram) entre 2010 e 2022?
- Qual o grau de concentração populacional e o que isso significa para decisões de mercado?

## 🔍 Principais insights

| Indicador | Resultado |
|---|---|
| População total (Censo 2022) | **203.080.756** habitantes |
| Crescimento 2010–2022 | **+6,46%** (menor ritmo intercensitário recente) |
| Concentração dos 5 maiores estados | **52,5%** da população |
| Região mais populosa | **Sudeste** (41,8%) |
| Concentração de 80% da população | em apenas **12 estados** |
| Maior crescimento | **Roraima** (+41,3%) |
| Menor crescimento | **Alagoas** (+0,2%) |

**Leitura executiva:** o Brasil combina **forte concentração** (Sudeste + Nordeste = 2/3 da
população) com um movimento de **interiorização** — Centro-Oeste e Norte crescem muito acima
da média, enquanto grandes centros maduros (RJ, BA, AL) estagnam.

## 📈 Visualizações

| | |
|---|---|
| ![Top 10](imagens/01_top10_populacao.png) | ![Regiões](imagens/02_distribuicao_regioes.png) |
| ![Crescimento](imagens/03_crescimento_estados.png) | ![Dispersão](imagens/05_dispersao_pop_crescimento.png) |
| ![Pareto](imagens/06_pareto_concentracao.png) | ![2022 vs 2025](imagens/04_pop_2022_vs_2025.png) |

O **dashboard interativo** (`docs/index.html`) reúne ranking por estado, participação
regional, um **treemap** região › estado e o gráfico população × crescimento, todos com tooltips.

## 🛠️ Tecnologias

**Python 3.10+** · **pandas** · **matplotlib** · **plotly** · **reportlab** (relatório PDF)

## 📂 Estrutura

```
brasil-indicadores-ibge/
├── README.md
├── Analise_Executiva_IBGE.pdf          # Relatório executivo (PDF)
├── requirements.txt
├── dados/indicadores_brasil_2022.csv   # Dados do Censo 2022 por UF
├── src/
│   ├── analise_ibge.py                 # Gera os 6 gráficos + dashboard
│   └── gerar_relatorio.py              # Gera o PDF executivo
├── imagens/                            # 6 gráficos (PNG)
└── docs/index.html                     # Dashboard interativo (GitHub Pages)
```

## ▶️ Como executar

```bash
pip install -r requirements.txt
python src/analise_ibge.py       # gera gráficos e dashboard
python src/gerar_relatorio.py    # gera a análise executiva em PDF
```

## 🗂️ Fonte dos dados

**IBGE — Censo Demográfico 2022** (referência 01/08/2022), com estimativa 2025 e variação
intercensitária 2010–2022. Dados públicos do [SIDRA/IBGE](https://sidra.ibge.gov.br) e do
[portal do Censo 2022](https://censo2022.ibge.gov.br).

---

👤 **Ana Paula Galdino** · Pós-graduação em Data Analytics (POSTECH/FIAP)
[GitHub](https://github.com/AnaPaula-Galdino) · [LinkedIn](https://linkedin.com/in/galdinoana/)
