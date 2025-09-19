# src/visualization.py
import plotly.express as px

def scatter_with_trend(df, x="Political_Stability", y="FDI", color="Country Name"):
    """
    Interactive scatter plot with trendline.
    """
    fig = px.scatter(
        df, x=x, y=y, color=color,
        hover_data=["Country Name","Year"],
        trendline="ols",
        title="Political Stability vs FDI"
    )
    return fig

def line_trend(df, x="Year", y_cols=["Political_Stability","FDI"], country=None):
    """
    Line chart for time trends (optionally filtered by country).
    """
    if country:
        df = df[df["Country Name"]==country]

    fig = px.line(df, x=x, y=y_cols, color_discrete_map={
        "Political_Stability":"blue",
        "FDI":"green"
    }, title=f"Trend of Stability & FDI{f' - {country}' if country else ''}")
    return fig
