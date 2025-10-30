import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_distribution(df, variable):
    """
    Función para graficar, por un lado, la distribución de una variable y los cuartiles (izquierda)
    y, por otro lado, un boxplot (derecha) para identificar la presencia de outliers.
    Muestra también estadísticas descriptivas: cuartiles (Q1, mediana, Q3), media y desviación estándar.
    
    Parameters:
    - df: conjunto de datos numéricos
    - variable: nombre de la variable a graficar
    """
    # Crear una figura con dos subplots en horizontal: histograma (izquierda, 75% del ancho) y boxplot (derecha, 25% del ancho)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5), width_ratios=[3, 1])
    
    sns.set_style("whitegrid")

    # Histograma a la izquierda
    sns.histplot(data=df, x=variable, bins=40, kde=True, ax=ax1)
    ax1.set_title(f'Distribución de {variable}')
    ax1.grid(alpha=0.4)
    
    # Obtener cuartiles, media y desviación estándar
    q1 = df[variable].quantile(0.25)
    q2 = df[variable].quantile(0.5)
    q3 = df[variable].quantile(0.75)
    mean = df[variable].mean()
    std = df[variable].std()
    
    # Añadir valores a los ejes
    ax1.axvline(q1, color='#d62728', linestyle='--',  alpha=0.7, label='Q1 - 25%')
    ax1.axvline(q2, color='#2ca02c', linestyle='--', alpha=0.7, label='Mediana - 50%')
    ax1.axvline(q3, color='#1f77b4', linestyle='--', alpha=0.7, label='Q3 - 75%')
    ax1.axvline(mean, color='#9467bd', linestyle='-', linewidth=2, alpha=0.8, label='Media')
    ax1.axvline(mean - std, color='#8c564b', linestyle=':', alpha=0.7, label='Media ± σ')
    ax1.axvline(mean + std, color='#8c564b', linestyle=':', alpha=0.7)
    # Añadir leyenda para identificar los valores de los ejes
    ax1.legend()
    
    # Boxplot a la derecha
    sns.boxplot(data=df, y=variable, ax=ax2)
    ax2.set_title(f'Boxplot de {variable}')
    ax2.grid(alpha=0.4)
    fig.tight_layout()
    plt.show()