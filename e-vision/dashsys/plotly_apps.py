# from sklearn.preprocessing import LabelEncoder
import pandas as pd
from django.db.models import F
from dash import Input, Output, dcc
import pandas as pd
from dash import dcc, html
from django_plotly_dash import DjangoDash
import plotly.express as px 
from sistema.models import Turma, Matricula

app = DjangoDash(
    'SimpleExample'
)

turmas_tet = Turma.objects.all().values(
    'disciplina__nome',
    'periodo',
    'disciplina__cursos__nome',
    'alunos__nome'
)

df = pd.DataFrame(turmas_tet)
dff = df.groupby(['periodo', 'disciplina__nome'], as_index=False)['alunos__nome'].nunique()

matriculas = Matricula.objects.all().values(
    'aluno__escolaridade',
    'aluno__condicao_financeira',
    'aluno__nome',
    'desistencia'
)

df_matriculas = pd.DataFrame(matriculas)
dff_matriculas = df_matriculas.loc[df_matriculas['desistencia'] == True].groupby('aluno__escolaridade', as_index=False)['aluno__nome'].nunique() 

dff_matriculas_cf = df_matriculas.loc[df_matriculas['desistencia'] == True].groupby('aluno__condicao_financeira', as_index=False)['aluno__nome'].nunique() 


df_curso = df.groupby(['disciplina__cursos__nome', 'periodo'], as_index=False)['alunos__nome'].nunique()
fig_curso = px.pie(
    df_curso,
    values='alunos__nome',
    names='disciplina__cursos__nome',
    title='Aluno x Curso',
    labels={'disciplina__cursos__nome': 'DISCIPLINA', 'alunos__nome': 'N° ALUNOS'},
)

app.layout = html.Div(
    style={'margin': '2rem auto'},
    children=[
        html.Div(
            style={
                'display': 'flex', 'flexDirection': 'column',
                'justifyContent': 'center', 'gap': '.5rem'
            },
            children=[
                html.Div(
                    style={'width': '100%'},
                    children=[
                        dcc.Graph(
                            id='output-1',
                            figure=fig_curso 
                        )  
                    ]),
                html.Div(
                    style={'width': '100%'},
                    children=[
                    dcc.Dropdown(
                        dff['disciplina__nome'].unique(),
                        value='',
                        id='input-disciplina',
                        multi=True
                    ),

                    dcc.Graph(
                        id='output-disciplina',
                        figure={}  
                    ),
                ]),
            ],
        ),
        html.Div(
            children=[
                html.H1(
                    children='Desistencias'
                ),
                html.Div(
                    style={'display': 'flex', 'width': '100%', 'flex-direction': 'column'},
                    className=[''],
                    children=[
                        dcc.Dropdown(
                            df_matriculas['aluno__escolaridade'].unique(),
                            value='',
                            id='input-escolaridade',
                            multi=True
                        ),

                        dcc.Graph(
                            id='output-escolaridade',
                            figure={}  
                        ),

                        html.Div(
                            style={
                                'display': 'flex', 'border': '1px solid', 
                                'border-radius': '.5rem', 'padding': '.5rem', 'gap': '.5rem',
                                'flexWrap': 'wrap'
                            },
                            children=[
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ANALFABETO (ANF) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO SUPERIOR COMPLETO (ESC) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='EDUCAÇÃO BÁSICA (EDB) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO FUNDAMENTAL COMPLETO (EFC) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO MÉDIO COMPLETO (EMC) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO SUPERIOR COMPLETO (ESC)'
                                ),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style={'display': 'flex', 'width': '100%', 'flex-direction': 'column'},
                    className=[''],
                    children=[
                        dcc.Dropdown(
                            df_matriculas['aluno__condicao_financeira'].unique(),
                            value='',
                            id='input-condicao',
                            multi=True
                        ),

                        dcc.Graph(
                            id='output-condicao',
                            figure={}  
                        ),

                        html.Div(
                            style={
                                'display': 'flex', 'border': '1px solid', 
                                'border-radius': '.5rem', 'padding': '.5rem', 'gap': '.5rem',
                                'flexWrap': 'wrap'
                            },
                            children=[
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ANALFABETO (ANF) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO SUPERIOR COMPLETO (ESC) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='EDUCAÇÃO BÁSICA (EDB) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO FUNDAMENTAL COMPLETO (EFC) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO MÉDIO COMPLETO (EMC) -'
                                ),
                                html.P(
                                    style={
                                        'textAlign': 'center'
                                    },
                                    children='ENSINO SUPERIOR COMPLETO (ESC)'
                                ),
                            ]
                        )
                    ]
                ),
            ]
        )
        
    ]
)

@app.callback(
    Output(component_id='output-disciplina', component_property='figure'),
    Input(component_id='input-disciplina', component_property='value')
)

def update_output1(disciplina):
    if disciplina:
        df_turma = dff.loc[dff['disciplina__nome'].isin(disciplina)]
    
        fig_turma = px.bar(
            df_turma,
            x='disciplina__nome', y='alunos__nome', color='periodo',
            labels={'disciplina__nome': 'Disciplina', 'alunos__nome': 'alunos'},
            barmode='group',
            text_auto=True,
            title='Alunos x Escolaridade',
        )

    else:
        fig_turma = px.bar(
            dff,
            x='disciplina__nome', y='alunos__nome',
            color='periodo',
            labels={'disciplina__nome': 'DISCIPLINA', 'alunos__nome': 'N° ALUNOS'},
            barmode='group',
            text_auto=True,
            title='Alunos x Disciplina',
        )

    return fig_turma

@app.callback(
    Output(component_id='output-escolaridade', component_property='figure'),
    Input(component_id='input-escolaridade', component_property='value')
)

def update_output2(escolaridade):
    if escolaridade:
        dff_matriculas_filtrado = dff_matriculas.loc[dff_matriculas['aluno__escolaridade'].isin(escolaridade)]

        fig_escolaridade = px.bar(
            dff_matriculas_filtrado,
            x = 'aluno__escolaridade',
            y='aluno__nome',
            barmode='group',
            labels={
                'aluno__escolaridade': 'ESCOLARIDADE', 
                'aluno__nome': 'N° ALUNOS'
            }
        )
    
    else:
        fig_escolaridade = px.bar(
            dff_matriculas,
            x = 'aluno__escolaridade',
            y='aluno__nome',
            barmode='group',
            labels={
                'aluno__escolaridade': 'ESCOLARIDADE', 
                'aluno__nome': 'N° ALUNOS'
            },
            text_auto=True,
            title='Alunos x Escolaridade',
        )

    return fig_escolaridade
@app.callback(
    Output(component_id='output-condicao', component_property='figure'),
    Input(component_id='input-escolaridade', component_property='value')
)


def update_output3(condicao):
    if condicao:
        dff_matriculas_filtrado = dff_matriculas_cf.loc[dff_matriculas['aluno__condicao_financeira'].isin(condicao)]

        fig_condicao = px.bar(
            dff_matriculas_filtrado,
            x = 'aluno__condicao_financeira',
            y='aluno__nome',
            barmode='group',
            labels={
                'aluno__condicao_financeira': 'COND. FINANCEIRA', 
                'aluno__nome': 'N° ALUNOS'
            }
        )
    
    else:
        fig_condicao = px.bar(
            dff_matriculas_cf,
            x = 'aluno__condicao_financeira',
            y='aluno__nome',
            barmode='group',
            labels={
                'aluno__condicao_financeira': 'Condição Financeira', 
                'aluno__nome': 'N° ALUNOS'
            },
            text_auto=True,
            title='Alunos x Condição Financeira',
        )

    return fig_condicao

if __name__ == '__main__':
    app.run(debug=True)
