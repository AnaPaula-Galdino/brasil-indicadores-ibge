"""
Análise de Indicadores Populacionais do Brasil — Censo IBGE 2022
Autora: Ana Paula Galdino
Gera 6 visualizações executivas (paleta azul) + dashboard interativo (Plotly).
Fonte: IBGE — Censo Demográfico 2022 (ref. 01/08/2022) e estimativa 2025.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import Patch

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados", "indicadores_brasil_2022.csv")
IMG = os.path.join(BASE, "imagens"); DOCS = os.path.join(BASE, "docs")
os.makedirs(IMG, exist_ok=True); os.makedirs(DOCS, exist_ok=True)

C = {"escuro": "#1f4e79", "medio": "#2e6da4", "claro": "#5b9bd5",
     "suave": "#a6c8e0", "destaque": "#4fc3f7", "cinza": "#d9d9d9", "alerta": "#c0392b"}
REGIAO_COR = {"Sudeste": "#1f4e79", "Nordeste": "#2e6da4", "Sul": "#5b9bd5",
              "Norte": "#7fb0d8", "Centro-Oeste": "#a6c8e0"}
FONTE = "Fonte: IBGE — Censo Demográfico 2022  |  Análise: Ana Paula Galdino"
plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans",
    "axes.edgecolor": "#9aa7b8", "axes.linewidth": 0.8, "axes.grid": True,
    "grid.color": "#eef2f7", "grid.linewidth": 1, "axes.axisbelow": True,
    "figure.dpi": 120, "savefig.bbox": "tight"})

def fmt_m(x, _): return f"{x/1e6:.0f}M"
def rodape(fig): fig.text(0.01, 0.005, FONTE, fontsize=7.5, color="#7a8aa0")

def carregar():
    df = pd.read_csv(DADOS)
    df["pop_2010"] = df["pop_2022"] - df["var_abs_2010_2022"]
    df["part_pct_2022"] = df["pop_2022"]/df["pop_2022"].sum()*100
    return df

def g1(df):
    top = df.nlargest(10,"pop_2022").sort_values("pop_2022")
    cores=[C["escuro"] if v>=top["pop_2022"].quantile(0.7) else C["claro"] for v in top["pop_2022"]]
    fig,ax=plt.subplots(figsize=(9.2,5.4)); ax.barh(top["uf"],top["pop_2022"],color=cores)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(fmt_m))
    ax.set_title("Top 10 estados mais populosos — Censo 2022",fontweight="bold",color=C["escuro"],fontsize=14,pad=12)
    ax.set_xlabel("População (milhões de habitantes)")
    for i,v in enumerate(top["pop_2022"]): ax.text(v,i,f"  {v/1e6:.1f}M",va="center",fontsize=9.5,color="#33414f")
    ax.legend(handles=[Patch(color=C["escuro"],label="3 maiores"),Patch(color=C["claro"],label="Demais do Top 10")],
              loc="lower right",frameon=True,fontsize=9)
    rodape(fig); fig.savefig(os.path.join(IMG,"01_top10_populacao.png")); plt.close(fig)

def g2(df):
    reg=df.groupby("regiao")["pop_2022"].sum().sort_values(ascending=False); total=reg.sum()
    cores=[REGIAO_COR[r] for r in reg.index]
    fig,ax=plt.subplots(figsize=(8.4,5.6))
    wedges,_=ax.pie(reg,colors=cores,startangle=90,wedgeprops=dict(width=0.42,edgecolor="white",linewidth=2))
    ax.text(0,0,"203,1 mi\nhabitantes",ha="center",va="center",fontsize=13,fontweight="bold",color=C["escuro"])
    leg=[f"{r}  —  {v/1e6:.1f}M ({v/total*100:.1f}%)" for r,v in reg.items()]
    ax.legend(wedges,leg,title="Região",loc="center left",bbox_to_anchor=(1.0,0.5),frameon=False,fontsize=10)
    ax.set_title("Distribuição da população por região — 2022",fontweight="bold",color=C["escuro"],fontsize=14)
    rodape(fig); fig.savefig(os.path.join(IMG,"02_distribuicao_regioes.png")); plt.close(fig)

def g3(df):
    d=df.sort_values("var_pct_2010_2022"); cores=[REGIAO_COR[r] for r in d["regiao"]]
    fig,ax=plt.subplots(figsize=(9.2,7.2)); ax.barh(d["sigla"],d["var_pct_2010_2022"],color=cores)
    ax.axvline(6.46,color=C["alerta"],ls="--",lw=1.4)
    ax.set_title("Crescimento populacional por estado — 2010 a 2022",fontweight="bold",color=C["escuro"],fontsize=14,pad=12)
    ax.set_xlabel("Variação (%)")
    for i,v in enumerate(d["var_pct_2010_2022"]): ax.text(v+0.4,i,f"{v:.1f}%",va="center",fontsize=8.5,color="#33414f")
    handles=[Patch(color=c,label=r) for r,c in REGIAO_COR.items()]
    handles.append(plt.Line2D([0],[0],color=C["alerta"],ls="--",label="Brasil: +6,46%"))
    ax.legend(handles=handles,loc="lower right",frameon=True,fontsize=9,title="Região")
    ax.set_xlim(0,d["var_pct_2010_2022"].max()*1.12)
    rodape(fig); fig.savefig(os.path.join(IMG,"03_crescimento_estados.png")); plt.close(fig)

def g4(df):
    top=df.nlargest(12,"pop_2022").sort_values("pop_2022",ascending=False)
    x=np.arange(len(top)); w=0.4
    fig,ax=plt.subplots(figsize=(10,5.4))
    ax.bar(x-w/2,top["pop_2022"],w,label="Censo 2022",color=C["escuro"])
    ax.bar(x+w/2,top["pop_2025_est"],w,label="Estimativa 2025",color=C["destaque"])
    ax.set_xticks(x); ax.set_xticklabels(top["sigla"])
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_m))
    ax.set_title("População: Censo 2022 vs Estimativa 2025 (Top 12)",fontweight="bold",color=C["escuro"],fontsize=14,pad=12)
    ax.set_ylabel("População"); ax.legend(frameon=True,fontsize=10)
    rodape(fig); fig.savefig(os.path.join(IMG,"04_pop_2022_vs_2025.png")); plt.close(fig)

def g5(df):
    fig,ax=plt.subplots(figsize=(9.6,6))
    for r,cor in REGIAO_COR.items():
        s=df[df["regiao"]==r]
        ax.scatter(s["pop_2022"],s["var_pct_2010_2022"],s=s["pop_2022"]/45000+40,color=cor,
                   alpha=0.85,edgecolor="white",linewidth=1,label=r)
    for _,row in df.iterrows():
        if row["var_pct_2010_2022"]>18 or row["pop_2022"]>15e6 or row["var_pct_2010_2022"]<1:
            ax.annotate(row["sigla"],(row["pop_2022"],row["var_pct_2010_2022"]),fontsize=8.5,ha="center",
                        va="bottom",xytext=(0,6),textcoords="offset points",color="#33414f")
    ax.axhline(6.46,color=C["alerta"],ls="--",lw=1,alpha=0.7)
    ax.text(df["pop_2022"].max(),6.9,"média Brasil",color=C["alerta"],fontsize=8,ha="right")
    ax.set_xscale("log"); ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_:f"{x/1e6:.0f}M"))
    ax.set_xlabel("População 2022 (escala log)"); ax.set_ylabel("Crescimento 2010–2022 (%)")
    ax.set_title("Tamanho x Dinamismo: população vs crescimento",fontweight="bold",color=C["escuro"],fontsize=14,pad=12)
    ax.legend(title="Região",frameon=True,fontsize=9,loc="upper right")
    rodape(fig); fig.savefig(os.path.join(IMG,"05_dispersao_pop_crescimento.png")); plt.close(fig)

def g6(df):
    d=df.sort_values("pop_2022",ascending=False).reset_index(drop=True)
    cum=d["pop_2022"].cumsum()/d["pop_2022"].sum()*100
    fig,ax=plt.subplots(figsize=(10,5.6)); ax.bar(d["sigla"],d["pop_2022"],color=C["claro"],label="População por estado")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_m)); ax.set_ylabel("População")
    ax.tick_params(axis="x",labelrotation=90,labelsize=8)
    ax2=ax.twinx(); ax2.plot(d["sigla"],cum,color=C["escuro"],marker="o",ms=4,lw=2,label="% acumulado")
    ax2.axhline(80,color=C["alerta"],ls="--",lw=1.2,label="80% da população"); ax2.set_ylim(0,105)
    ax2.set_ylabel("% acumulado"); ax2.grid(False)
    n80=int((cum<=80).sum())+1; ax2.text(n80-1,82,f"{n80} estados = 80%",color=C["alerta"],fontsize=9,fontweight="bold")
    ax.set_title("Concentração populacional (Curva de Pareto)",fontweight="bold",color=C["escuro"],fontsize=14,pad=12)
    l1,la1=ax.get_legend_handles_labels(); l2,la2=ax2.get_legend_handles_labels()
    ax.legend(l1+l2,la1+la2,loc="center right",frameon=True,fontsize=9)
    rodape(fig); fig.savefig(os.path.join(IMG,"06_pareto_concentracao.png")); plt.close(fig)

def dashboard(df):
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    d=df.sort_values("pop_2022",ascending=False)
    colorway=["#1f4e79","#2e6da4","#5b9bd5","#7fb0d8","#a6c8e0"]
    fig=make_subplots(rows=2,cols=2,
        specs=[[{"type":"bar"},{"type":"domain"}],[{"type":"treemap"},{"type":"scatter"}]],
        subplot_titles=("População por estado (Censo 2022)","Participação por região",
                        "Mapa de proporção: região › estado","População × Crescimento 2010–2022"),
        vertical_spacing=0.12,horizontal_spacing=0.08,row_heights=[0.45,0.55])
    fig.add_trace(go.Bar(x=d["sigla"],y=d["pop_2022"],marker_color="#1f4e79",
        hovertemplate="<b>%{x}</b><br>%{y:,.0f} hab.<extra></extra>"),row=1,col=1)
    reg=df.groupby("regiao")["pop_2022"].sum().reindex(["Sudeste","Nordeste","Sul","Norte","Centro-Oeste"])
    fig.add_trace(go.Pie(labels=reg.index,values=reg.values,hole=0.5,marker=dict(colors=colorway),
        hovertemplate="<b>%{label}</b><br>%{value:,.0f} (%{percent})<extra></extra>"),row=1,col=2)
    fig.add_trace(go.Treemap(labels=list(df["uf"])+list(reg.index),
        parents=list(df["regiao"])+[""]*len(reg),values=list(df["pop_2022"])+[0]*len(reg),
        marker=dict(colors=[REGIAO_COR[r] for r in df["regiao"]]+colorway),
        hovertemplate="<b>%{label}</b><br>%{value:,.0f} hab.<extra></extra>",textinfo="label+percent root"),row=2,col=1)
    for r,cor in REGIAO_COR.items():
        s=df[df["regiao"]==r]
        fig.add_trace(go.Scatter(x=s["pop_2022"],y=s["var_pct_2010_2022"],mode="markers+text",
            text=s["sigla"],textposition="top center",name=r,
            marker=dict(size=s["pop_2022"]/600000+8,color=cor,line=dict(width=1,color="white")),
            hovertemplate="<b>%{text}</b><br>Pop: %{x:,.0f}<br>Cresc.: %{y:.1f}%<extra></extra>"),row=2,col=2)
    fig.update_xaxes(type="log",title_text="População (log)",row=2,col=2)
    fig.update_yaxes(title_text="Crescimento (%)",row=2,col=2)
    fig.update_layout(title=dict(text="<b>Painel Executivo — Indicadores Populacionais do Brasil (Censo IBGE 2022)</b>",
        font=dict(size=20,color="#1f4e79")),showlegend=False,height=900,template="plotly_white",
        font=dict(family="Inter, Arial",size=12),margin=dict(t=100,b=60),
        annotations=[dict(text="Fonte: IBGE — Censo Demográfico 2022 | Análise: Ana Paula Galdino",
            xref="paper",yref="paper",x=0,y=-0.06,showarrow=False,font=dict(size=10,color="#7a8aa0"))])
    fig.write_html(os.path.join(DOCS,"index.html"),include_plotlyjs="cdn")

def main():
    df=carregar()
    for f in (g1,g2,g3,g4,g5,g6,dashboard): f(df)
    print("OK. Graficos:",sorted([x for x in os.listdir(IMG) if x.startswith('0')]))

if __name__=="__main__": main()
