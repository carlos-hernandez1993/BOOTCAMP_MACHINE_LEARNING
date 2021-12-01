# BOOTCAMP_MACHINE_LEARNING
Un grupo de Directivos solicitó nuestros servicios para la creación y constitución de una empresa 
relacionada al ámbito aeronáutico, destinada exclusivamente a una Línea Aérea Comercial. Por 
lo que a partir de un dataset tomado de la base de datos de Data World se pudo realizar el 
estudio requerido. La empresa solicita la siguiente información:
• Una ciudad como sede que concentre el mayor número de viajeros.
• Variables claves que inciden en el precio del billete.
Además, se pide la creación de un modelo que permita predecir el precio del billete de vuelos a 
distintos destinos desde diferentes lugares de origen, para poder evaluar los beneficios que 
podría dar este negocio.
En primer lugar, se realizó la inspección del dataset el cual consiste de 9 columnas entre las que 
se encuentran el coste del ticket en libras esterlinas, número de viajeros (que en este caso solo 
habrá un único con valor de 1), clase del ticket entre las que se encuentran la clase económica, 
premium económica, business y first (primera clase),tipo de ticket(ya sea de ida o de vuelta), 
fecha del vuelo, lugar de origen, lugar de destino y nombre de aerolínea.
El dataset consta de unos 3000 vuelos aproximadamente, con unos 114 lugares de origen en 
donde se encuentran ciudades de distintos continentes, por nombrar países de América 
tenemos a México y Canadá; de Europa tenemos a España, Inglaterra, Polonia, Irlanda; de Asia 
tenemos a Singapur, Corea del Sur y de África tenemos a Marruecos. Así como también tenemos 
unos 200 lugares de destino.
A partir de esta primera fase, se pudo establecer las correlaciones entre cada una de las variables 
y la variable target (precio del billete). Para esto, lo primero que se hace es pasar a variables 
numéricas cada una de ellas, por medio de funciones de reemplazamiento de string y Label 
Encoder.
Se observa que la variable de mayor importancia respecto al target es el tipo de clase del billete, 
por encima de las otras variables. Asimismo, se identificó correlaciones bajas con respecto a las 
otras variables.
Posteriormente, se borraron las columnas que contenían valores únicos y las columnas con las 
variables categóricas, por lo que quedamos con el dataset limpio, para poder realizar el 
entrenamiento del modelo. Y se observó como hay una distribución asimétrica de los datos, la 
cual mejoró notablemente al aplicar logaritmo.
Se trabajó primero con modelos sencillos de Regresión Lineal y Polinómica, estos dos modelos 
originaron métricas de error alta como el MAE y un r2 score bajo, por ende se pudieron 
descartar. Luego, se ejecutaron otros dos modelos un poco más potentes como lo son el
Gradient Boosting Regressor y el Ada Boost Regressor, pero igualmente dieron métricas no 
deseadas para nuestro estudio.
A continuación,se procedió a usar los modelos XGBoost y Random Forest Regressor, en donde 
dieron métricas de MAE más bajas y un score más alto que ronda un 60%. La diferencia de 
ambos, es que el modelo XGBoost conllevó un mayor coste computacional debido a que para 
entrenarlo tomó unos 40 minutos de ejecución; mientras que el Random Forest, brindó métricas 
un poco mejor y fue ejecutado en mucho menos tiempo, por lo cual el coste computacional es
menor.
Cabe destacar, que lo deseado era obtener métricas mejores, pero al intentar ejecutar modelos 
con variables creadas a partir de variables preexistentes, y borrando otras columnas, el score y 
el MAE nunca mejoraron. Por lo que el modelo antes mencionado fue el seleccionado.
Como conclusión, se pudo entregar a los empresarios un informe en donde el mejor lugar para 
establecer el centro de operaciones de la aerolínea sería la ciudad de Londres, debido a que se 
concentran la mayor cantidad de viajeros. Además, se comunica que la mayor cantidad de clases 
vendidas es la económica, por lo que a partir de esto la compañía puede realizar distintas 
estrategias de venta. En cuanto al modelo de predicción de precios del billete, se entregó el 
modelo de Random Forest Regression, con el cual se pueden predecir los precios de billetes 
dependiendo del lugar de origen, destino, aerolínea,mes, día y clase del billete, y a partir de esto 
se puede calcular un aproximado de cuánto será el precio del billete dependiendo del destino
