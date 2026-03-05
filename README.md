# Mockups - Plataforma de Automatización de Viáticos

Este proyecto contiene los mockups completos del sistema de automatización de reportes y cálculo de viáticos para tripulantes, basados en el documento funcional proporcionado.

## Estructura del Proyecto

```
PROYEC/
├── index.html                  # Dashboard principal
├── login.html                  # Página de inicio de sesión
├── registro-vuelos.html        # Módulo de registro de vuelos
├── calculo-viaticos.html       # Módulo de cálculo automático
├── reportes.html               # Módulo de generación de reportes
├── control-caja.html           # Módulo de control de caja
├── ingreso-manual.html         # Módulo de ingreso manual
├── administracion.html         # Módulo de administración
├── servidor.py                 # Servidor HTTP para compartir (Python)
├── servidor.bat                # Script para iniciar servidor (Windows)
├── subir-github.bat            # Script para subir cambios a GitHub
├── INSTRUCCIONES_COMPARTIR.md  # Guía para compartir el sistema
├── GUIA_GITHUB.md             # Guía completa para publicar en GitHub Pages
├── styles/
│   ├── common.css              # Estilos comunes
│   └── dashboard.css           # Estilos del dashboard
└── README.md                   # Este archivo
```

## Módulos Implementados

### 1. Dashboard Principal (`index.html`)
- Vista general del sistema
- Estadísticas de viáticos pendientes
- Total calculado del mes
- Estado de cajas (SCL y LIM) con alertas
- Acciones rápidas
- Últimos movimientos

**Campos y Elementos:**
- Tarjetas de estadísticas
- Botones de acciones rápidas
- Tabla de últimos movimientos
- Indicadores de alerta

### 2. Registro de Vuelos (`registro-vuelos.html`)
- Formulario para registro manual de vuelos
- Importación de reporte AIMS
- Listado de vuelos registrados

**Campos:**
- ID Tripulante (búsqueda automática de nombre)
- Nombre Tripulante (auto-completado)
- Rol Cumplido (CPT, FO, FE, CC)
- Base del Tripulante
- Vuelo / Tramo
- Fecha de Operación
- Destino Final
- Puerto de Pago
- Horarios (Presentación, Salida, Llegada, Retorno, TSV Inicio)
- Observaciones

**Botones:**
- Importar Reporte AIMS
- Registrar Vuelo
- Limpiar Formulario
- Validar Datos
- Filtrar / Exportar (en tabla)

### 3. Cálculo de Viáticos (`calculo-viaticos.html`)
- Vista de viáticos calculados y pendientes
- Filtros avanzados
- Detalle de cálculo por registro
- Aprobación y generación de débitos

**Campos en Tabla:**
- Checkbox de selección
- ID Tripulante, Nombre, Rol
- Vuelo, Fecha, Base, Destino
- Hora Llegada
- Noches, Valor Diario, % Aplicado
- Monto Calculado, Moneda, Caja
- Regla Aplicada, Estado

**Botones:**
- Calcular Todos los Pendientes
- Recalcular Seleccionados
- Filtrar / Buscar
- Ver Detalle
- Aprobar y Generar Débito
- Exportar Seleccionados

**Sección de Detalle:**
- Información completa del vuelo
- Traza del cálculo
- Regla aplicada y justificación

### 4. Generación de Reportes (`reportes.html`)
- Generación de reportes consolidados y detallados
- Filtros por tipo, fecha, país, estación
- Exportación en múltiples formatos
- Reporte especial para rutas EZE-REC

**Campos de Filtro:**
- Tipo de Reporte (Consolidado, Detallado, por País, por Estación, por Tripulante, Rutas Especiales)
- Fecha Desde / Hasta
- País
- Estación / Caja
- Formato de Exportación (Excel, PDF, CSV)
- Checkboxes para incluir pendientes y ajustes

**Botones:**
- Generar Reporte
- Limpiar Filtros
- Exportar a Excel / PDF
- Enviar por Email
- Ver Historial de Reportes

**Reporte Especial:**
- Reporte semanal para rutas EZE-REC
- Consolidación para pagos por transferencia bancaria

### 5. Control de Caja (`control-caja.html`)
- Visualización de saldos de cajas
- Registro de abonos
- Registro de ajustes manuales
- Historial de movimientos

**Información de Caja:**
- Límite Establecido
- Saldo Actual
- Disponible
- Alertas de porcentaje usado

**Formulario de Abono:**
- Caja
- Monto
- Motivo / Descripción
- Documento de Respaldo

**Formulario de Ajuste Manual:**
- Caja
- Tipo de Ajuste (Corrección, Reembolso, Gasto Extra, Otro)
- Monto (positivo/negativo)
- Fecha del Ajuste
- Motivo Detallado
- Documento de Respaldo (obligatorio)
- Checkbox de confirmación

**Tabla de Movimientos:**
- Fecha, Caja, Tipo Movimiento
- Descripción, Monto
- Saldo Anterior, Saldo Resultante
- Usuario

**Botones:**
- Nueva Caja
- Registrar Abono
- Ver Movimientos
- Registrar Ajuste

### 6. Ingreso Manual (`ingreso-manual.html`)
- Registro de viáticos especiales no extraídos de AIMS
- Carga masiva por CSV
- Validación de duplicados

**Tipos de Caso Especial:**
- Apoyo a Otra Base (1 mes o más)
- Comisión de Servicio (CRSV)
- Delivery de Avión
- Búsqueda de Aeronave
- Otro Caso Especial

**Campos del Formulario:**
- ID Tripulante (búsqueda automática)
- Nombre Tripulante (auto-completado)
- Tipo de Caso Especial
- Base del Tripulante
- Destino / Base de Apoyo
- Caja de Pago
- Fecha Inicio / Fin
- Monto Estimado
- Moneda
- Motivo Detallado
- Documento de Respaldo

**Carga Masiva:**
- Upload de archivo CSV
- Validación de duplicados
- Descarga de plantilla

**Botones:**
- Carga Masiva (CSV)
- Registrar Viático Manual
- Limpiar Formulario
- Validar Duplicados
- Cargar y Validar (CSV)
- Descargar Plantilla CSV

### 7. Administración (`administracion.html`)
- Gestión de usuarios
- Configuración de reglas de cálculo
- Valores diarios por país
- Gestión de cajas

**Gestión de Usuarios:**
- Tabla con: Usuario, Nombre, Email, Rol, Estado, Último Acceso
- Botones: Nuevo Usuario, Editar, Desactivar

**Configuración de Reglas:**
- Mantenedor dinámico de reglas
- Tabla con: País, Tipo Regla, Condición, Porcentaje, Estado
- Botones: Nueva Regla, Editar

**Valores por País:**
- Tabla con: Código, Puerto/Ciudad, País, Valor Diario (USD), Última Actualización
- Botones: Actualizar Valores, Editar

**Gestión de Cajas:**
- Tabla con: Código, Nombre, Estación, País, Límite, Regla Asociada, Estado
- Botones: Nueva Caja, Editar

## Características de Diseño

### Colores Principales
- Azul primario: `#1e3a8a`
- Verde éxito: `#10b981`
- Rojo peligro: `#ef4444`
- Amarillo alerta: `#f59e0b`
- Gris neutro: `#6b7280`

### Componentes Reutilizables
- Botones (Primary, Secondary, Danger, Success)
- Formularios con validación visual
- Tablas de datos responsivas
- Badges de estado
- Alertas informativas
- Cards contenedores
- Sidebar de navegación

### Responsive
- Diseño adaptable a diferentes tamaños de pantalla
- Grid system flexible
- Navegación lateral colapsable (preparado)

## Usuarios del Sistema

### Administradores Totales
- **Daniel López** - Gerente de Roles
- **Andrés Guevara** - Jefe Recovery y Crew Tracking
- **Mayra Rifo** - Analista Crew Travel

**Permisos:**
- Ver y modificar ajustes de saldos
- Acceso completo a todos los módulos
- Gestión de usuarios y configuración

### Administradores Parciales
- **Crew Tracking** - Equipo de turno SOC

**Permisos:**
- Solo visualización de reportes
- Ajustes manuales limitados
- Sin acceso a configuración de sistema

## Reglas de Negocio Implementadas

1. **Identificador Único de Viático:**
   - ID Tripulante + Fecha + Vuelo + Rol + Puerto de Pago
   - Prevención de doble pago

2. **Políticas de Pago:**
   - Reglas generales y específicas por país
   - Porcentajes 50% / 100% según horarios
   - Valores diarios configurables por puerto

3. **Control de Caja:**
   - Límites: SCL $80,000, LIM $40,000
   - Alertas preventivas
   - Saldos negativos permitidos con alerta

4. **Rutas Especiales:**
   - EZE-REC: Cálculo post-rol, pago por transferencia
   - Consolidación semanal

## Cómo Usar los Mockups

### Opción 1: Abrir Localmente
1. Abrir `index.html` o `login.html` directamente en un navegador web
2. Hacer clic en "Iniciar Sesión" (sin validación real)
3. Navegar entre módulos usando el menú lateral
4. Explorar formularios, tablas y funcionalidades

### Opción 2: Usar el Servidor Local (Para Compartir)
1. Ejecutar `servidor.bat` (Windows) o `python servidor.py` (cualquier sistema)
2. El servidor mostrará URLs para acceso local y desde otros dispositivos
3. Compartir la URL con otros usuarios en la misma red
4. Ver `INSTRUCCIONES_COMPARTIR.md` para más detalles

## 📤 Compartir el Sistema

Para compartir el sistema con otros usuarios, consulta los siguientes archivos:

### 🌐 Publicar en GitHub Pages (Recomendado)
- **`GUIA_GITHUB.md`**: Guía completa paso a paso para publicar en GitHub y activar GitHub Pages
- **`subir-github.bat`**: Script para facilitar la subida de cambios a GitHub

### 🏠 Servidor Local
- **`INSTRUCCIONES_COMPARTIR.md`**: Instrucciones para servidor local y otras opciones
- **`servidor.bat`**: Script para iniciar servidor local

**Opciones disponibles:**
- ✅ GitHub Pages (gratis, acceso desde internet)
- ✅ Servidor local (misma red WiFi)
- ✅ Netlify, Vercel, Surge.sh (alternativas en la nube)

## Notas Técnicas

- Los mockups son estáticos (HTML/CSS puro)
- No hay funcionalidad JavaScript real (solo navegación básica)
- Los datos mostrados son ejemplos
- Los formularios no envían datos reales
- Diseñado para ser usado como referencia visual para desarrollo

## ✅ Ajustes Implementados (Enero 2025)

### Clasificación de Movimientos
- **Programado**: Operación normal del día siguiente
- **Contingencia**: Cambios no previstos (tripulaciones varadas, reemplazos, apoyos especiales)
- **Apoyo**: Casos de apoyo a otras bases
- **Otro**: Otros casos especiales

### Trazabilidad de Movimientos Manuales
- Todos los movimientos ingresados manualmente quedan identificados como **MANUAL**
- Se muestra el origen del dato (AIMS o MANUAL) en todas las tablas
- Clasificación visible en tablas de movimientos y cálculos

### Indicadores de Control de Caja
- **Gasto Diario**: Muestra el gasto del día actual por caja
- **Gasto Acumulado**: Muestra el gasto acumulado del mes por caja
- Indicadores visibles en:
  - Dashboard principal
  - Módulo de Control de Caja
  - Tarjetas de resumen de cada caja

### Diferenciación Programado vs Contingencia
- Filtro por clasificación en módulo de cálculo
- Badges visuales para identificar tipo de viático
- Diferenciación automática en el sistema

## Próximos Pasos de Desarrollo

1. Implementar backend con base de datos
2. Integración con AIMS (confirmar base de datos, tablas y campos)
3. Sistema de autenticación real
4. Lógica de cálculo de viáticos parametrizable
5. Generación real de reportes
6. Sistema de notificaciones
7. API para búsqueda de tripulantes
8. Ejecución programada diaria (4:00 - 5:00 p.m.)
9. Recalcular viáticos si existen cambios en AIMS el mismo día
10. Definir formato de cargas manuales y masivas
