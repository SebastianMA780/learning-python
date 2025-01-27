La arquitectura del framework está diseñada para ser reutilizable y organizar todas tus tareas. 
Utiliza el modelo MVT (Model, View, Template).


- **Model**
	- Es la capa de acceso a la base de datos.
	- Contiene toda la lógica de negocio.

- **View**
	- Actúa como un conector
	- Accede y dirige los datos
	- controla el flujo de peticiones y respuestas
	- verifica permisos y realiza comprobaciones necesarias

- **Template**
	- Es la capa de presentación
	- Se encarga de mostrar los datos al usuario

### Cómo interactúan las capas?

- El flujo de datos es el siguiente:
	- El modelo pasa datos a la vista en un array.
	- La vista pasa esos datos al template en un contexto.
	- El template muestra los datos gráficos.

- En sentido contrario:
	- Un usuario busca en el template.
	- La vista recibe la búsqueda y consulta al modelo.
	- El modelo devuelve los resultados a la vista
	- La vista envía los datos al template para mostrarlos.


**Nota:**  No debe haber conexión directa entre template y model. Siempre usa la vista para asegurar verificaciones y permisos.