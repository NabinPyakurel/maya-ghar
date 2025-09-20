from dash import html


TABLEAU_EMBED_URL = (
    "https://public.tableau.com/views/Book1_17582585060170/Dashboard1"
    "?:embed=y&:display_count=yes&:showVizHome=no"
)

layout = html.Div(
    style={
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "center",
        "minHeight": "100vh",
        "backgroundColor": "#f9f9f9",
        "padding": "0",
        "margin": "0",
    },
    children=[
        html.H1(
            "Research Question: Is political stability linked to higher foreign investment?",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "20px",
                "fontFamily": "Arial, sans-serif",
            },
        ),
        html.H1(
            "Political Stability & FDI Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "20px",
                "fontFamily": "Arial, sans-serif",
            },
        ),
        html.Div(
            children=[
                html.Iframe(
                    src=TABLEAU_EMBED_URL,
                    style={
                        "height": "90vh",   # fill most of viewport height
                        "width": "95vw",    # almost full width
                        "border": "2px solid #ddd",
                        "borderRadius": "12px",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.1)",
                        "backgroundColor": "white",
                    },
                )
            ],
            style={
                "width": "100%",
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
            },
        ),
    ],
)