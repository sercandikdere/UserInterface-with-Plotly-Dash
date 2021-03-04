import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output,State

columnList=["ID","User Name","Display Name","Phone","Email","User Roles","Enabled"]

app=dash.Dash(__name__)

app._layout=html.Div([
    html.Button("Add New User",id="adding-rows-button2",n_clicks=0,style={"height":25,"width":130}),    # Button to add new user
    html.Button("Add New Column",id="adding-rows-button",n_clicks=0,value="",style={"height":25,"width":130}),
    html.Br(),  # New line

    dash_table.DataTable(
        id="adding-rows-table",
        columns=[{
            "name":"{}".format(i),
            "id":"column-{}".format(i),
            "deletable":True,   # to delete the column
            "renamable":True    # for give a new name to the column
        }for i in columnList],
        data=[
            {"column-{}".format(col):"" for col in columnList}
        ],
        editable=True,
        row_deletable=True,       # to delete of chosen row
        sort_action='native',     # to sort of values which chosen column
        filter_action='native',   # to seek a value in a column
        style_header={
            'backgroundColor': 'rgb(80, 80, 255)',
            'fontWeight': 'bold'
        },
        export_format='xlsx',     # to save of table
        export_headers='display'

    )

])

@app.callback(
    Output("adding-rows-table","data"),
    Input("adding-rows-button2","n_clicks"),
    [State("adding-rows-table","data"),
     State("adding-rows-table","columns")]
)
def add_row(n_clicks,rows,columns):

    if n_clicks>0:
        rows.append({i["id"]:"" for i in columns})

    return rows

@app.callback(
    Output("adding-rows-table","columns"),
    Input("adding-rows-button","n_clicks"),
    [State("adding-rows-button","value"),
     State("adding-rows-table","columns")]
)
def update_columns(n_clicks,value,existing_columns):
    if n_clicks>0:
        existing_columns.append({
            "id":value,"name":value,
            "renamable":True,"deletable":True
        })
    return existing_columns


if __name__ == '__main__':
    app.run_server(debug=True)












