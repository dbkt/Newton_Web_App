import streamlit as st
import numpy as np
# from functions import newton, function
import matplotlib.pyplot as plt

# Inputs from user
input_function = st.text_input("Enter a function (dependant from x):", value="np.log(x)**2-1")
input_h = st.number_input("Enter a step wide h:", min_value=0.0000001, max_value=1.0, value=0.1, step=0.1)
input_max_iter = st.number_input("Enter a maximal count of iterations", min_value=1, value=20)
input_x0 = st.number_input("Enter start value for x", value=9.0)
input_d = st.number_input("Enter value for max error", value=0.000001)
input_diff = st.number_input("Enter diff for showing the plot between [x-diff, x+diff]", value=2.5)


def function(x):
    return eval(input_function)


def newton(f, x0, h=0.001, max_iter=1000, d=0.0001):
    count = 0
    x1 = x0
    sol = [x0]
    while (count < max_iter) & (abs(f(x0)) >= d):
        derivative = (f(x0 + h) - f(x0 - h)) / (2 * h)
        x1 = x0 - f(x0) / derivative
        count += 1
        x0 = x1
        sol.append(x0)
    return x1, count, np.array(sol)


# create button to calculate results of the Newton procedure to find a root of user's function
if st.button("Calculate"):
    x_fin, x_iter, _ = newton(function, input_x0, input_h, input_max_iter, input_d)
    result = st.write(f"Root in x = {x_fin}. Total iterations = {x_iter}. Function value = {function(x_fin)}")
    # result = st.write("Root in x")
    result

# set result text to ""
if st.button("Reset"):
    x_fin, x_iter, _ = newton(function, input_x0, input_h, input_max_iter)
    result = st.write("")
    result

if st.button("Plot"):
    x_fin, _, x_sol = newton(function, input_x0, input_h, input_max_iter)
    x_axis = np.linspace(x_fin - input_diff, x_fin + input_diff, 10000)
    fig, ax = plt.subplots()
    ax.scatter(x_axis, function(x_axis), marker=".")
    # ax.scatter([x_fin], [function(x_fin)])
    ax.plot(x_sol, function(x_sol), color="orange")
    ax.scatter(x_sol, function(x_sol), s=10, zorder=1)
    ax.grid()
    st.pyplot(fig)
