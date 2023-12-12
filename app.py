import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            df = pd.read_excel(uploaded_file)
        return df

def plot_histogram(df, column):
    plt.hist(df[column], bins='auto', color='skyblue', alpha=0.7)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

def plot_pie_chart(df, column):
    pie_data = df[column].value_counts()
    plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
    plt.title(f'Pie Chart of {column}')

def plot_line_graph(df, column):
    plt.plot(df[column])
    plt.title(f'Line Graph of {column}')
    plt.xlabel('Index')
    plt.ylabel(column)

def plot_scatter_plot(df, column1, column2):
    plt.scatter(df[column1], df[column2])
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)

def plot_box_plot(df, column):
    plt.boxplot(df[column])
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)

def plot_bar_chart(df, column1, column2):
    sns.barplot(x=column1, y=column2, data=df)
    plt.title(f'Bar Chart of {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)

def main():
    st.title("Data Comparison Visualization App")

    st.sidebar.header("Upload Files")
    file1 = st.sidebar.file_uploader("Upload first file", type=['csv', 'xlsx'])
    file2 = st.sidebar.file_uploader("Upload second file", type=['csv', 'xlsx'])

    plot_type = st.sidebar.selectbox("Select Plot Type", 
                                     ['Histogram', 'Pie Chart', 'Line Graph', 
                                      'Scatter Plot', 'Box Plot', 'Bar Chart'])

    if file1 and file2:
        df1 = load_data(file1)
        df2 = load_data(file2)

        st.sidebar.header("Settings")
        if plot_type in ['Histogram', 'Pie Chart', 'Line Graph', 'Box Plot']:
            column1 = st.sidebar.selectbox("Select column from first file", df1.columns)
            column2 = st.sidebar.selectbox("Select column from second file", df2.columns)
        elif plot_type in ['Scatter Plot', 'Bar Chart']:
            column1 = st.sidebar.selectbox("Select first column from first file", df1.columns)
            column3 = st.sidebar.selectbox("Select second column from first file", df1.columns)
            column2 = st.sidebar.selectbox("Select first column from second file", df2.columns)
            column4 = st.sidebar.selectbox("Select second column from second file", df2.columns)

        if st.button("Generate Plots"):
            fig, axs = plt.subplots(2, figsize=(10, 10))

            plt.sca(axs[0])
            if plot_type == 'Histogram':
                plot_histogram(df1, column1)
            elif plot_type == 'Pie Chart':
                plot_pie_chart(df1, column1)
            elif plot_type == 'Line Graph':
                plot_line_graph(df1, column1)
            elif plot_type == 'Scatter Plot':
                plot_scatter_plot(df1, column1, column3)
            elif plot_type == 'Box Plot':
                plot_box_plot(df1, column1)
            elif plot_type == 'Bar Chart':
                plot_bar_chart(df1, column1, column3)

            plt.sca(axs[1])
            if plot_type == 'Histogram':
                plot_histogram(df2, column2)
            elif plot_type == 'Pie Chart':
                plot_pie_chart(df2, column2)
            elif plot_type == 'Line Graph':
                plot_line_graph(df2, column2)
            elif plot_type == 'Scatter Plot':
                plot_scatter_plot(df2, column2, column4)
            elif plot_type == 'Box Plot':
                plot_box_plot(df2, column2)
            elif plot_type == 'Bar Chart':
                plot_bar_chart(df2, column2, column4)

            plt.tight_layout()
            st.pyplot(fig)

if __name__ == "__main__":
    main()
