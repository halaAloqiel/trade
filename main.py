import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd



# Data
sectiond = pd.read_excel("data/saudi trade.xlsx", sheet_name="Exports and Imports by Section")
sectiond['Date'] = sectiond['Date'].apply(pd.to_datetime)

importByMode = pd.read_excel("data/saudi trade.xlsx", sheet_name="EXP by Mode of TXP and Port ")

exportsByMode = pd.read_excel("data/saudi trade.xlsx", sheet_name="IMP by Mode of TXP and Port ")

TotalExports = pd.read_excel("data/saudi trade.xlsx", sheet_name="Total Trade")
TotalExports['Date'] = TotalExports['Date'].apply(pd.to_datetime)

oilVsNonOil = pd.read_excel("data/saudi trade.xlsx", sheet_name="oil vs non oil")
oilVsNonOil['date'] = oilVsNonOil['date'].apply(pd.to_datetime)

GccTrading = pd.read_excel("data/saudi trade.xlsx", sheet_name="GCC Trading")
GccTrading['YEAR'] = GccTrading['YEAR'].apply(str)

CountryTrading = pd.read_excel("data/saudi trade.xlsx", sheet_name="Exports & imports by country")
CountryTrading['Date'] = CountryTrading['Date'].apply(pd.to_datetime)
CountryTrading = CountryTrading.sort_values(by="Date")


# figure
TotalTrade = px.line(TotalExports , x= "Date" , y="value", color="Indicator" , template=  "plotly_white" ,color_discrete_sequence=["#8175aa", "#027b8e"])
TotalTrade.update_layout(yaxis_title="", xaxis_title="" ,legend=dict(orientation="h",yanchor="bottom", y=-0.4, xanchor="center",x=0.5, title=""))

oilVsNonOilFig = px.area(oilVsNonOil, x= "date" , y="value", color="indicator" , template=  "plotly_white" ,color_discrete_sequence=["#8175aa", "#027b8e"])
oilVsNonOilFig.update_layout(yaxis_title="", xaxis_title="" ,legend=dict(orientation="h",yanchor="bottom", y=-0.4, xanchor="center",x=0.5, title=""))

# DashApp
app = dash.Dash(__name__ , external_stylesheets = ['https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700'])
server = app.server
app.title = "Saudi Arabia's Trade"

app.layout = html.Div(className="container-fluid py-4", children=([
    html.H3("Saudi Arabia International Trade Performance"),
    html.H5(html.A(href="https://www.stats.gov.sa/en/statistics-overview",children="Source: Gstat")),
    html.Div(className="row",
             children= [html.Div(className="col-xl-3 col-sm-6 mb-xl-0 mb-4" ,
                        children= html.Div(className="card",
                                children = html.Div(className= "card-body p-3" ,
                                            children= html.Div(className="row",
                                                               children=html.Div(
                                                                        children=[html.Div(className="numbers",
                                                                                      children=[html.P(className="text-sm mb-0 text-capitalize font-weight-bold",children="Total Exports in 2021"),
                                                                                                html.H5(className="font-weight-bolder mb-0",children="1,047 B SAR")]),
                                                                             html.H5(children=[html.Span(className="text-success text-sm font-weight-bolder",children="+37.2%"),
                                                                                               html.Span(className="text-muted text-sm font-weight-bolder",children=" since last year")])]))))),

                        html.Div(className="col-xl-3 col-sm-6 mb-xl-0 mb-4" ,
                        children= html.Div(className="card",
                                children = html.Div(className= "card-body p-3" ,
                                            children= html.Div(className="row",
                                                        children= html.Div(
                                                                           children= [html.Div(className="numbers" ,
                                                                                              children = [html.P(className="text-sm mb-0 text-capitalize font-weight-bold" , children="Oil Exports in 2021"),
                                                                                                          html.H5(className="font-weight-bolder mb-0", children="777 B SAR")]),
                                                                                      html.H5(children=[html.Span(className="text-success text-sm font-weight-bolder", children="+41.0%"),
                                                                                                        html.Span(className="text-muted text-sm font-weight-bolder", children=" since last year")])]))))),
                        html.Div(className="col-xl-3 col-sm-6 mb-xl-0 mb-4" ,
                        children= html.Div(className="card",
                                children = html.Div(className= "card-body p-3" ,
                                            children= html.Div(className="row",
                                                        children= html.Div(
                                                                           children= [html.Div(className="numbers" ,
                                                                                              children = [html.P(className="text-sm mb-0 text-capitalize font-weight-bold" , children="Total Imports in 2021"),
                                                                                                          html.H5(className="font-weight-bolder mb-0", children="579 B SAR")]),
                                                                                      html.H5(children=[html.Span(className="text-success text-sm font-weight-bolder", children="+15.0%"),
                                                                                                        html.Span(className="text-muted text-sm font-weight-bolder", children=" since last year")])]))))),
                        html.Div(className="col-xl-3 col-sm-6 mb-xl-0 mb-4" ,
                        children= html.Div(className="card",
                                children = html.Div(className= "card-body p-3" ,
                                            children= html.Div(className="row",
                                                        children= html.Div(
                                                                           children= [html.Div(className="numbers" ,
                                                                                              children = [html.P(className="text-sm mb-0 text-capitalize font-weight-bold" , children="Trade Balance in 2021"),
                                                                                                          html.H5(className="font-weight-bolder mb-0", children="468 B SAR")]),
                                                                                      html.H5(children=[html.Span(className="text-success text-sm font-weight-bolder", children="+64.8%"),
                                                                                                        html.Span(className="text-muted text-sm font-weight-bolder", children=" since last year")])])))))

                        ]),
    html.Div(className="row mt-4",
             children=[html.Div(
                                children=(html.Div(className="card z-index-2",
                                                   children=html.Div(className="card-body p-3",
                                                                     children=[html.P(
                                                                         className="text-sm mb-0 text-capitalize font-weight-bold",
                                                                         children="Total Exports & Imports (million SAR)"),
                                                                               dcc.Graph(figure=TotalTrade)]))))
                       ]),
    html.Div(className="row mt-4",
             children=[html.Div(className="col-lg-6 mb-lg-0 mb-4",
                                children=(html.Div(className="card z-index-2",
                                                   children=html.Div(className="card-body p-3",
                                                                     children=[
                                                                         html.Div(className="row" , children=[
                                                                            html.P(className="col mb-0 text-sm text-capitalize font-weight-bold",children="Exports by Mode & Customes Port (million SAR)"),
                                                                            html.Div(className="col-auto float-end ", children= dcc.RadioItems(exportsByMode["YEAR"].unique() ,2021,id="yearSlideExports" , inline=True))
                                                                         ]),
                                                                         dcc.Graph(id = "ExportsGraph")]
                                                                     )))),
                       html.Div(className="col-lg-6",
                                children=(html.Div(className="card z-index-2",
                                                   children = html.Div(className="card-body p-3" ,
                                                                       children=[
                                                                           html.Div(className="row", children=[
                                                                               html.P(className="col mb-0 text-sm text-capitalize font-weight-bold",children="Imports by Mode & Customs Port(million SAR)"),
                                                                               html.Div(className="col-auto float-end",children=dcc.RadioItems(importByMode["YEAR"].unique() ,2021,id="yearSliderImports" , inline=True))
                                                                           ]),
                                                                           dcc.Graph(id="importByMode")
                                                                       ]))))
                                ]),
    html.Div(className="row mt-4",
             children=[html.Div(className="col-lg-7 mb-lg-0 mb-4",
                                children=(html.Div(className="card z-index-2",
                                                   children = html.Div(className="card-body p-3" ,
                                                                       children=[
                                                                           html.Div(className="row", children=[html.P(className="mb-0 text-sm text-capitalize font-weight-bold",children="Exports & Imports By Countries (million SAR)"), ]),
                                                                           html.Div(className="row",children=[
                                                                                        html.Div(className="col-6 mb-lg-0 mb-4",children=dcc.Dropdown(id="contFilt",options=CountryTrading["Continent"].unique(),value='Asia')),
                                                                                        html.Div(className="col-6",children=dcc.Dropdown(id="countryFilt",options=CountryTrading["Country X"].unique(),value='United Arab Emirates'))

                                                                           ]),
                                                                           dcc.Graph(id='countryTradeFig'),
                                                                        ])))),
                       html.Div(className="col-lg-5",
                                children=(html.Div(className="card z-index-2",
                                                   children = html.Div(className="card-body p-3" ,
                                                                       children=[
                                                                           html.P(className="mb-0 text-sm text-capitalize font-weight-bold" , children="Exports & Imports By Section (million SAR)"),
                                                                           dcc.Dropdown(id="sec", options=sectiond["section"].unique(),value='Live Animals; Animal products'),
                                                                       dcc.Graph(id="trade by section")]))))
                                ]),
    html.Div(className="row mt-4",
             children=[html.Div(className="col-lg-5 mb-lg-0 mb-4",
                                children=(html.Div(className="card z-index-2",
                                                   children=html.Div(className="card-body p-3",
                                                                     children=[html.P(
                                                                         className="text-sm mb-0 text-capitalize font-weight-bold",children="Oil & Non-oil Exports (million SAR)"),
                                                                         dcc.Graph(figure=oilVsNonOilFig)
                                                                            ])))),
                       html.Div(className="col-lg-7",
                                children=(html.Div(className="card z-index-2",
                                                   children = html.Div(className="card-body p-3" ,
                                                                       children=[
                                                                           html.Div(className="row", children=[
                                                                           html.Div(className= "col-lg-6 mb-lg-0 mb-4", children= html.P(className="text-sm mb-0 text-capitalize font-weight-bold" , children="GCC Trading (million SAR)")),
                                                                           html.Div(className='col-lg-3', children=dcc.Dropdown(id='GCCMonths',options=GccTrading['MONTH'].unique(),value='December')),
                                                                           html.Div(className = "col-lg-3", children= dcc.Dropdown(id='GCCYears',options=GccTrading['YEAR'].unique(),value='2021'))]),
                                                                                 dcc.Graph(id = 'GccGraph')
                                                                                 ]))))
                                ]),
]))

@app.callback(
    Output('countryFilt', 'options'),
    Output('countryFilt', 'value'),
    Input('contFilt', 'value')
)


def update_options(contFilt):
    ContTradingFilter = CountryTrading[CountryTrading["Continent"] == contFilt]
    country_options = ContTradingFilter["Country X"].unique()
    return country_options, country_options[0]



@app.callback(
    Output('trade by section' , 'figure'),
    Output('importByMode' ,'figure'),
    Output('GccGraph' ,'figure'),
    Output('ExportsGraph' ,'figure'),
    Output('countryTradeFig' ,'figure'),
    Input('sec' ,'value'),
    Input('yearSliderImports' , 'value'),
    Input('GCCYears', 'value'),
    Input("GCCMonths", 'value'),
    Input('yearSlideExports' , 'value'),
    Input("countryFilt", "value")

)

def update_graph(selected_section , selectedImports_year , GCCYears, GCCMonths, yearSlideExports, countryFilt ):
    filtered_section = sectiond[sectiond["section"] == selected_section]
    filteredImports_year = importByMode[importByMode["YEAR"] == selectedImports_year ]
    importsByModeFig = px.sunburst(filteredImports_year, values='Imports by Mode of Transport and Customs Port',path=['MODE', 'Customs Port'],color_discrete_sequence=["#027b8e", "#8175aa", "#9f8f12"])
    importsByModeFig.update_traces(textinfo="label+percent parent")
    trade_section = px.line(filtered_section, x="Date", y="value" , color="indicator", color_discrete_sequence=["#8175aa", "#027b8e"], template=  "plotly_white")
    trade_section.update_layout(yaxis_title="", xaxis_title="",
                   legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5, title=""))
    GccTrading_fil = GccTrading[(GccTrading["YEAR"]== GCCYears ) & (GccTrading["MONTH"]== GCCMonths)]
    GccGraph = px.bar(GccTrading_fil , x='GCC Country',y="value" , color="indicator", color_discrete_sequence=["#8175aa", "#ccb22b","#027b8e"])
    GccGraph.update_layout(yaxis_title="", xaxis_title="",
                                legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5,
                                            title=""))
    filteredExports_year = exportsByMode[exportsByMode["YEAR"] == yearSlideExports]
    ExportsGraph= px.sunburst(filteredExports_year, values='Exports by Mode of Transport and Customs Port',path=['MODE', 'Customs Port'],color_discrete_sequence=["#027b8e", "#9f8f12","#8175aa" ])
    ExportsGraph.update_traces(textinfo="label+percent parent")

    GccGraph.update_layout(barmode='group',
                         legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5, title=""),
                         template="plotly_white")

    CountryTradingFilter = CountryTrading[CountryTrading["Country X"] == countryFilt]
    countryTradeFig = px.line(CountryTradingFilter, x="Date", y="value", color="indicator", template="plotly_white",color_discrete_sequence=["#8175aa", "#027b8e"])
    countryTradeFig.update_layout(yaxis_title="", xaxis_title="", legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5,title=""))

    return trade_section , importsByModeFig, GccGraph , ExportsGraph, countryTradeFig



if __name__=='__main__':
    app.run_server(debug=False)
