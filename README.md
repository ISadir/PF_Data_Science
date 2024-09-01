# Proyecto Grupal - PF Data Science - Henry bootcamp

<img src="https://i.postimg.cc/5NGkYLrz/Proyecto-final-Henry-2.png" alt="Proyecto-final-Henry" width="900">

# Índice

1. [¿Quienes Somos?](#¿quienes-somos?)
2. [Nuestro cliente](#nuestro-cliente)
3. [Nuestra propuesta](#nuestra-propuesta)
4. [KPIs](#kpis)
5. [Tecnologías](#tecnologías)
6. [Metodología de trabajo](#metodología-de-trabajo)
7. [Producto](#producto)
8. [Colaboradores](#colaboradores)


# ¿Quienes Somos?

<p align="center">
<img src="https://i.postimg.cc/jjKymB7Y/logo.png" alt="Proyecto-final-Henry" width="250">
</p>

>Somos una consultora que transforma los datos en información. Buscamos ser un aliado estratégico para su empresa, centrados en ayudarle a alcanzar sus objetivos a través del correcto aprovechamiento de sus datos. Nuestro propósito es  transformar positivamente el entorno a través del uso inteligente de la información.

<p align="center">
<img src="https://i.postimg.cc/xCMSbwGk/equipo.png" alt="Proyecto-final-Henry" width="650">
</p>

# Nuestro cliente

>Empresa de renombre en el rubro de transportes de larga distancia. En busca de ingresar al mercado de transporte de pasajeros con automóviles con su nueva unidad de negocios **NYC GreenCabs**. Sabemos el interés que tienen por conseguir un futuro menos contaminado y más verde.<br>
Por eso en **Urban Data** realizamos el siguiente análisis preliminar sobre los taxis en NYC para que con este tengan un marco de referencia, puedan tomar decisiones bien fundamentadas y comprendan aún más las tendencias actuales del mercado de transporte.

# Nuestra propuesta

>El objetivo general es, al término del proyecto, maximizar la efectividad de información sobre el mercado de taxis disponible, para que el cliente pueda obtener un marco de referencia y poder tomar decisiones bien fundamentadas para proseguir con su nueva unidad de negocios.

## Objetivos específicos

>Elaborar un estudio de la situación actual (2019) del sector de transporte de pasajeros en NYC para definir la factibilidad del negocio.
Crear un modelo de ML que permita analizar a futuro cómo se desarrolla el mercado de autos eléctricos/híbridos para transporte de pasajeros en NYC.
Crear un modelo de ML que informe cómo varía la contaminación de CO2 en NYC y permita dar fundamentos a la puesta en marcha de la empresa taxis con energías verdes.
Diseñar un dashboard que muestre de forma clara y directa para el cliente las información relevante generada en las etapas previas.
Desarrollar un Data Warehouse (en la nube) en donde poder almacenar todos los datos y automatizar su ciclo de vida para futuras consultas del cliente.

# KPIs

En consonancia con los objetivos se plantean una serie de KPIs que serán medidores de desempeño para evaluar la información obtenida.


- Como uno de los objetivos principales del cliente es reducir la emisión de CO2, se crea este KPI que evalúa las variaciones de la concentración de CO2 en el aire año a año.


$$Variación\ CO_2 = ((CO_2\ año\ actual - CO_2\ año\ anterior) / CO_2\ año\ anterior) * 100\%$$


- Además, se necesita conocer cómo fue evolucionando el mercado de taxis verdes en relación a los tradicionales, por eso se calcula el siguiente KPI:


$$Ratio\ Taxis\ Verde = (Viajes\ taxis verdes/Viajes\ totales\ del\ mes)*100\%$$


- Finalmente, como en cualquier negocio, se debe evaluar la rentabilidad, por lo que se genera el KPI ROI (retorno de inversión, por sus siglas en inglés). Se contemplaran distintos escenarios de inversión.


$$ROI=(Ganancia\ neta / inversión)*100\%$$

$$ROI=((Ingresos\ totales\ mensual - Costos\ totales\ mensual) / inversión)*100\%$$


# Tecnologías

<p align="center">
 <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="50" height="50"/> 
 </a> 
 <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="50" height="50"/> 
 </a>
 <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="50" height="50"/> 
 </a>
<a href="https://cloud.google.com/storage/?_gl=1*1ljt00g*_up*MQ..&gclid=Cj0KCQjwzva1BhD3ARIsADQuPnUt7bWhxla9ofW4Qf0r6BlrA-R4l-xsBXO47SRxM6FP749mo3npYKIaAvhuEALw_wcB&gclsrc=aw.ds&hl=es_419" target="_blank" rel="noreferrer">
   <img src="https://www.gstatic.com/bricks/image/8b43e59a7cf2a59f124a3883f58cb970c96e393831e025759271b050b92bd6dc.svg" alt="Cloud Storage" width="60" height="60"/>
</a>
<a href="https://cloud.google.com/bigquery/?_gl=1*927n8u*_up*MQ..&gclid=Cj0KCQjwzva1BhD3ARIsADQuPnUt7bWhxla9ofW4Qf0r6BlrA-R4l-xsBXO47SRxM6FP749mo3npYKIaAvhuEALw_wcB&gclsrc=aw.ds&hl=es_419" target="_blank" rel="noreferrer">
   <img src="https://www.gstatic.com/bricks/image/702bc723dcfcddf8942bb459be20163106a5f64ed91404df38c73ca955f96260.svg" alt="BigQuery" width="60" height="60"/>
</a>
<a href="https://powerbi.microsoft.com/" target="_blank" rel="noreferrer">
   <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" alt="Power BI" width="60" height="60"/>
</a>
<a href="https://facebook.github.io/prophet/" target="_blank" rel="noreferrer">
   <img src="https://facebook.github.io/prophet/static/logo.svg" alt="Prophet" width="60" height="60"/>
</a>
<a href="https://plotly.com/" target="_blank" rel="noreferrer">
   <img src="https://images.plot.ly/logo/new-branding/plotly-logomark.png" alt="Plotly" width="60" height="60"/>
</a>
<a href="https://streamlit.io/" target="_blank" rel="noreferrer">
   <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit" width="60" height="60"/>
</a>

</p>

<p align="center">
<img src="https://i.postimg.cc/9Qm8d624/Proyecto-final-Henry.gif" alt="Proyecto-final-Henry" width="800">
</p>

# Metodología de trabajo

<p align="center">
 
## Metodología de gestión del proyecto: **SCRUM**
</p>

<div style="text-align: justify;">

>Marco de trabajo ágil a través del cual un equipo pueden abordar problemas complejos a la vez que se entregan productos con el máximo valor. Es un enfoque más flexible e iterativo que permite responder y adaptarse continuamente al entorno para construir el mejor producto final para el cliente.<br>
El uso exitoso de Scrum depende de cinco valores: **compromiso, enfoque, apertura, respeto y coraje**<br>
En el equipo no hay subequipos ni jerarquías,  es una unidad cohesionada de profesionales enfocados en un objetivo a la vez. Son multifuncionales y lo suficientemente pequeños como para permanecer ágil y lo suficientemente grande como para completar un trabajo.
</div>

<p align="center">
<img src="https://i.postimg.cc/3JpnQK80/scrum.png" alt="Proyecto-final-Henry" width="800">
</p>

# Producto

## En el siguiente link se puede encontrar el MVP del producto, donde se tiene la parte de ML y de BI: <a href="https://pf-data-science-urbandata.streamlit.app/" style="font-size: 52px;">🚕</a>



# Colaboradores

## *Inés Sadir*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ines-sadir/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ISadir)


## *Miguel Denis*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/miguel-denis-a835b92a9/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MiguelDenisP)


## *Matias Sosa*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matias-agustin-sosa/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Matias-Agustin-Sosa)


## *Guido Biotti*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guido-biotti/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Guido-Biotti)

#
<p align="center">
<img src="https://i.postimg.cc/zvPZmq8c/gracias.png" alt="Proyecto-final-Henry" width="400">
</p>
