import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from relatorio_exec import construir

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(BASE, "imagens")
def img(n): return os.path.join(IMG, n)

config = {
 "titulo": "Indicadores Populacionais do Brasil",
 "subtitulo": "Censo Demográfico IBGE 2022 — Análise das 27 Unidades da Federação",
 "meta": "Autora: Ana Paula Galdino  •  Pós-graduação em Data Analytics (POSTECH/FIAP)  •  Junho de 2026",
 "fonte": "Fonte: IBGE — Censo Demográfico 2022  |  Análise: Ana Paula Galdino",
 "sumario": [
   "O Censo Demográfico 2022 registrou <b>203.080.756 habitantes</b> no Brasil, um crescimento de "
   "<b>+6,46%</b> em relação a 2010 — o menor ritmo de crescimento intercensitário da história recente. "
   "Esta análise examina como essa população se distribui entre estados e regiões e quais territórios "
   "lideram (ou estagnam) na dinâmica demográfica.",
   "Dois movimentos se destacam: uma <b>forte concentração</b> da população em poucos estados do Sudeste e "
   "Nordeste, e uma <b>interiorização</b> do crescimento, com Centro-Oeste e Norte avançando muito acima "
   "da média nacional. Esses padrões têm implicações diretas para políticas públicas, expansão de mercado "
   "e decisões de investimento regional.",
 ],
 "kpis": [
   ("203,1 mi", "habitantes (2022)"),
   ("+6,46%", "crescimento 2010–2022"),
   ("52,5%", "população nos 5 maiores estados"),
   ("41,8%", "população no Sudeste"),
 ],
 "secoes": [
   {"titulo": "1. Distribuição da População",
    "texto": [
      "São Paulo concentra sozinho <b>44,4 milhões</b> de habitantes — mais que toda a região Sul somada. "
      "Os três maiores estados (SP, MG e RJ) respondem por cerca de <b>40%</b> da população nacional, "
      "evidenciando o peso histórico do eixo Sudeste.",
      "Em termos regionais, o <b>Sudeste (41,8%)</b> e o <b>Nordeste (26,8%)</b> reúnem mais de dois terços "
      "dos brasileiros, enquanto Norte e Centro-Oeste, apesar da vasta extensão territorial, somam menos de "
      "18% da população — um indicador de baixa densidade e potencial de expansão.",
    ],
    "imagens": [(img("01_top10_populacao.png"), "Top 10 estados por população — Censo 2022"),
                (img("02_distribuicao_regioes.png"), "Participação de cada região na população nacional")]},
   {"titulo": "2. Dinâmica de Crescimento (2010–2022)",
    "texto": [
      "O crescimento populacional foi <b>profundamente desigual</b> entre os estados. <b>Roraima (+41,3%)</b>, "
      "<b>Santa Catarina (+21,8%)</b> e <b>Mato Grosso (+20,5%)</b> lideram com folga, muito acima da média do "
      "país (+6,46%). No extremo oposto, <b>Alagoas (+0,2%)</b>, <b>Rio de Janeiro (+0,4%)</b> e "
      "<b>Bahia (+0,9%)</b> ficaram praticamente estagnados.",
      "O cruzamento entre tamanho e dinamismo revela que os estados mais populosos tendem a crescer abaixo da "
      "média, enquanto territórios menores das fronteiras agrícolas e de serviços (Centro-Oeste e Norte) "
      "puxam o crescimento — confirmando o movimento de <b>interiorização</b> da população brasileira.",
    ],
    "imagens": [(img("03_crescimento_estados.png"), "Variação populacional por estado, colorida por região"),
                (img("05_dispersao_pop_crescimento.png"), "População x crescimento: tamanho do ponto = população")]},
   {"titulo": "3. Concentração e Projeção",
    "texto": [
      "A curva de Pareto mostra que apenas <b>12 das 27 unidades federativas</b> concentram <b>80%</b> da "
      "população — um grau de concentração que orienta priorização de recursos, logística e estratégias "
      "comerciais de alcance nacional.",
      "A comparação entre o Censo 2022 e a estimativa 2025 confirma a continuidade do crescimento nos grandes "
      "centros, com São Paulo projetado para superar <b>46 milhões</b> de habitantes, reforçando a tendência já "
      "observada no período intercensitário.",
    ],
    "imagens": [(img("06_pareto_concentracao.png"), "Concentração populacional acumulada (Curva de Pareto)"),
                (img("04_pop_2022_vs_2025.png"), "Censo 2022 frente à estimativa populacional de 2025")]},
 ],
 "conclusao_titulo": "Conclusões e Recomendações",
 "conclusoes": [
   "<b>Priorização territorial:</b> com 80% da população em 12 estados, ações de alcance nacional devem "
   "concentrar esforços iniciais nesses mercados, sem perder de vista nichos regionais.",
   "<b>Atenção às fronteiras de crescimento:</b> Centro-Oeste e Norte (Roraima, Mato Grosso, Santa Catarina) "
   "são os territórios de maior expansão — relevantes para investimentos de médio e longo prazo.",
   "<b>Mercados maduros:</b> estados estagnados (RJ, AL, BA) demandam estratégias de retenção e ganho de "
   "participação, não de expansão por volume populacional.",
   "<b>Próximos passos analíticos:</b> enriquecer a base com PIB per capita, densidade e indicadores sociais "
   "para transformar a leitura demográfica em recomendações econômicas acionáveis.",
 ],
}

if __name__ == "__main__":
    construir(config, os.path.join(BASE, "Analise_Executiva_IBGE.pdf"))
