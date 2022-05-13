import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash import dcc, dash
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
import json
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly import graph_objects as go



import os
# port = int(os.environ.get('PORT', 50000))  # add these lines in code



##Carregando datasets
# Data
df = px.data.iris()
df_mapa = pd.read_csv('datasets/empresas_mapa_new2.csv')
df_empresas = pd.read_csv('datasets/df_empresas_fast4sign_geral.csv')  # carregando os dados das empresas
df_sales_mensal = pd.read_csv('datasets/sales_mensal.csv')  # carregando os dados das empresas
df_usuarios_assinantes = pd.read_csv('datasets/df_usuarios_assinates.csv')
usuarios_assinantes = pd.read_csv("datasets/usuarios_assinantes.csv", sep=';', encoding = 'Windows-1252')
df_atendimentos = pd.read_csv('datasets/hubspot_atendimentos_agrupado_2022.csv')
df_testando = pd.read_csv('datasets/df_usuarios_testando.csv')

#Carregando os dados de geolocalização
with open('datasets/estados_brasil.geojson') as response: # carregando o arquivo ".geojson"
    limites_brasil = json.load(response)
for feature in limites_brasil ['features']: # adicionado o ID aos dados
    feature['id'] = feature['properties']['name']







def drawMapa():
    #pass
    #df_ano = df2[df2['Ano'] >= 2000]
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id='map-brazil',
                    figure=px.choropleth_mapbox(
                        df_mapa,  # primeiro parâmetro é o dataframe com os dados
                        locations='Estado',  # coluna do DF que referencia as IDs do mapa
                        geojson=limites_brasil,  # arquivo com os limites dos estados
                        color='Total',  # indicando qual coluna será utilizada para pintar os estados
                        mapbox_style="carto-positron",  # estilo do mapa
                        center={'lon': -55, 'lat': -14},  # definindo a posição inicial do mapa
                        zoom=2.5,  # definindo o zoom do mapa (número inteiro entre 0 e 20)
                        opacity=1.0,  # definindo uma opacidade para a cor do mapa
                        hover_name="Estado",  # nome do hover
                        color_continuous_scale='greens',  # muda a escala de cor
                        range_color=[0, df_mapa['Total'].max()],  # limites do eixo Y
                    ).update_layout(
                        template='plotly_dark',
                        margin={"r": 0, "t": 0, "l": 0, "b": 0},
                        title_text="Carteira Ativa por Estado ",
                        # plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        # paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    )
                )
            ])
        ),
    ])


def drawResultado():
    #pass
    #df_ano = df2[df2['Ano'] == 2021]
    #df_emp_resultado_por_ano['Total'] = df_emp_resultado_por_ano.valor.sum()
    #df_resultado_2020 = df_emp_resultado_por_ano.loc[(df_emp_resultado_por_ano.Ano == 2020)]
    #df_resultado_2021 = df_emp_resultado_por_ano.loc[(df_emp_resultado_por_ano.Ano == 2021)]
    #df_indice = ((float(df_resultado_2020.valor.sum()) - float(df_resultado_2021.valor.sum()) / float(df_resultado_2021.valor.sum()) * -1)) * 100
    #print('Indice',df_indice)
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id='bar_resultado',
                    figure=px.bar(df_sales_mensal, y="Total", x="month",
                    ).update_layout(
                            template='plotly_dark',
                            bargap=0.2,
                            margin={"r": 0, "t": 30, "l": 0, "b": 0},
                            title_text="Vendas por Mês",
                            xaxis_title_text='Ano',  # xaxis labNO
                            yaxis_title_text='Faturamento (R$)',  # yaxis label
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',


                    ).update_traces(texttemplate='%{y:$.2f}', textposition='outside')
                )
            ])
        ),
    ])



def drawEmpresaPorEstado():
    #pass
    empresas_uf = df_empresas
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id='bar_emp_uf',
                    figure=px.bar(df_empresas, y="Total", x="uf",
                    ).update_layout(
                            template='plotly_dark',
                            bargap=0.2,
                            margin={"r": 0, "t": 30, "l": 0, "b": 0},
                            xaxis_title_text='UF',  # xaxis labNO
                            yaxis_title_text='Quantidade',  # yaxis label
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',
                            title_text="Carteira Ativa por Estado ",
                    )
                )
            ])
        ),
    ])



def drawVendas():
    df_sales = df_sales_mensal
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(
                            go.Scatter(
                                x=df_sales['month'],
                                y=df_sales['Total'],
                                name="Desempenho",
                            )
                    ).add_trace(
                        go.Bar(
                            x=df_sales['month'],
                            y=df_sales['Total'],
                            text=df_sales['Total'],
                            name="Vendas",
                        )
                    ).update_layout(
                        title="Resultado Vendas Mensal",
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        bargap=0.05

                    )
                )
                ])
            )
    ])




def drawAssinantesFree():
    df_assinantes = df_usuarios_assinantes
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(
                            go.Scatter(
                                x=df_assinantes['month'],
                                y=df_assinantes['Total'],
                                name="Desempenho",
                            )
                    ).add_trace(
                        go.Bar(
                            x=df_assinantes['month'],
                            y=df_assinantes['Total'],
                            text=df_assinantes['Total'],
                            name="Usuários Free",
                        )
                    ).update_layout(
                        title="Assinantes FREE",
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        bargap=0.05

                    )
                )
                ])
            )
    ])



def drawClientesTestando():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(
                            go.Scatter(
                                x=df_testando['month'],
                                y=df_testando['Total'],
                                name="Desempenho",
                            )
                    ).add_trace(
                        go.Bar(
                            x=df_testando['month'],
                            y=df_testando['Total'],
                            text=df_testando['Total'],
                            name="Usuários Free",
                        )
                    ).update_layout(
                        title="Assinantes FREE",
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        bargap=0.05

                    )
                )
                ])
            )
    ])



# def drawEmpresasPorSituacao():
#     #pass
#     df_ano = df2[df2['Ano'] == 2021]
#     df1_gr = df_empresas_devolus.groupby(['situacao', ]).size().reset_index(name='Total')
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     id='pie_empresas_situacao',
#                     figure=px.pie(df1_gr, values='Total', names='situacao', color='situacao',
#                                color_discrete_map={'ATIVO': 'lightcyan',
#                                                    'GRATÚITO': 'cyan',
#                                                    'TESTE': 'royalblue',
#                                                    'INATIVO N PGTO': 'darkblue'}
#                     ).update_layout(
#                             template='plotly_dark',
#                             bargap=0.2,
#                             margin={"r": 0, "t": 30, "l": 0, "b": 0},
#                             title="Empresas por Situação",
#                             plot_bgcolor='rgba(0, 0, 0, 0)',
#                             paper_bgcolor='rgba(0, 0, 0, 0)',
#                     )
#                 )
#                 ])
#             )
#     ])


def drawAtendiemntos():
    # df_atendimentos.sort_values("month")
    # df_emp_situacao_geral = df_empresas_devolus_geral.groupby(['uf', 'situacao']).size().reset_index(name='Total')
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_atendimentos, x="month", y="Total", color="Proprietário do negócio"
                    ).update_layout(
                        title_text="Atendimentos por Atendente (Mês)",
                    ),
                    config={
                        'displayModeBar': True
                    }
                )
            ])
        ),
    ])




# def drawEmpAtivaCancelada():
#     # df_ativas_canceladas = df_empresas_ativas_canceladas.groupby(['uf', 'situacao']).size().reset_index(name='count')
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.bar(
#                         df_empresas_ativas_canceladas, x="uf", y="count", color="situacao"
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                         title_text="Ativas X Canceladas",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])
#
#
#
# def drawEmpPorValor():
#     df_ativos = df_empresas_devolus_geral[df_empresas_devolus_geral['situacao'] == 'Ativa']
#     df_result = df_ativos.groupby(['uf']).sum().reset_index()
#     # print(df_result)
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.bar(
#                         df_result, x="uf", y="valor",
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                         title_text="Mercado por Valor (R$)",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])
#
#
# def drawTableCancelados():
#     df_cancelados_trimestre = df_emp_preparadas[(df_emp_preparadas['dtcancelamento'] >= '2021-11-01') & (df_emp_preparadas['situacao'] == 'Cancelada')]
#     df_nomes_cancelados = df_cancelados_trimestre[['nome', 'dtcancelamento', 'valor', 'uf']]
#     # print(df_nomes_cancelados)
#     # pass
#     # print(df_cancelados_trimestre)
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=ff.create_table(df_nomes_cancelados).update_layout(
#                         title_text="Empresas que cancelaram último trimestre",
#                         margin={'t': 100, 'b': 100},
#                     )
#                 )
#             ])
#         )
#     ])
#
#
# def drawTableExtras():
#     selected = df_empresas_add_extras[["Nome do Cliente", "dif"]]
#     selected.sort_values(by=['dif'], ascending=False).head(10)
#
#     # grouped_df = selected.groupby("dif")
#     #maximos = grouped_df.max()
#     #maximos = maximos.reset_index()
#     # maximos.sort_values('dif', ascending=True)
#     # maximos.drop("Unnamed: 0", axis=1)
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=ff.create_table(selected).update_layout(
#                         title_text="Rankind de empresas que mais consomem extras",
#                         margin={'t': 50, 'b': 20},
#                     )
#                 )
#             ])
#         )
#     ])
#
#
#
def drawfunil():
    df_funil = usuarios_assinantes[(usuarios_assinantes['Data de Cadastro'] >= '2022-01-01') & ((usuarios_assinantes['Situação'] != 'INATIVA_PAG') & (usuarios_assinantes['Situação'] != 'GRATUITO') & (usuarios_assinantes['Situação'] != 'CANCELADA'))]
    df_gruped = df_funil.groupby(['Situação']).size().reset_index(name='Total')
    # new_row1 = {'Situação': 'IMPRESSOES', 'Total': 252404}
    new_row2 = {'Situação': 'CLIQUES', 'Total': 6932}
    # df_gruped = df_gruped.append(new_row1, ignore_index=True)
    df_gruped = df_gruped.append(new_row2, ignore_index=True)
    order = ['CLIQUES', 'TESTE', 'GRATUITO', 'ATIVA', 'CANCELADA']
    df_gruped = df_gruped.reindex(df_gruped['Situação'].map(dict(zip(order, range(len(order))))).sort_values().index)

    # df_funil_teste = df[(df['Data de Cadastro'] >= '2022-01-01') & (df['Situação'] == 'TESTE')].size
    # df_funil_venda = df[(df['Data de Cadastro'] >= '2022-01-01') & (df['Situação'] == 'ATIVA')].size
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.funnel_area(
                        names=df_gruped['Situação'],
                        values=df_gruped['Total'],
                        # marker={"line": {"color": ['aliceblue'],
                        #                  "width": [0, 1, 5,]}},
                    ).update_layout(
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',
                            title_text="Funil de Resultado Até Abril 2022"
                    ),
                )
            ])
        )
    ])



# def drawSalesTrimestre():
#     # df_emp_resultado_ultimo_trimestre.sort_values(by='month', ascending=True, inplace=True)
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.line(df_emp_resultado_ultimo_trimestre, x='month', y='Total'
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                         title_text="Vendas por Trimestre (QTD)",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])
#
#
#
#
#
# def drawEmpCanceladaUf():
#     df_cancelados = df_emp_preparadas[(df_emp_preparadas['dtcancelamento'] >= '2021-11-01') & (df_emp_preparadas['situacao'] == 'Cancelada')]
#     df_emp_cancelado_estado = df_cancelados.groupby(['uf']).size().reset_index(name='Total')
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.bar(
#                         df_emp_cancelado_estado, x="uf", y="Total"
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                         title_text="Cancelados Por UF - Último Trimestre",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])
#
#
#
#
#
# def drawInadimplentes():
#     df_inadimoplentes.drop("Unnamed: 0", axis=1)
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.line(df_inadimoplentes, x='month', y='Total'
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                         title_text="Inadimplência por mês",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])




# def drawCanceladosPeriodo():
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.line(df_cancelados_e_vendidos_por_mes, x='month', y='Total'
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                         title_text="Cancelados Ultimo Semestre (QTD)",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])


# def drawCanceladosPeriodo():
#     result_df = df_cancelados_e_vendidos_por_mes
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure = go.Figure(
#                     ).add_trace(go.Scatter(x=result_df['month'], y=result_df['sum_x'], mode='lines+markers', name='Vendas')
#                     ).add_trace(go.Scatter(x=result_df['month'], y=result_df['sum_y'], mode='lines+markers', name='Cancelados')
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                         title_text="Vendas X Cancelados (Semestre) (R$)",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])





# def drawHubSpot():
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.bar(
#                         df_hubspot, x="month", y="Total", color="Etapa do negÃ³cio"
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor='rgba(0, 0, 0, 0)',
#                         paper_bgcolor='rgba(0, 0, 0, 0)',
#                         title_text="Atendimento HUBSpot Até Jan/22 por Fase",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])



# def drawEmpresasDevolusgrSitua():
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.bar(
#                        df_emp_devolus_gr_situa , x="month", y="Total", color="situacao"
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor='rgba(0, 0, 0, 0)',
#                         paper_bgcolor='rgba(0, 0, 0, 0)',
#                         title_text="Quantidade Empresas por situação",
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 )
#             ])
#         ),
#     ])



# Iris bar figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_white',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),
    ])

# Text field
def drawMrr():
    result = df_empresas[df_empresas['Situação'] == 'ATIVA']
    mrr = result['Preço'].sum()
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H3('MRR'),
                    html.Br(),
                    html.H3('R$ ' + format(mrr, '.2f')),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

def drawAtivos():
    df_empresas.drop("Unnamed: 0", axis=1)
    result_emp = df_empresas[df_empresas['Situação'] == 'ATIVA']
    result_assinantes = usuarios_assinantes[usuarios_assinantes['Situação'] == 'ATIVA']
    ativos = len(result_emp.index) + len(result_assinantes.index)
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H3('ATIVOS'),
                    html.Br(),
                    html.H3(format(ativos)),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

def drawfree():
    result = df_empresas[df_empresas['Situação'] == 'GRATUITO']
    free = len(result.index)
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H3('GRATUITO'),
                    html.Br(),
                    html.H3(format(free)),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])



def drawTeste():
    result = df_empresas[df_empresas['Situação'] == 'TESTE']
    testando = len(result.index)
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H3('TESTANDO'),
                    html.Br(),
                    html.H3(format(testando)),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])



def drawLost():
    result = df_empresas[df_empresas['Situação'] == 'CANCELADA']
    cancelada = len(result.index)
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H3('CANCELADA'),
                    html.Br(),
                    html.H3(format(cancelada)),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])


# Text field
# def drawLost():
#     df_cancelados = df_emp_preparadas[(df_emp_preparadas['dtcancelamento'] >= '2021-11-01') & (df_emp_preparadas['situacao'] == 'Cancelada')]
#     lost = df_cancelados['valor'].sum()
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 html.Div([
#                     html.H3('LOST (TRI)'),
#                     html.Br(),
#                     html.H3('R$ ' + format(lost, '.2f')),
#                 ], style={'textAlign': 'center'})
#             ])
#         ),
#     ])


# def drawWon():
#     df_cancelados = df_emp_preparadas[(df_emp_preparadas['dtcompra'] >= '2021-11-01') & (df_emp_preparadas['situacao'] == 'Ativa')]
#     won = df_cancelados['valor'].sum()
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 html.Div([
#                     html.H3('WON (TRI)'),
#                     html.Br(),
#                     html.H3('R$ ' + format(won, '.2f')),
#                 ], style={'textAlign': 'center'})
#             ])
#         ),
#     ])
#
#
# def drawOneShot():
#     oneshot = df_empresas_add_extras.dif.sum()
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 html.Div([
#                     html.H3('One Shot (Mensal)'),
#                     html.Br(),
#                     html.H3('R$ ' + format(oneshot, '.2f')),
#                 ], style={'textAlign': 'center'})
#             ])
#         ),
#     ])
#
#
# def drawCarteira():
#     df_result = df_empresas_geral_tratadas[df_empresas_geral_tratadas.situacao == 'Ativa']
#     df_count = len(df_result)
#     # print(df_result)
#     #pass
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 html.Div([
#                     html.H3('CARTEIRA (Ativos)'),
#                     html.Br(),
#                     html.H3(df_count),
#                     #html.H3(format(indinad, '.2f')),
#                 ], style={'textAlign': 'center'})
#             ])
#         ),
#     ])

def drawText2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("20%"),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])



# Build App
app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawMrr()
                ], width=2),
                dbc.Col([
                    drawAtivos()
                ], width=2),
                dbc.Col([
                    drawfree()
                ], width=2),
                dbc.Col([
                    drawTeste()
                ], width=2),
                dbc.Col([
                    drawLost()
                ], width=2),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawVendas()
                ], width=7),
                dbc.Col([
                    drawMapa()
                ], width=5),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawAssinantesFree()
                ], width=6),
                dbc.Col([
                    drawfunil()
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawAtendiemntos()
                ], width=7),
                dbc.Col([
                    drawClientesTestando()
                ], width=5),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    # drawHubSpot()
                ], width=7),
                dbc.Col([
                    # drawEmpCanceladaUf()
                ], width=5),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    # drawSalesTrimestre()
                ], width=7),
                dbc.Col([
                    # drawfunilTrimestre()
                ], width=5),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    # drawTableCancelados()
                ], width=12),
            ], align='center'),
            dbc.Row([
                dbc.Col([
                    # drawTableExtras()
                ], width=12),
            ], align='center'),
        ]), color = 'dark'
    )
])

# import io
# import requests
# url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
# s=requests.get(url).content
# c=pd.read_csv(io.StringIO(s.decode('utf-8')))

# web: python dashboard-devolus.py

# Run app and display result inline in the notebook
# if __name__ == "__main__":
server = app.server
app.run_server(host='0.0.0.0', port=8080, debug=True)
