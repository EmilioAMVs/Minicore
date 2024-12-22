# Minicore: Sistema de Filtrado de Gastos por Departamento

Este proyecto es una aplicación web desarrollada con **Django** que permite filtrar y calcular los gastos de una organización en un rango de fechas específico. Los datos están estructurados en tres tablas relacionadas: **Departamento**, **Gasto**, y **Empleado**.

## Funcionalidades Principales

1. **Filtrar gastos por rango de fechas**: 
   - Los usuarios pueden ingresar una fecha de inicio y una fecha final para visualizar los gastos en ese período.

2. **Cálculo total de gastos por departamento**:
   - La aplicación muestra el total de los gastos agrupados por departamento.

3. **Interfaz moderna**:
   - La aplicación utiliza **Bootstrap** para proporcionar una experiencia de usuario amigable.

---

## Despliegue

### Servidor en Azure
La aplicación está desplegada y disponible en **Azure App Service** en la siguiente URL:  
👉 [minicore.azurewebsites.net](minicore.azurewebsites.net)

### Base de Datos
Se utiliza una base de datos PostgreSQL alojada en **Railway**.  
Las configuraciones están definidas en las variables de entorno para garantizar la seguridad.

