<p align="center">
    <img src="https://assets.soyhenry.com/logoOG.png">
</p>

# <h1 align="center">Proyecto Individual Nº1</h1>
# <h1 align="center">Machine Learning Operations (MLOps) - Modelo de recomendación (Steam Dataset)</h1>


## Descripción del Proyecto

En este proyecto, hemos desarrollado un sistema de recomendación basado en el dataset de Steam, utilizando técnicas de Machine Learning y operaciones de MLOps. El objetivo principal es proporcionar recomendaciones personalizadas a los usuarios de la plataforma Steam basándonos en su historial de juego y preferencias.

## Proceso

### Extracción, Transformación y Carga (ETL)

- Realizamos un proceso ETL para preparar los datos para el análisis, incluyendo la limpieza de datos, normalización, y extracción de características relevantes.

### Análisis Exploratorio de Datos (EDA)

- Llevamos a cabo un EDA para comprender mejor las características de los datos, incluyendo la distribución de géneros de juegos, preferencias de los usuarios, y patrones de juego.

### Feature Engineering

- Implementamos técnicas de Feature Engineering para mejorar el rendimiento del modelo, incluyendo análisis de sentimientos en las reseñas de los usuarios para clasificarlas en positivas, neutrales, o negativas.

### Desarrollo de API

- Desarrollamos una API RESTful utilizando FastAPI para exponer los datos y las funcionalidades del modelo a aplicaciones externas. Los endpoints incluyen:

  - Información de desarrolladores
  - Datos de usuario
  - Recomendaciones por género
  - Top desarrolladores por año
  - Análisis de reseñas por desarrollador

### Modelo de Aprendizaje Automático

Implementamos un sistema de recomendación de videojuegos para Steam mediante el algoritmo K Vecinos Más Cercanos (K-NN) y filtrado colaborativo, comenzando con el preprocesamiento de datos para construir una matriz de utilidad optimizada como matriz sparse. Este enfoque facilita la identificación de patrones de juego, utilizando la métrica de similitud del coseno para entrenar el modelo y seleccionar los 20 vecinos más cercanos, equilibrando precisión y eficiencia. La generación de recomendaciones personalizadas se basa en similitudes de patrones de juego, mejorando la experiencia del usuario en Steam. Este sistema demuestra un avance en la personalización de la experiencia de juego, con potencial para futuras mejoras en complejidad y precisión mediante la integración de más datos y técnicas avanzadas.

### Despliegue

- Desplegamos la API en Render para hacerla accesible públicamente. Esto permite a cualquier aplicación consumir los datos y las recomendaciones generadas por nuestro modelo.

## Tecnologías Utilizadas

- Python
- FastAPI
- Pandas
- Scikit-learn
- TextBlob
- NLTK
- Render (para el despliegue)



## Enlaces de Interés

- [API en Render](https://pl-ml-ops.onrender.com/docs)
- [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)
- [Video-Presentación](https://drive.google.com/file/d/1NmkVjW49HoHEfNJf8_muwxmmo0G_EFRD/view?usp=sharing)

<hr>  

<div align="center">
    <img src="./img/hero.jpg" alt="hero" style="width: 200px; height: auto; border-radius: 50%;">
    <h3>Andres Castaño</h3>
    <p>Data Scientist Associate | Geological Engineer</p>
    <a href="https://github.com/FeRsOmBrA" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github" />
    </a>
    <a href="https://www.linkedin.com/in/ferney-castano/" target="_blank">
        <img alt="LinkedIn" src="https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin" />
    </a>
</div>
