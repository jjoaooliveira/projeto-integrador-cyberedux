# from sklearn.preprocessing import LabelEncoder
import pandas as pd
from django.db.models import F
from dash import Input, Output, dcc
import pandas as pd
from dash import dcc, html
from django_plotly_dash import DjangoDash
import plotly.express as px 
from sistema.models import Turma, Matricula

app = DjangoDash('SimpleExample')

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
print(dff_matriculas)

df_curso = df.groupby(['disciplina__cursos__nome', 'periodo'], as_index=False)['alunos__nome'].nunique()
fig_curso = px.pie(
    df_curso,
    values='alunos__nome',
    names='disciplina__cursos__nome'
)

app.layout = html.Div(
    style={'margin': '2rem auto'},
    children=[
        html.Div(
            className=['container'],
            style={'display': 'flex', 'justifyContent': 'center', 'gap': '.5rem'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.H1(
                            'ALUNOS POR CURSO'
                        ),
                        dcc.Graph(
                            id='output-1',
                            figure=fig_curso 
                        )  
                    ]),
                html.Div(
                    style={'width': '50%'},
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
                    className=[''],
                    style={'width': '100%'},
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
                ]),
            ]
        )
        
    ]
)

@app.callback(
    Output(component_id='output-disciplina', component_property='figure'),
    Input(component_id='input-disciplina', component_property='value')
)

def update_output1(disciplina):
    if len(disciplina) > 0:
        print('oi 1')
        df_turma = dff.loc[dff['disciplina__nome'].isin(disciplina)]
    
        fig_turma = px.bar(
            df_turma,
            x='disciplina__nome', y='alunos__nome', color='periodo',
            labels={'disciplina__nome': 'Disciplina', 'alunos__nome': 'alunos'},
            barmode='group'
        )

    else:
        fig_turma = px.bar(
            dff,
            x='disciplina__nome', y='alunos__nome',
            color='periodo',
            labels={'x': 'Disciplina', 'y': 'n° alunos'},
            barmode='group' 
        )

    return fig_turma

@app.callback(
    Output(component_id='output-escolaridade', component_property='figure'),
    Input(component_id='input-escolaridade', component_property='value')
)

def update_output2(escolaridade):
    if len(escolaridade) > 0:
        print('oi 2')
        dff_matriculas_filtrado = dff_matriculas.loc[dff_matriculas['aluno__escolaridade'].isin(escolaridade)]
        print(dff_matriculas_filtrado)

        fig_escolaridade = px.bar(
            dff_matriculas_filtrado,
            x = 'aluno__escolaridade',
            y='aluno__nome',
            barmode='group'
        )
    
    else:
        fig_escolaridade = px.bar(
            dff_matriculas,
            x = 'aluno__escolaridade',
            y='aluno__nome',
            barmode='group'
        )

    return fig_escolaridade

if __name__ == '__main__':
    app.run(debug=True)
