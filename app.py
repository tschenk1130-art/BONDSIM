
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

# ==========================================
# BONDSIM - CALCULUS II SEMESTER PROJECT
# ==========================================

st.set_page_config(
    page_title="BONDSIM",
    page_icon="📈",
    layout="wide"
)

FOREST = "#245B4B"
GOLD = "#C2A16A"
BLUE = "#638A9E"
BURGUNDY = "#A34F5B"
INK = "#202B26"
IVORY = "#F7F5EE"

# ==========================================
# WEBSITE DESIGN - ORIGINAL THEME
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;600;700&display=swap');

.stApp {
    background: #F7F5EE;
    color: #202B26;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

html, body, p, li, label, input {
    font-family: 'Inter', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, serif !important;
    color: #245B4B !important;
    text-align: left;
}

.bondsim-heading {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 56px;
    font-weight: 700;
    color: #245B4B;
    text-align: center;
    line-height: 1.2;
}

.bondsim-subheading {
    font-family: 'Inter', sans-serif;
    font-size: 19px;
    color: #34483E;
    text-align: center;
    margin: 10px 0 32px;
}

.page-heading {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 36px;
    font-weight: 700;
    color: #245B4B;
    text-align: center;
    margin: 26px 0;
}

/* Navigation tabs */

.stTabs [data-baseweb="tab-list"] {
    width: 100%;
    display: flex;
    gap: 0;
    border-bottom: 1px solid #C6D2CA;
}

.stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"] {
    flex: 1 1 0;
    min-width: 0;
    justify-content: center;
    background: transparent;
    opacity: 1 !important;
}

.stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"],
.stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"] *,
.stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"] p,
.stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"] span {
    color: #15251D !important;
    -webkit-text-fill-color: #15251D !important;
    opacity: 1 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}

.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
    background: #DFEAE2 !important;
}

.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] *,
.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] p {
    color: #174436 !important;
    -webkit-text-fill-color: #174436 !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    background: #174436 !important;
}

/* Input labels */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] *,
[data-testid="stSlider"] label,
[data-testid="stSlider"] label *,
[data-testid="stSlider"] p,
[data-testid="stNumberInput"] label,
[data-testid="stNumberInput"] label *,
[data-testid="stNumberInput"] p {
    color: #15251D !important;
    -webkit-text-fill-color: #15251D !important;
    opacity: 1 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
}

[data-testid="stSlider"] [data-testid="stTickBar"],
[data-testid="stSlider"] [data-testid="stTickBar"] *,
[data-testid="stSlider"] [data-baseweb="slider"] div,
[data-testid="stSlider"] [data-baseweb="slider"] span {
    color: #15251D !important;
    -webkit-text-fill-color: #15251D !important;
}

[data-testid="stNumberInput"] input {
    color: #15251D !important;
    -webkit-text-fill-color: #15251D !important;
    background-color: #FFFFFF !important;
}

/* Metric cards */

[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #DCE4DC;
    border-radius: 10px;
    padding: 14px;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] * {
    color: #245B4B !important;
    -webkit-text-fill-color: #245B4B !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] * {
    color: #34483E !important;
    -webkit-text-fill-color: #34483E !important;
}

/* Regular text */

[data-testid="stMarkdownContainer"] p {
    color: #202B26;
    text-align: left;
    line-height: 1.7;
}

/* Expander labels */

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary *,
[data-testid="stExpander"] summary p {
    color: #202B26 !important;
    -webkit-text-fill-color: #202B26 !important;
    font-weight: 600 !important;
}

/* Tables */

[data-testid="stTable"] {
    color: #202B26;
}

/* Center formulas */

[data-testid="stLatex"] {
    text-align: center;
}

@media (max-width: 700px) {
    .bondsim-heading {
        font-size: 42px;
    }

    .bondsim-subheading {
        font-size: 15px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def heading(text):
    st.markdown(
        f'<div class="page-heading">{text}</div>',
        unsafe_allow_html=True
    )


def bond_price(y, face, coupon, years):
    return sum(
        coupon / (1 + y) ** t
        for t in range(1, years + 1)
    ) + face / (1 + y) ** years


def first_derivative(y, face, coupon, years):
    return sum(
        -t * coupon / (1 + y) ** (t + 1)
        for t in range(1, years + 1)
    ) - years * face / (1 + y) ** (years + 1)


def second_derivative(y, face, coupon, years):
    return sum(
        t * (t + 1) * coupon / (1 + y) ** (t + 2)
        for t in range(1, years + 1)
    ) + (
        years * (years + 1) * face
        / (1 + y) ** (years + 2)
    )


def style_graph(fig, title, x_title, y_title, height=480):
    fig.update_layout(
        template="plotly_white",
        title=dict(
            text=title,
            x=0.5,
            xanchor="center",
            font=dict(
                family="Playfair Display, Georgia, serif",
                color="#15251D",
                size=22
            )
        ),
        xaxis=dict(
            title=dict(
                text=x_title,
                font=dict(color="#000000", size=15)
            ),
            tickfont=dict(color="#000000", size=13),
            gridcolor="#E3E5DF",
            linecolor="#202B26",
            showline=True
        ),
        yaxis=dict(
            title=dict(
                text=y_title,
                font=dict(color="#000000", size=15)
            ),
            tickfont=dict(color="#000000", size=13),
            gridcolor="#E3E5DF",
            linecolor="#202B26",
            showline=True
        ),
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.25,
            font=dict(color="#000000", size=13),
            bgcolor="#FFFFFF"
        ),
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor="#DCE4DC",
            font=dict(color="#000000", size=13)
        ),
        font=dict(
            family="Inter, sans-serif",
            color="#000000"
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        hovermode="x unified",
        height=height,
        margin=dict(l=75, r=35, t=85, b=115)
    )
    return fig


# ==========================================
# MAIN HEADER
# ==========================================

st.markdown(
    '<div class="bondsim-heading">BONDSIM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="bondsim-subheading">'
    'Traditional Fixed-Rate Bond Calculator using Taylor Series'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# NAVIGATION
# ==========================================

home, learn, examples, simulator, applications, reflection = st.tabs([
    "Home",
    "Learn",
    "Worked Examples",
    "Bond Simulator",
    "Real-World Applications",
    "Reflection"
])


# ==========================================
# TAB 1: HOME
# ==========================================

with home:

    heading("WELCOME")

    st.subheader("Project Overview")

    st.write(
        "BONDSIM is an interactive Calculus II project "
        "that demonstrates how Taylor series can "
        "approximate traditional fixed-rate bond prices "
        "as market interest rates change."
    )

    st.write(
        "The project connects power series and "
        "polynomial approximations with financial "
        "mathematics, specifically duration, convexity, "
        "and interest-rate risk."
    )

    st.divider()

    st.subheader("The Central Question")

    st.write(
        "How can derivatives of a mathematical function "
        "help investors estimate the value of a bond "
        "when market interest rates change?"
    )

    st.write(
        "BONDSIM answers this by comparing exact "
        "bond prices with first-order and second-order "
        "Taylor polynomial approximations."
    )

    st.divider()

    st.subheader("Explore BONDSIM")

    st.markdown("""
**Learn:** Explore power series, Taylor and Maclaurin
series, convergence, derivatives, and approximation error.

**Worked Examples:** Follow complete mathematical
examples, including a real bond pricing calculation.

**Bond Simulator:** Change bond characteristics and
interest rates to compare exact and estimated prices.

**Real-World Applications:** Learn how financial
analysts use duration and convexity to assess risk.

**Reflection:** Review the mathematical conclusions
and limitations of the project.
    """)

    st.divider()

    st.subheader("Project Objectives")

    st.write(
        "By the end of this project, users should "
        "understand how Taylor polynomials are "
        "constructed, why approximation accuracy "
        "depends on distance from the center, "
        "and how those ideas can be applied to finance."
    )


# ==========================================
# TAB 2: LEARN
# ==========================================

with learn:

    heading("LEARN")

    st.subheader("1. Understanding Power Series")

    st.write(
        "A power series is an infinite sum containing "
        "powers of a variable. It has coefficients "
        "that determine the contribution of each term "
        "and a center around which the series is constructed."
    )

    st.latex(
        r"\sum_{n=0}^{\infty}a_n(x-c)^n"
    )

    st.write(
        "Here, a_n is the coefficient of the nth term, "
        "x is the variable, and c is the center."
    )

    st.write(
        "Unlike an ordinary polynomial, a power series "
        "can contain infinitely many terms."
    )

    st.subheader("Convergence and Radius of Convergence")

    st.write(
        "A series converges when its partial sums approach "
        "a finite limit. For a power series, convergence "
        "often depends on how far x is from its center."
    )

    st.latex(
        r"\frac{1}{1-x}=1+x+x^2+x^3+\cdots"
    )

    st.write(
        "This series converges for -1 < x < 1. "
        "Its radius of convergence is R = 1. "
        "Both endpoints diverge, so its interval "
        "of convergence is (-1, 1)."
    )

    st.write(
        "The ratio test is one common method used "
        "to find the radius of convergence. "
        "The endpoints must then be checked separately."
    )

    st.divider()

    st.subheader("2. Taylor Series vs. Maclaurin Series")

    st.write(
        "Taylor and Maclaurin series use the same "
        "mathematical idea: constructing polynomial "
        "representations of functions from derivatives."
    )

    st.write(
        "The difference is the center of expansion."
    )

    st.markdown("""
| Feature | Taylor Series | Maclaurin Series |
|---|---|---|
| Center | Any valid point a | Always a = 0 |
| Uses derivatives | Yes | Yes |
| Polynomial powers | (x-a) | x |
| Purpose | Approximate near a | Approximate near 0 |
| Relationship | General form | Special case of Taylor |
    """)

    st.write("The general Taylor series is:")

    st.latex(
        r"f(x)=\sum_{n=0}^{\infty}"
        r"\frac{f^{(n)}(a)}{n!}(x-a)^n"
    )

    st.write(
        "The Maclaurin series is obtained "
        "by setting a = 0."
    )

    st.latex(
        r"f(x)=\sum_{n=0}^{\infty}"
        r"\frac{f^{(n)}(0)}{n!}x^n"
    )

    st.info(
        "Every Maclaurin series is a Taylor series, "
        "but not every Taylor series is a Maclaurin series."
    )

    st.subheader("Why Does the Center Matter?")

    st.write(
        "A Taylor polynomial is designed to match "
        "a function and its derivatives at the center. "
        "Therefore, the approximation is usually "
        "most accurate near that point."
    )

    st.write(
        "In BONDSIM, the center a represents "
        "the starting market interest rate. "
        "Changing the starting rate changes "
        "where the Taylor approximation is constructed."
    )

    st.divider()

    st.subheader("3. Building Taylor Polynomials")

    st.write(
        "A Taylor polynomial is a finite portion "
        "of the full Taylor series."
    )

    st.write("First-order Taylor polynomial:")

    st.latex(
        r"T_1(x)=f(a)+f'(a)(x-a)"
    )

    st.write(
        "This uses the function's starting value "
        "and slope to form a tangent-line approximation."
    )

    st.write("Second-order Taylor polynomial:")

    st.latex(
        r"T_2(x)=f(a)+f'(a)(x-a)"
        r"+\frac{f''(a)}{2!}(x-a)^2"
    )

    st.write(
        "The second derivative introduces curvature "
        "and can improve the approximation."
    )

    st.write("Third-order Taylor polynomial:")

    st.latex(
        r"T_3(x)=f(a)+f'(a)(x-a)"
        r"+\frac{f''(a)}{2!}(x-a)^2"
        r"+\frac{f'''(a)}{3!}(x-a)^3"
    )

    st.write(
        "Higher-order terms allow the polynomial "
        "to match additional derivatives "
        "of the original function."
    )

    st.divider()

    st.subheader("4. Four Calculus II Practice Problems")

    st.write(
        "The following examples demonstrate "
        "Maclaurin expansion, Taylor expansion "
        "around a nonzero center, graphing, "
        "convergence, and approximation error."
    )

    # --------------------------------------
    # PRACTICE PROBLEM 1
    # --------------------------------------

    with st.expander(
        "Problem 1 - First Four Nonzero Maclaurin Terms",
        expanded=True
    ):

        st.write(
            "Use the Taylor definition to find "
            "the first four nonzero terms for:"
        )

        st.latex(r"f(x)=2\cos^2x,\qquad a=0")

        st.markdown("**Step 1: Simplify using an identity.**")

        st.latex(r"2\cos^2x=1+\cos(2x)")

        st.write(
            "This identity makes differentiation "
            "and the Maclaurin expansion easier."
        )

        st.markdown("**Step 2: Find derivative values.**")

        st.markdown("""
| k | Derivative | Value at 0 |
|---|---|---|
| 0 | 1 + cos(2x) | 2 |
| 1 | -2sin(2x) | 0 |
| 2 | -4cos(2x) | -4 |
| 3 | 8sin(2x) | 0 |
| 4 | 16cos(2x) | 16 |
| 5 | -32sin(2x) | 0 |
| 6 | -64cos(2x) | -64 |
        """)

        st.write(
            "All odd-power coefficients are zero, "
            "so the nonzero terms occur at even powers."
        )

        st.markdown(
            "**Step 3: Divide each derivative by its factorial.**"
        )

        st.latex(
            r"f(x)=2-\frac{4}{2!}x^2"
            r"+\frac{16}{4!}x^4"
            r"-\frac{64}{6!}x^6+\cdots"
        )

        st.markdown("**Final answer:**")

        st.latex(
            r"\boxed{2-2x^2+\frac{2}{3}x^4"
            r"-\frac{4}{45}x^6}"
        )

        st.write(
            "This is a Maclaurin polynomial "
            "because the center is zero."
        )

    # --------------------------------------
    # PRACTICE PROBLEM 2
    # --------------------------------------

    with st.expander(
        "Problem 2 - Taylor Series Centered at a = 4"
    ):

        st.write(
            "Find the Taylor series and radius "
            "of convergence for:"
        )

        st.latex(
            r"f(x)=e^{2x},\qquad a=4"
        )

        st.markdown("**Step 1: Find the derivative pattern.**")

        st.latex(
            r"f^{(n)}(x)=2^n e^{2x}"
        )

        st.write("Evaluate at the center:")

        st.latex(
            r"f^{(n)}(4)=2^n e^8"
        )

        st.markdown(
            "**Step 2: Substitute into the Taylor formula.**"
        )

        st.latex(
            r"f(x)=\sum_{n=0}^{\infty}"
            r"\frac{2^ne^8}{n!}(x-4)^n"
        )

        st.write("The first terms are:")

        st.latex(
            r"e^8\left[1+2(x-4)"
            r"+\frac{2^2(x-4)^2}{2!}"
            r"+\frac{2^3(x-4)^3}{3!}+\cdots\right]"
        )

        st.markdown("**Step 3: Check convergence.**")

        st.write(
            "Apply the ratio test to consecutive "
            "absolute values of the series terms."
        )

        st.latex(
            r"\lim_{n\to\infty}"
            r"\left|\frac{a_{n+1}}{a_n}\right|"
            r"=\lim_{n\to\infty}"
            r"\frac{2|x-4|}{n+1}=0"
        )

        st.write(
            "Since the limit is zero for every "
            "real x, the series converges everywhere."
        )

        st.markdown("**Final answer:**")

        st.latex(
            r"\boxed{e^{2x}=\sum_{n=0}^{\infty}"
            r"\frac{2^ne^8}{n!}(x-4)^n}"
        )

        st.latex(r"\boxed{R=\infty}")

        st.write(
            "This is a Taylor series rather than "
            "a Maclaurin series because it is "
            "centered at a = 4."
        )

    # --------------------------------------
    # PRACTICE PROBLEM 3
    # --------------------------------------

    with st.expander(
        "Problem 3 - Third-Order Taylor Polynomial and Graph"
    ):

        st.write(
            "Find the third-order Taylor polynomial "
            "for the following function centered "
            "at a = 1, and compare the graphs."
        )

        st.latex(
            r"f(x)=5\arctan(x),\qquad a=1"
        )

        st.markdown("**Step 1: Compute derivatives.**")

        st.latex(
            r"f'(x)=\frac{5}{1+x^2}"
        )

        st.latex(
            r"f''(x)=\frac{-10x}{(1+x^2)^2}"
        )

        st.latex(
            r"f'''(x)=\frac{30x^2-10}{(1+x^2)^3}"
        )

        st.markdown(
            "**Step 2: Evaluate the derivatives at x = 1.**"
        )

        st.latex(
            r"f(1)=\frac{5\pi}{4}"
        )

        st.latex(
            r"f'(1)=\frac52,\quad"
            r"f''(1)=-\frac52,\quad"
            r"f'''(1)=\frac52"
        )

        st.markdown(
            "**Step 3: Construct the Taylor polynomial.**"
        )

        st.latex(
            r"\boxed{T_3(x)=\frac{5\pi}{4}"
            r"+\frac52(x-1)"
            r"-\frac54(x-1)^2"
            r"+\frac5{12}(x-1)^3}"
        )

        st.markdown("**Step 4: Compare the graphs.**")

        x = np.linspace(-1, 3, 300)

        original = 5 * np.arctan(x)

        approx = (
            5 * np.pi / 4
            + 2.5 * (x - 1)
            - 1.25 * (x - 1)**2
            + (5 / 12) * (x - 1)**3
        )

        fig_arctan = go.Figure()

        fig_arctan.add_trace(go.Scatter(
            x=x,
            y=original,
            mode="lines",
            name="Original Function",
            line=dict(color=FOREST, width=3)
        ))

        fig_arctan.add_trace(go.Scatter(
            x=x,
            y=approx,
            mode="lines",
            name="Third-Order Taylor",
            line=dict(color=BLUE, width=3)
        ))

        fig_arctan.add_vline(
            x=1,
            line_dash="dash",
            line_color=GOLD
        )

        style_graph(
            fig_arctan,
            "Original Function vs. Taylor Polynomial",
            "x",
            "f(x)"
        )

        st.plotly_chart(
            fig_arctan,
            use_container_width=True,
            theme=None,
            key="arctan_graph"
        )

        st.write(
            "Both curves agree at the center x = 1 "
            "and have matching first three derivatives "
            "there. Their agreement is generally "
            "best near that center."
        )

    # --------------------------------------
    # PRACTICE PROBLEM 4
    # --------------------------------------

    with st.expander(
        "Problem 4 - Taylor Approximation Error"
    ):

        st.write(
            "Find the third-order Taylor polynomial "
            "for the function centered at a = 1, "
            "then bound its error on [0.7, 1.3]."
        )

        st.latex(
            r"f(x)=x^{1/5},\qquad a=1"
        )

        st.markdown("**Step 1: Find the derivatives.**")

        st.latex(
            r"f'(x)=\frac15x^{-4/5}"
        )

        st.latex(
            r"f''(x)=-\frac4{25}x^{-9/5}"
        )

        st.latex(
            r"f'''(x)=\frac{36}{125}x^{-14/5}"
        )

        st.latex(
            r"f^{(4)}(x)=-\frac{504}{625}x^{-19/5}"
        )

        st.write(
            "At x = 1, every power of x equals 1."
        )

        st.markdown(
            "**Step 2: Construct the third-order polynomial.**"
        )

        st.latex(
            r"\boxed{T_3(x)=1+\frac15(x-1)"
            r"-\frac2{25}(x-1)^2"
            r"+\frac6{125}(x-1)^3}"
        )

        st.markdown(
            "**Step 3: Find a bound for the fourth derivative.**"
        )

        st.write(
            "On [0.7, 1.3], the absolute value "
            "of the fourth derivative is greatest at 0.7."
        )

        st.latex(
            r"M=\frac{504}{625}(0.7)^{-19/5}"
        )

        st.markdown("**Step 4: Apply Taylor's inequality.**")

        st.latex(
            r"|R_3(x)|\leq\frac{M}{4!}|x-1|^4"
        )

        M = (504 / 625) * 0.7**(-19/5)
        error_bound = M / 24 * 0.3**4

        st.latex(
            rf"|R_3(x)|\leq {error_bound:.8f}"
        )

        st.markdown("**Step 5: Visualize the actual error.**")

        error_x = np.linspace(0.7, 1.3, 300)

        actual = error_x**0.2

        polynomial = (
            1
            + 0.2 * (error_x - 1)
            - (2 / 25) * (error_x - 1)**2
            + (6 / 125) * (error_x - 1)**3
        )

        absolute_error = np.abs(actual - polynomial)

        fig_error = go.Figure()

        fig_error.add_trace(go.Scatter(
            x=error_x,
            y=absolute_error,
            name="Actual Absolute Error",
            line=dict(color=FOREST, width=3)
        ))

        fig_error.add_hline(
            y=error_bound,
            line_dash="dash",
            line_color=BURGUNDY,
            annotation_text="Guaranteed Error Bound"
        )

        style_graph(
            fig_error,
            "Taylor Polynomial Absolute Error",
            "x",
            "Absolute Error",
            height=460
        )

        st.plotly_chart(
            fig_error,
            use_container_width=True,
            theme=None,
            key="error_graph"
        )

        st.write(
            "The actual error is zero at x = 1 "
            "because the Taylor polynomial equals "
            "the function at its center."
        )

        st.write(
            "The theoretical error bound guarantees "
            "that the approximation error does not "
            "exceed the calculated limit "
            "on the specified interval."
        )

    st.divider()

    st.subheader("5. What These Four Examples Demonstrate")

    st.markdown("""
- **Problem 1:** How derivatives generate Maclaurin coefficients.
- **Problem 2:** How the center changes a Taylor expansion and how the ratio test establishes convergence.
- **Problem 3:** Why Taylor polynomials agree most closely with functions near their expansion centers.
- **Problem 4:** How Taylor's inequality provides a guaranteed bound on approximation error.
    """)

    st.write(
        "Together, these concepts explain the "
        "mathematics used in BONDSIM's financial model."
    )


# ==========================================
# TAB 3: WORKED EXAMPLES
# ==========================================

with examples:

    heading("WORKED EXAMPLES")

    st.subheader("Example 1: Exponential Function")

    st.write(
        "Find the second-order Maclaurin polynomial "
        "for the exponential function."
    )

    st.latex(r"f(x)=e^x")

    st.write(
        "All derivatives of e^x equal e^x, "
        "so at zero each derivative equals 1."
    )

    st.latex(
        r"f(0)=f'(0)=f''(0)=1"
    )

    st.latex(
        r"T_2(x)=1+x+\frac{x^2}{2}"
    )

    st.write("Estimate the function at x = 0.1.")

    st.latex(
        r"T_2(0.1)=1+0.1+\frac{0.1^2}{2}=1.105"
    )

    st.write(
        f"Exact value: {math.exp(0.1):.6f}"
    )

    st.write(
        f"Absolute error: "
        f"{abs(math.exp(0.1)-1.105):.6f}"
    )

    st.divider()

    st.subheader("Example 2: Bond Price Approximation")

    st.write(
        "Consider a five-year fixed-rate bond "
        "with a face value of $1,000, annual coupon "
        "payments of $50, and a starting yield of 5%."
    )

    st.write(
        "Estimate the bond price if the yield "
        "increases to 6%."
    )

    st.latex(
        r"P(y)=\sum_{t=1}^{5}"
        r"\frac{50}{(1+y)^t}"
        r"+\frac{1000}{(1+y)^5}"
    )

    starting_yield = 0.05
    ending_yield = 0.06

    p0 = bond_price(starting_yield, 1000, 50, 5)
    p1 = first_derivative(starting_yield, 1000, 50, 5)
    p2 = second_derivative(starting_yield, 1000, 50, 5)

    dy = ending_yield - starting_yield

    first = p0 + p1 * dy
    second = first + 0.5 * p2 * dy**2

    exact = bond_price(ending_yield, 1000, 50, 5)

    st.markdown("**Step 1: Calculate the original bond price.**")

    st.latex(r"P(0.05)=1000")

    st.markdown("**Step 2: Calculate the derivatives.**")

    st.latex(
        r"P'(y)=-\sum_{t=1}^{5}"
        r"\frac{50t}{(1+y)^{t+1}}"
        r"-\frac{5000}{(1+y)^6}"
    )

    st.latex(
        r"P''(y)=\sum_{t=1}^{5}"
        r"\frac{50t(t+1)}{(1+y)^{t+2}}"
        r"+\frac{30000}{(1+y)^7}"
    )

    st.latex(
        rf"P'(0.05)\approx {p1:.4f}"
    )

    st.latex(
        rf"P''(0.05)\approx {p2:.4f}"
    )

    st.markdown("**Step 3: Calculate the change in yield.**")

    st.latex(
        r"\Delta y=0.06-0.05=0.01"
    )

    st.markdown("**Step 4: First-order approximation.**")

    st.latex(
        rf"T_1=1000+({p1:.4f})(0.01)"
        rf"\approx {first:.4f}"
    )

    st.markdown("**Step 5: Second-order approximation.**")

    st.latex(
        rf"T_2=T_1+\frac{{{p2:.4f}}}{{2}}"
        rf"(0.01)^2\approx {second:.4f}"
    )

    st.markdown("**Step 6: Compare the calculations.**")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Exact Bond Price",
        f"${exact:,.2f}"
    )

    col2.metric(
        "First-Order Taylor",
        f"${first:,.2f}"
    )

    col3.metric(
        "Second-Order Taylor",
        f"${second:,.2f}"
    )

    st.write(
        f"First-order error: ${abs(first-exact):.4f}"
    )

    st.write(
        f"Second-order error: ${abs(second-exact):.4f}"
    )

    st.write(
        "The second-order approximation is more "
        "accurate in this example because it "
        "accounts for the curvature of the "
        "bond price function."
    )


# ==========================================
# TAB 4: BOND SIMULATOR
# ==========================================

with simulator:

    heading("BOND SIMULATOR")

    st.write(
        "Adjust the bond characteristics and compare "
        "exact prices with first-order and second-order "
        "Taylor approximations."
    )

    left, middle, right = st.columns([1, 2, 1])

    with middle:

        face = st.number_input(
            "Bond Face Value ($)",
            min_value=100.0,
            value=1000.0,
            step=100.0
        )

        coupon_pct = st.slider(
            "Annual Coupon Rate (%)",
            0.0, 15.0, 5.0, 0.5
        )

        years = st.slider(
            "Years Until Maturity",
            1, 30, 5
        )

        base_pct = st.slider(
            "Starting Market Interest Rate (%)",
            1.0, 15.0, 5.0, 0.5
        )

        new_pct = st.slider(
            "New Market Interest Rate (%)",
            1.0, 15.0, 6.0, 0.5
        )

    coupon = face * coupon_pct / 100

    base_yield = base_pct / 100
    new_yield = new_pct / 100

    p0 = bond_price(
        base_yield, face, coupon, years
    )

    p1 = first_derivative(
        base_yield, face, coupon, years
    )

    p2 = second_derivative(
        base_yield, face, coupon, years
    )

    change = new_yield - base_yield

    first = p0 + p1 * change
    second = first + 0.5 * p2 * change**2

    exact = bond_price(
        new_yield, face, coupon, years
    )

    st.divider()

    st.subheader("Bond Price Comparison")

    a, b, c = st.columns(3)

    a.metric(
        "Exact Bond Price",
        f"${exact:,.2f}"
    )

    b.metric(
        "First-Order Taylor",
        f"${first:,.2f}"
    )

    c.metric(
        "Second-Order Taylor",
        f"${second:,.2f}"
    )

    st.write(
        f"First-order error: ${abs(first-exact):,.4f}"
    )

    st.write(
        f"Second-order error: ${abs(second-exact):,.4f}"
    )

    st.divider()

    st.subheader("Bond Price vs. Market Interest Rate")

    st.write(
        "The graph compares the exact bond pricing "
        "function with two Taylor polynomial "
        "approximations centered at the starting yield."
    )

    rates = np.linspace(0.01, 0.15, 250)

    exact_line = [
        bond_price(r, face, coupon, years)
        for r in rates
    ]

    first_line = [
        p0 + p1 * (r - base_yield)
        for r in rates
    ]

    second_line = [
        p0
        + p1 * (r - base_yield)
        + 0.5 * p2 * (r - base_yield)**2
        for r in rates
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=rates * 100,
        y=exact_line,
        name="Exact Bond Price",
        mode="lines",
        line=dict(
            color=FOREST,
            width=4
        )
    ))

    fig.add_trace(go.Scatter(
        x=rates * 100,
        y=first_line,
        name="First-Order Taylor",
        mode="lines",
        line=dict(
            color=GOLD,
            width=3,
            dash="dash"
        )
    ))

    fig.add_trace(go.Scatter(
        x=rates * 100,
        y=second_line,
        name="Second-Order Taylor",
        mode="lines",
        line=dict(
            color=BLUE,
            width=3,
            dash="dot"
        )
    ))

    fig.add_trace(go.Scatter(
        x=[new_pct],
        y=[exact],
        name="Selected Interest Rate",
        mode="markers",
        marker=dict(
            color=BURGUNDY,
            size=12
        )
    ))

    fig.add_vline(
        x=base_pct,
        line_dash="dash",
        line_color="#758079"
    )

    style_graph(
        fig,
        "Bond Price and Taylor Approximations",
        "Market Interest Rate (%)",
        "Bond Price ($)",
        height=550
    )

    fig.update_yaxes(
        tickprefix="$",
        tickformat=",.0f"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        theme=None,
        key="bond_simulator_graph"
    )

    st.write(
        "At the starting yield, both Taylor "
        "approximations equal the exact bond price. "
        "As the yield moves farther from the center, "
        "the approximation errors generally increase."
    )

    st.divider()

    st.subheader("Duration and Convexity")

    modified_duration = -p1 / p0
    convexity = p2 / p0

    a, b = st.columns(2)

    a.metric(
        "Modified Duration",
        f"{modified_duration:.4f}"
    )

    b.metric(
        "Convexity",
        f"{convexity:.4f}"
    )

    st.latex(
        r"\frac{\Delta P}{P}\approx"
        r"-D_{mod}\Delta y"
        r"+\frac12 C(\Delta y)^2"
    )

    st.write(
        "Modified duration is based on the "
        "first derivative of the price function. "
        "It estimates the percentage sensitivity "
        "of the bond price to changes in yield."
    )

    st.write(
        "Convexity is based on the second derivative "
        "and measures the curvature of the "
        "price-yield relationship."
    )

    st.divider()

    st.subheader("Understanding the Results")

    st.write(
        "The exact price is calculated by discounting "
        "all future coupon and principal payments."
    )

    st.write(
        "The first-order Taylor estimate uses only "
        "the starting price and slope."
    )

    st.write(
        "The second-order estimate includes a "
        "curvature adjustment, which generally "
        "improves accuracy for small yield changes."
    )


# ==========================================
# TAB 5: REAL-WORLD APPLICATIONS
# ==========================================

with applications:

    heading("REAL-WORLD APPLICATIONS")

    st.subheader("1. Interest-Rate Risk")

    st.write(
        "Interest-rate risk is the possibility "
        "that a bond's market value changes "
        "as market yields change."
    )

    st.write(
        "For a conventional fixed-rate bond, "
        "increasing market yields generally "
        "decrease the bond's price."
    )

    st.divider()

    st.subheader("2. Duration in Financial Analysis")

    st.write(
        "Financial analysts use duration "
        "to estimate how much a bond's "
        "price will change following "
        "a small change in yield."
    )

    st.latex(
        r"\frac{\Delta P}{P}\approx"
        r"-D_{mod}\Delta y"
    )

    st.write(
        "For example, a modified duration of 5 "
        "suggests that a one-percentage-point "
        "increase in yield would cause "
        "approximately a 5% price decrease "
        "using the first-order estimate."
    )

    st.divider()

    st.subheader("3. Convexity in Financial Analysis")

    st.write(
        "Because the relationship between "
        "bond prices and yields is curved, "
        "duration alone is not perfectly accurate."
    )

    st.write(
        "Convexity adds a second-order correction "
        "to account for this curvature."
    )

    st.latex(
        r"\frac{\Delta P}{P}\approx"
        r"-D_{mod}\Delta y"
        r"+\frac12 C(\Delta y)^2"
    )

    st.write(
        "This is a practical application "
        "of the second-order Taylor polynomial."
    )

    st.divider()

    st.subheader("4. Portfolio Risk Management")

    st.write(
        "Investment managers hold portfolios "
        "containing bonds with different maturities, "
        "coupon rates, and market yields."
    )

    st.write(
        "Duration and convexity allow them "
        "to compare interest-rate sensitivity "
        "and estimate the effects of hypothetical "
        "rate changes."
    )

    st.write(
        "These approximations can help managers "
        "evaluate portfolio risk, but complex "
        "securities and large interest-rate "
        "changes may require full repricing."
    )

    st.divider()

    st.subheader("5. Limitations of BONDSIM")

    st.write(
        "BONDSIM models traditional fixed-rate bonds "
        "using annual coupon payments, a fixed "
        "maturity date, and a single constant "
        "yield for discounting."
    )

    st.write(
        "It does not explicitly model default risk, "
        "callable bonds, floating coupons, "
        "or changes in the shape of the yield curve."
    )

    st.write(
        "The Taylor approximation is centered "
        "at one starting yield. Its accuracy "
        "depends on the size of the yield change."
    )


# ==========================================
# TAB 6: REFLECTION
# ==========================================

with reflection:

    heading("REFLECTION")

    st.subheader("Mathematical Conclusions")

    st.write(
        "This project demonstrates that Taylor "
        "polynomials can approximate nonlinear "
        "functions using their derivatives."
    )

    st.write(
        "The first-order approximation represents "
        "the function's value and slope, "
        "while the second-order approximation "
        "also accounts for curvature."
    )

    st.divider()

    st.subheader("What the Visualizations Demonstrate")

    st.write(
        "The graphs illustrate how Taylor "
        "approximations agree most closely "
        "with the original function near "
        "the selected center."
    )

    st.write(
        "Changing the interest rate in BONDSIM "
        "makes the difference between the "
        "exact bond price and the approximations "
        "visible numerically and graphically."
    )

    st.divider()

    st.subheader("Limitations and Accuracy")

    st.write(
        "Taylor polynomials do not necessarily "
        "provide equally accurate estimates "
        "at every point."
    )

    st.write(
        "The approximation error usually grows "
        "as the input moves farther from "
        "the center, which explains why "
        "higher-order terms can be useful."
    )

    st.divider()

    st.subheader("Personal Reflection")
    st.write("""Throughout this project, I developed a deeper understanding of how Taylor polynomials and power series work and how they relate to real-world applications. I learned how higher-degree Taylor polynomials can produce more accurate approximations and how derivatives can be used to approximate entire functions. Connecting these concepts to a real-world application also helped me understand why the center, a, is important and gave me a better understanding of the meaning behind the equations and variables beyond just the mathematics.
I'm actually in the process of transferring back into a finance degree, so this project was especially relevant to my interests. It allowed me to connect calculus with finance while learning about bond pricing, interest-rate risk, and how Taylor series can estimate changes in bond values. I also learned how duration relates to the first derivative and convexity relates to the second derivative. Beyond the mathematics, I improved my Python and Streamlit skills by building an interactive website, creating graphs that respond to user inputs, and troubleshooting issues with the layout, formatting, and readability.
One concept that initially challenged me was understanding why Taylor approximations become less accurate as interest rates move farther from the starting yield, even though the formula itself doesn't change. I also originally questioned why these approximations would be useful when exact values could simply be calculated. However, through this project, I learned that approximations can be valuable for efficiently estimating changes and understanding how different variables affect a financial model. Overall, this project helped me understand Taylor series beyond simply solving problems in class. It showed me how concepts from calculus can be applied to financial analysis while also giving me practical experience with programming and building interactive tools. """    )


# ==========================================
# WEBSITE FOOTER
# ==========================================

st.divider()

st.caption(
    "BONDSIM | Calculus II Semester Project"
)

st.caption(
    "Educational model of fixed-rate bonds "
    "with annual coupon payments."
)
