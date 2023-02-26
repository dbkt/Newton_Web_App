import streamlit as st
import numpy as np
import time

from button_plot import plot_settings_root, plot_settings_axis, plot_settings_common
from newton_iteration import newton

import matplotlib.pyplot as plt


# Function used certain times
def create_space():
    return st.write("")


st.header("Input area")

# Create 3 columns for the inputs
col = st.columns(3)

# Inputs from user
with col[0]:
    input_function = st.text_input("Enter a function (dependant from x):", value="np.log(x)**2-1")
    create_space()
    input_h = st.number_input("Enter a step wide h:", value=0.000001)
    create_space()

with col[1]:
    input_max_iter = st.number_input("Enter a maximal count of iterations", min_value=1, value=20)
    create_space()
    input_x0 = st.number_input("Enter start value for x", value=1.0)
    create_space()

with col[2]:
    input_d = st.number_input("Enter value for max error", value=0.000001)
    create_space()
    input_sec = st.number_input("Enter speed of Plot", value=0.3)
    create_space()


st.write("")

st.header("Buttons area")

# Create 3 columns for the buttons
col2 = st.columns(5)

# define buttons and put them into the window in the correct format
with col2[0]:
    button_calc = st.button("Calculate")

with col2[1]:
    button_plot = st.button("Plot")

with col2[2]:
    button_reset = st.button("Reset")


def function(x):
    return eval(input_function)


st.write("")

st.header("Output area")

# create button to calculate results of the Newton procedure to find a root of user's function
if button_calc:
    x_fin, x_iter, message = newton(function, input_x0, input_h, input_max_iter, input_d)
    if x_iter == -1:
        result = st.write(message + "Newton Iteration failed to converge.")
    else:
        result = st.write(f"Root in x = {x_fin}. Total iterations = {x_iter}. Function value = {function(x_fin)}")

# set result text to ""
if button_reset:
    x_fin, x_iter, _ = newton(function, input_x0, input_h, input_max_iter)
    result = st.write("")

# Plot function and Newton iteration with a time freeze of input_sec seconds
if button_plot:
    x_fin, _, x_sol = newton(function, input_x0, input_h, input_max_iter)

    fig, ax = plt.subplots(figsize=(8, 6))

    plot_settings_common(function, x_sol, x_fin, fig, ax)
    ax.scatter([x_sol[0]], [function(x_sol[0])], color="black")
    figure_plot = st.empty()

    for x_before, x_now in zip(x_sol[:-1], x_sol[1:]):
        # Plot line from current point to the x-axis along the tangent
        plot_settings_root(function, x_before, x_now, ax)

        # Add previous plot to the streamlit plot within the streamlit window after sec's
        time.sleep(input_sec)
        figure_plot.pyplot(fig)

        # Plot line from current point to the x-axis along the y-value (straight down)
        plot_settings_axis(function, x_now, ax)

        # Add previous plot to the streamlit plot within the streamlit window after sec's
        time.sleep(input_sec)
        figure_plot.pyplot(fig)
