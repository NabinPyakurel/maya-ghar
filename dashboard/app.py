from dash import Dash
from layouts import layout
from callbacks import register_callbacks

# Initialize Dash app
app = Dash(__name__, suppress_callback_exceptions=True)

# App layout
app.layout = layout

# Callbacks (not really needed for Tableau iframe, but kept for structure)
register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
