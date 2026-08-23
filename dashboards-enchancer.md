---

name: dashboard-enchance-skill
description: Diseña, analiza y mejora dashboards y paneles administrativos profesionales priorizando datos, jerarquía visual, arquitectura de información, progressive disclosure, estados, interacción, accesibilidad, responsive design y usabilidad. Evita dashboards genéricos, card-soup, decoración innecesaria y UI sin comportamiento.

---

# Dashboard Design Professional

## Purpose

Esta skill define cómo diseñar y evaluar dashboards, paneles administrativos, backoffices, CRMs, ERPs, sistemas de gestión, analytics dashboards y aplicaciones SaaS profesionales.

El objetivo no es simplemente crear una interfaz visualmente atractiva.

El objetivo es crear una interfaz que permita:

**ver → comprender → decidir → actuar**

con la menor fricción cognitiva posible.

---

# Core Philosophy

## 1. Data drives the UI

Los datos deben determinar la forma de la interfaz.

Nunca comenzar con:

> "¿Qué cards, gráficos o componentes puedo agregar?"

Comenzar con:

> "¿Qué información existe, qué necesita comprender el usuario y cuál es la mejor representación para esa información?"

### Mapping obligatorio

| Data                   | Preferred UI             |
| ---------------------- | ------------------------ |
| Métrica                | KPI / Metric             |
| Comparación            | Table                    |
| Evolución temporal     | Line / Area chart        |
| Distribución           | Bar chart                |
| Estado                 | Badge / Chip             |
| Actividad temporal     | Timeline / Activity feed |
| Entidad                | List / Table / Card      |
| Información contextual | Tooltip / Popover        |
| Detalle                | Drawer / Detail view     |
| Configuración          | Form                     |
| Acción secundaria      | Dropdown / Context menu  |
| Acción rápida          | Inline action            |
| Ubicación              | Map                      |
| Relación jerárquica    | Tree / Nested list       |

No asumir que una tabla es correcta simplemente porque los datos son tabulares.

No asumir que una card es correcta simplemente porque es un dashboard.

---

# 2. Design around user tasks

Antes de diseñar una pantalla, identificar:

* Qué necesita saber el usuario.
* Qué necesita hacer.
* Qué hace frecuentemente.
* Qué hace ocasionalmente.
* Qué acciones son peligrosas.
* Qué información necesita contexto.
* Qué decisiones debe poder tomar.

Priorizar la UI según:

**frecuencia × importancia × consecuencia**

### High frequency + high importance

Siempre visible.

Ejemplo:

* Buscar
* Crear
* Guardar
* Consultar estado

### High frequency + low importance

Visible o contextual.

### Low frequency + high consequence

Fácil de encontrar, pero con protección.

Ejemplo:

* Eliminar
* Cancelar
* Desactivar

### Low frequency + low consequence

Progressively disclosed.

Ejemplo:

* Copiar ID
* Exportar
* Metadata

---

# 3. Information hierarchy

Cada pantalla debe tener una jerarquía visual evidente.

Prioridad:

1. Información crítica.
2. Acción principal.
3. Métricas importantes.
4. Problemas y alertas.
5. Información secundaria.
6. Acciones secundarias.
7. Información técnica o contextual.

La jerarquía debe utilizar:

* Tamaño.
* Peso tipográfico.
* Contraste.
* Espaciado.
* Posición.
* Agrupación.
* Color.
* Densidad.

No dar el mismo peso visual a todos los elementos.

---

# 4. Avoid card soup

No convertir automáticamente cada sección en una card.

Preguntar:

> "¿Este contenido necesita realmente un contenedor visual?"

Puede utilizarse:

* Espaciado.
* Divisores.
* Agrupación.
* Tipografía.
* Secciones.
* Backgrounds sutiles.

Las cards deben utilizarse cuando ayudan a agrupar información o crear una unidad conceptual.

No utilizarlas simplemente porque "un dashboard tiene cards".

---

# 5. Progressive Disclosure

No mostrar toda la funcionalidad al mismo tiempo.

Utilizar el spectrum of explicitness:

```text
ALWAYS VISIBLE
      ↓
VISIBLE IN CONTEXT
      ↓
VISIBLE ON INTERACTION
      ↓
VISIBLE WHEN REQUESTED
```

### Always visible

* Primary action.
* Search.
* Critical filters.
* Important navigation.

### Contextual

* Edit.
* Share.
* Export.
* Secondary actions.

### Interaction

* Copy.
* Delete.
* Row actions.
* Additional metadata.

### Requested

* Advanced configuration.
* Technical details.
* Full history.
* Metadata.

No esconder una función importante solamente para conseguir una apariencia minimalista.

---

# 6. UI is what you can't see

Diseñar explícitamente tanto la UI visible como la UI contextual.

Cada componente debe considerar:

* Default.
* Hover.
* Focus.
* Active.
* Selected.
* Disabled.
* Loading.
* Empty.
* Error.
* Success.

Además considerar:

* Tooltip.
* Popover.
* Dropdown.
* Drawer.
* Modal.
* Toast.
* Context menu.
* Confirmation.
* Inline editing.
* Keyboard interaction.

Una interfaz no está terminada cuando su estado normal está diseñado.

---

# 7. State-first design

Antes de considerar terminado un componente, definir sus estados.

## Buttons

```text
Default
Hover
Focus
Active
Disabled
Loading
Success
Error
```

## Inputs

```text
Empty
Focused
Filled
Invalid
Disabled
Read-only
Loading
```

## Tables

```text
Loading
Empty
Populated
Filtered
Selected
Error
Partial
```

## Pages

```text
Loading
Empty
Error
Unauthorized
Forbidden
Offline
Success
```

---

# 8. Empty states

Nunca limitarse a:

> "No hay datos."

Un empty state debe explicar:

1. Qué está vacío.
2. Por qué.
3. Qué puede hacer el usuario.

Preferir:

```text
Todavía no tenés clientes.

Registrá tu primer cliente para comenzar.

[ + Nuevo cliente ]
```

El empty state debe ser funcional, no simplemente informativo.

---

# 9. Loading states

Elegir el loading state según el contexto.

Utilizar:

* Skeleton.
* Spinner.
* Progress.
* Optimistic UI.
* Placeholder.

Preferir skeleton cuando la estructura del contenido sea conocida.

Evitar bloquear toda la pantalla con un spinner si solamente está cargando una sección.

---

# 10. Error handling

Todo error visible debe responder:

* Qué ocurrió.
* Qué impacto tiene.
* Qué puede hacer el usuario.

Evitar:

```text
Error 500.
```

Preferir:

```text
No pudimos cargar las reservas.

Intentá nuevamente.

[ Reintentar ]
```

Cuando sea posible:

* Preservar datos introducidos.
* Mantener contexto.
* Permitir retry.
* Explicar recuperación.
* Evitar obligar al usuario a repetir trabajo.

---

# 11. Feedback

Toda acción importante debe proporcionar feedback.

Ejemplo:

```text
Guardar
↓
Guardando...
↓
Cambios guardados ✓
```

El usuario nunca debería quedar preguntándose:

> "¿Funcionó?"

Utilizar:

* Toast.
* Inline feedback.
* State change.
* Progress.
* Confirmation.
* Undo.

---

# 12. Undo over confirmation when appropriate

Para acciones reversibles, preferir Undo cuando sea más eficiente que un modal.

Ejemplo:

```text
Cliente archivado.

[ Deshacer ]
```

No interrumpir constantemente el flujo con confirmaciones innecesarias.

Para acciones irreversibles o de alto impacto, utilizar confirmación explícita.

---

# 13. Tables

Una tabla debe existir porque facilita una tarea.

Debe contemplar cuando corresponde:

* Search.
* Filtering.
* Sorting.
* Pagination.
* Selection.
* Bulk actions.
* Row actions.
* Column visibility.
* Export.
* Detail view.

## Column hierarchy

Clasificar columnas:

### Primary

Siempre visibles.

### Secondary

Ocultables o adaptables.

### Contextual

Mostrar mediante:

* Drawer.
* Expanded row.
* Detail page.
* Popover.

---

# 14. Table interaction

Evitar colocar demasiadas acciones directamente en cada fila.

Preferir:

```text
⋯
```

para acciones secundarias.

Usar hover para revelar acciones cuando sea apropiado.

Ejemplo:

```text
Juan Pérez     Admin     Activo     ⋯
```

No convertir cada fila en una barra de herramientas.

---

# 15. Numbers

Los valores numéricos deben estar correctamente alineados.

Por defecto:

**right-align numbers**

Esto facilita comparar:

```text
$       9.500
$      25.000
$     125.000
$   1.250.000
```

Utilizar formatos consistentes:

* Moneda.
* Porcentaje.
* Decimales.
* Separadores.
* Unidades.

---

# 16. Text truncation

No permitir que textos largos rompan una tabla o layout.

Usar:

* Ellipsis.
* Tooltip.
* Expand.
* Drawer.
* Detail view.

Nunca sacrificar toda la estructura de la interfaz para mostrar texto secundario completo.

---

# 17. Semantic color

El color debe tener significado.

Usar colores principalmente para:

* Success.
* Warning.
* Error.
* Info.
* Status.
* Priority.
* Selection.

No utilizar colores arbitrarios únicamente para decorar cards.

### Important

Nunca comunicar información únicamente mediante color.

Combinar:

**color + icon + label**

cuando sea relevante.

---

# 18. Charts

Un chart debe responder una pregunta.

Antes de agregarlo:

> "¿Qué decisión permite tomar este gráfico?"

Utilizar charts para:

* Tendencias.
* Comparaciones.
* Distribuciones.
* Anomalías.
* Evolución.
* Relaciones.

No agregar charts simplemente porque "el dashboard necesita gráficos".

---

# 19. Dashboard hierarchy

Un dashboard general debería normalmente seguir:

```text
Global status
      ↓
Key metrics
      ↓
Alerts / problems
      ↓
Trends
      ↓
Recent activity
      ↓
Actions
      ↓
Detailed analysis
```

No convertir el dashboard principal en una página de reportes.

Su objetivo principal es:

> **orientar al usuario y permitirle actuar.**

---

# 20. KPI design

Una KPI debe proporcionar contexto.

No mostrar únicamente:

```text
1.248
```

Preferir:

```text
CLIENTES

1.248

↑ 12,5%
vs. mes anterior
```

Una KPI debería responder:

* Qué.
* Cuánto.
* Comparado con qué.
* Si está mejorando o empeorando.

---

# 21. Alerts

Las alertas deben representar problemas accionables.

Ejemplo:

```text
⚠ 3 productos tienen stock crítico

[ Ver productos ]
```

No sobreutilizar alertas.

> If everything is urgent, nothing is urgent.

---

# 22. Activity feeds

Activity feeds deberían comunicar:

* Who.
* What.
* Which entity.
* When.

Ejemplo:

```text
Juan creó una reserva
Hace 3 minutos

María confirmó un pago
Hace 8 minutos
```

Utilizar avatars/icons cuando aceleren el reconocimiento.

---

# 23. Context preservation

No perder innecesariamente:

* Search.
* Filters.
* Sorting.
* Pagination.
* Selected items.
* Scroll position.
* Current tab.

Si el usuario vuelve a una pantalla, conservar su contexto cuando sea razonable.

---

# 24. Navigation

La navegación debe reflejar el modelo mental del usuario, no la arquitectura interna del código.

Ejemplo:

```text
Dashboard

OPERACIONES
  Clientes
  Ventas
  Inventario

ANÁLISIS
  Reportes
  Estadísticas

SISTEMA
  Configuración
```

Separar conceptualmente:

* Operations.
* Analysis.
* Administration.
* Configuration.

---

# 25. Contextual navigation

Dentro de una entidad utilizar:

* Tabs.
* Secondary navigation.
* Breadcrumbs.

Ejemplo:

```text
Cliente
├── Información
├── Actividad
├── Compras
├── Pagos
└── Historial
```

No enviar al usuario a páginas independientes cuando un contexto interno sea suficiente.

---

# 26. Modals vs Drawers vs Popovers

## Modal

Para:

* Confirmaciones importantes.
* Tareas concentradas.
* Acciones que requieren interrupción.

## Drawer

Para:

* Detalles.
* Inspección.
* Edición contextual.
* Información extensa.

## Popover

Para:

* Acciones rápidas.
* Filtros.
* Información contextual.
* Contenido pequeño.

## Tooltip

Para:

* Explicaciones breves.
* Iconos.
* Labels ambiguos.

---

# 27. Responsive

No simplemente reducir desktop.

Cada breakpoint debe tener una estrategia.

### Desktop

Priorizar:

* Densidad.
* Comparación.
* Multi-column.
* Sidebar.

### Tablet

Reducir:

* Columnas.
* Navegación.
* Acciones simultáneas.

### Mobile

Transformar:

* Tables → lists/cards.
* Filters → drawer.
* Actions → menus.
* Sidebar → navigation menu.
* Secondary information → detail view.

Preguntar:

> "¿Qué información puede desaparecer sin afectar la tarea?"

---

# 28. Accessibility

Todo dashboard debe considerar:

* WCAG principles.
* Contrast.
* Keyboard navigation.
* Focus.
* Screen readers.
* Semantic HTML.
* Labels.
* Accessible names.
* Reduced motion.

No utilizar el color como único indicador.

Icon-only buttons necesitan accessible labels.

Los estados de focus deben ser visibles.

---

# 29. Design tokens

Mantener consistencia mediante tokens.

## Spacing

```text
4
8
12
16
24
32
48
64
```

## Typography

```text
Display
Heading
Body
Label
Caption
```

## Color

```text
Background
Surface
Border
Text
Muted
Primary
Success
Warning
Danger
Info
```

## Radius

Utilizar un sistema limitado y consistente.

No asignar valores arbitrarios a cada componente.

---

# 30. Consistency

Una misma acción debe verse y comportarse de manera similar en todo el producto.

Si:

```text
[ + Nuevo cliente ]
```

es la acción principal en Clientes, utilizar el mismo patrón para:

```text
[ + Nueva venta ]
[ + Nuevo producto ]
[ + Nueva reserva ]
```

La consistencia reduce el aprendizaje.

---

# 31. Microinteractions

Utilizar animaciones para comunicar:

* Cambio.
* Causa y efecto.
* Entrada.
* Salida.
* Feedback.
* Continuidad espacial.

No utilizar animaciones únicamente para decorar.

### Rule

> Animation should explain a transition, not compete with the content.

---

# 32. Performance perception

El usuario debe percibir que la aplicación responde.

Considerar:

* Skeletons.
* Optimistic updates.
* Lazy loading.
* Pagination.
* Virtualization.
* Progressive loading.
* Immediate feedback.

No bloquear toda la interfaz si solamente una sección está cargando.

---

# 33. Forms

Mostrar primero la información necesaria.

Separar:

### Essential

Campos necesarios para completar la tarea.

### Optional

Información complementaria.

### Advanced

Configuraciones técnicas.

Ejemplo:

```text
Nuevo producto

Nombre *
Precio *
Categoría *

[ Más opciones ]

Stock
Proveedor
SKU
Impuestos
Metadata
```

No presentar 30 campos cuando solamente 4 son necesarios para comenzar.

---

# 34. Validation

Validar cerca del problema.

Preferir:

```text
Email

luigi@

⚠ Introducí un email válido
```

en lugar de esperar al submit para informar todos los errores.

Preservar siempre los datos introducidos cuando sea posible.

---

# 35. Destructive actions

Acciones de alto impacto necesitan mayor explicitud.

Ejemplos:

* Delete.
* Cancel.
* Disable.
* Reset.
* Remove.

Considerar:

* Context.
* Confirmation.
* Consequence.
* Undo.
* Reauthentication.

Nunca colocar acciones destructivas importantes junto a acciones frecuentes sin diferenciación suficiente.

---

# 36. Permissions

La UI debe considerar roles y permisos.

No mostrar acciones que el usuario no puede ejecutar cuando ocultarlas sea más claro.

Considerar:

```text
View
Create
Edit
Delete
Export
Manage
Configure
```

No asumir que todos los usuarios tienen el mismo nivel de acceso.

---

# 37. Auditability

Para sistemas empresariales, considerar:

```text
Who
What
When
Before
After
```

Ejemplo:

```text
Juan Pérez

Modificó el precio.

Anterior: $25.000
Nuevo:    $27.500

23/08/2026 — 16:42
```

Especialmente importante para:

* ERP.
* CRM.
* Inventario.
* Finanzas.
* Administración.

---

# 38. Cognitive load

Reducir:

* Decisiones simultáneas.
* Información redundante.
* Colores innecesarios.
* Botones innecesarios.
* Texto innecesario.
* Navegación ambigua.
* Estados poco claros.

Utilizar:

* Grouping.
* Hierarchy.
* Progressive disclosure.
* Consistency.
* Context.
* Defaults inteligentes.

---

# 39. Scanability

Los usuarios generalmente escanean dashboards antes de leerlos.

Diseñar para que puedan identificar rápidamente:

* Qué está pasando.
* Qué cambió.
* Qué está mal.
* Qué requiere atención.
* Qué pueden hacer.

Utilizar:

* Headings.
* Numbers.
* Badges.
* Icons.
* Alignment.
* Whitespace.
* Grouping.

---

# 40. Three-level information architecture

Diseñar la información en niveles.

## Level 1 — Scan

Información inmediatamente visible.

## Level 2 — Inspect

Información contextual al profundizar.

## Level 3 — Act

Acciones específicas.

Ejemplo:

```text
CLIENTE

Juan Pérez
Activo
$125.000

        ↓

Información
Email
Teléfono
Última compra

        ↓

Acciones
Editar
Archivar
Más acciones
```

---

# 41. Decision framework

Antes de agregar cualquier elemento, responder:

```text
1. ¿Qué información representa?
2. ¿Por qué necesita existir?
3. ¿Quién la necesita?
4. ¿Con qué frecuencia?
5. ¿Qué decisión permite tomar?
6. ¿Qué acción permite realizar?
7. ¿Debe estar siempre visible?
8. ¿Puede ser contextual?
9. ¿Qué ocurre cuando está vacío?
10. ¿Qué ocurre si falla?
```

Si no tiene una respuesta clara:

**considerar eliminarlo.**

---

# 42. Dashboard quality test

Un dashboard debe poder evaluarse con estas preguntas:

### Data

* ¿Los datos determinan la UI?
* ¿La representación es adecuada?

### Hierarchy

* ¿Qué veo primero?
* ¿Qué puedo ignorar?

### Action

* ¿Cuál es la acción principal?
* ¿Puedo encontrarla inmediatamente?

### Context

* ¿Sé dónde estoy?
* ¿Sé sobre qué entidad estoy trabajando?

### State

* ¿Qué ocurre cuando carga?
* ¿Qué ocurre cuando está vacío?
* ¿Qué ocurre si falla?

### Interaction

* ¿Qué aparece al hover?
* ¿Qué aparece al focus?
* ¿Qué acciones están ocultas?

### Feedback

* ¿Sé si mi acción funcionó?

### Accessibility

* ¿Puedo utilizarlo con teclado?
* ¿El color es suficiente?
* ¿Los iconos tienen significado accesible?

### Responsive

* ¿Qué sucede en mobile?

---

# 43. Mandatory design workflow

Cuando esta skill se utilice para crear un dashboard, seguir este orden:

## Step 1 — Understand

Identificar:

* Usuario.
* Rol.
* Objetivos.
* Tareas.
* Datos.
* Frecuencia.
* Consecuencias.

## Step 2 — Model

Definir:

* Entidades.
* Relaciones.
* Estados.
* Permisos.
* Dimensiones de datos.

## Step 3 — Prioritize

Clasificar:

* Primary.
* Secondary.
* Contextual.
* Advanced.

## Step 4 — Choose representation

Determinar:

* Table.
* Chart.
* Timeline.
* List.
* Card.
* Metric.
* Form.
* Drawer.
* Popover.

## Step 5 — Structure

Crear:

* Navigation.
* Sections.
* Hierarchy.
* Layout.
* Information levels.

## Step 6 — Interaction

Definir:

* Hover.
* Focus.
* Click.
* Selection.
* Menus.
* Shortcuts.
* Inline actions.

## Step 7 — States

Diseñar:

* Loading.
* Empty.
* Error.
* Success.
* Disabled.
* Offline.
* Permission denied.

## Step 8 — Responsive

Definir comportamiento:

* Desktop.
* Tablet.
* Mobile.

## Step 9 — Accessibility

Revisar:

* Keyboard.
* Contrast.
* Labels.
* Focus.
* Semantic structure.

## Step 10 — Polish

Solamente después optimizar:

* Typography.
* Spacing.
* Colors.
* Borders.
* Radius.
* Shadows.
* Animation.

**Visual polish comes last.**

---

# 44. Anti-patterns

Evitar explícitamente:

## Generic dashboard

```text
6 cards
+
3 charts
+
recent activity
+
table
```

sin una razón funcional.

## Card soup

Todo convertido en cards.

## Chart decoration

Gráficos que no responden ninguna pregunta.

## Rainbow UI

Colores sin significado.

## Button overload

Demasiadas acciones visibles.

## Modal overload

Todo resuelto mediante modals.

## Tooltip dependency

Información fundamental escondida en tooltips.

## Desktop shrinking

Desktop simplemente reducido para mobile.

## One-state design

Diseñar solamente el estado normal.

## Empty dashboard

Dashboard que no orienta al usuario.

## Decorative minimalism

Ocultar funcionalidades importantes únicamente para conseguir una apariencia "clean".

---

# 45. Final principles

Estas reglas tienen prioridad durante cualquier diseño:

1. **Data drives the UI.**
2. **User tasks drive the hierarchy.**
3. **Important actions remain discoverable.**
4. **Secondary actions are progressively disclosed.**
5. **Every component has states.**
6. **Every important action provides feedback.**
7. **Color communicates meaning.**
8. **Not everything needs a card.**
9. **Not everything needs a table.**
10. **Charts must answer questions.**
11. **Context should be preserved.**
12. **Errors should be recoverable.**
13. **Accessibility is part of the design, not an afterthought.**
14. **Responsive behavior must be intentionally designed.**
15. **Visual polish comes after information architecture and interaction design.**

---

# Final Mental Model

Cuando diseñes un dashboard, pensar siempre:

```text
DATA
  ↓
MEANING
  ↓
REPRESENTATION
  ↓
HIERARCHY
  ↓
PROGRESSIVE DISCLOSURE
  ↓
INTERACTION
  ↓
STATE
  ↓
FEEDBACK
  ↓
ACCESSIBILITY
  ↓
RESPONSIVE
  ↓
VISUAL POLISH
```

El resultado esperado no es:

> "Un dashboard lindo."

El resultado esperado es:

> **Una herramienta que permite al usuario comprender información, detectar situaciones importantes y actuar rápidamente.**

---

# Golden Rule

> ## Don't design the dashboard.
>
> ## Design the user's understanding of the data.

Un dashboard profesional debe permitir:

**SEE → UNDERSTAND → DECIDE → ACT**

con la menor fricción posible.
