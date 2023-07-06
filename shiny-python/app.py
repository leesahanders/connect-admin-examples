## Thanks Roger!! https://github.com/lagerratrobe/R_Data/blob/master/app.py

import matplotlib.pyplot as plt
import pandas
from shiny import App, render, ui

app_ui = ui.page_fluid(
    # App title ----
    ui.panel_title("Old Faithful Geyser Data - from Roger"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider("n", "Number of bins:", 1, 50, 30),
        ),
        ui.panel_main(
            ui.output_plot("histogram"),
        ),
    ),
)


def server(input, output, session):
    @output
    @render.plot(alt="A histogram")
    def histogram():
        df = pandas.read_csv("https://raw.githubusercontent.com/lagerratrobe/R_Data/master/faithful.csv")
        x = df["waiting"]
        plt.title("Histogram of waiting times")
        plt.hist(x, input.n(), density=True)
        plt.xlabel("Waiting time to next eruption (in mins)")
        plt.ylabel("Frequency")

app = App(app_ui, server, debug=True)

if __name__ == "__main__":
    app.run()
    
