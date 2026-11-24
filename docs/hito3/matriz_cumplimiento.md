# Matriz de cumplimiento de la entrega final

Fuente de requisitos: transcripción `PAUTAS_ENTREGA_FINAL.md` proporcionada por el estudiante, basada en las páginas 1–5 de la consigna. El PDF original no se adjuntó a esta revisión. Los estados describen evidencia observada en la rama `cambios-Luciano`; no son una nota académica. Se distingue lo exigido por la consigna de las recomendaciones del proyecto.

## Instrucciones generales y Hito 1

| Requisito oficial | Página | Evidencia examinada | Prueba ejecutada | Resultado | Estado | Acción pendiente |
|---|---:|---|---|---|---|---|
| Grupo de 3 a 4 integrantes | 1 | `README.md`, carátulas históricas | Comparación de nombres | Tres integrantes identificados | Cumplido y verificado | Confirmar datos finales con el equipo |
| Gestión de proyectos y código fuente | 1 | `docs/gestion_del_proyecto.md`, historial Git | Inspección de archivo y commits | Tablero y flujo documentados | Parcial | Equipo confirma uso real de la herramienta de gestión |
| URL GitHub y ZIP completo | 1 | `README.md`, `entregables/kipu_hito3.zip` | `ZipFile.testzip()` y revisión de contenido | ZIP íntegro; URL consignada; commits finales solo locales | Parcial | Equipo revisa y autoriza publicación antes de entregar URL actualizada |
| Artefactos de análisis, diseño y desarrollo en repositorio | 1 | `grammar/`, `src/`, `tests/`, `docs/` | Inventario Git y ZIP | Fuentes e informes presentes; presentación PDF y video final ausentes | Parcial | Incorporar artefactos finales tras revisión humana |
| Componentes mínimos o interoperabilidad del lenguaje | 1 | `grammar/Kipu.g4`, `src/` | Lexer, parser, semántica, IR y JIT | Funcionan los casos probados | Cumplido y verificado | Revisar cobertura final del equipo |
| Visto bueno del profesor para la idea | 1 | Informes históricos | Solo consta narración del proyecto | No hay evidencia independiente de aprobación | No verificable | Equipo aporta constancia o confirma con docente |
| Originalidad y realización por el equipo | 1 | Código e informes | Una prueba técnica no establece autoría | No verificable por este agente | No verificable | Integrantes revisan, comprenden y realizan trabajo propio; consultar asistencia permitida |
| Problemática, motivación y objetivos | 2–3 | Informe Hito 1 pp. 2–3; informe Hito 3 §§1–2 | Lectura de documentos | Contenido presente | Cumplido y verificado | Revisar redacción final |
| Siete construcciones y cinco ejemplos por cada una | 2–3 | `tests/construcciones.py`, informe Hito 3 anexo A | `test_ejemplos_de_cada_construccion` | 35 ejemplos reconocidos | Cumplido y verificado | Ninguna técnica |
| Léxico: tipos, variables y palabras clave | 2–3 | `grammar/Kipu.g4`, informe Hito 3 §§2 y anexo B | Pruebas léxicas | Reconocimiento correcto en casos probados | Cumplido y verificado | Ninguna técnica |
| Token y lexemas en informe | 2–3 | Informe Hito 3 anexo B | Cotejo con reglas de lexer | Tabla de 54 tokens incorporada | Cumplido y verificado | Revisar maquetación del informe final |
| Lexer ANTLR con expresiones regulares y varias entradas | 2–3 | `grammar/Kipu.g4`, `src/generated/`, `tests/lexico` | `unittest` léxico | Casos válidos e inválidos pasan | Cumplido y verificado | Ninguna técnica |
| Gramáticas libres de contexto por construcción y notación de clase | 2–3 | `grammar/Kipu.g4`, `docs/hito3/gramatica_bnf.txt` | `gramatica_bnf.py`, `verificar_gramatica.py` | G0–G7 y L1–L6 presentes | Cumplido y verificado | Equipo confirma notación con docente |
| Cuatro derivaciones izquierdas por gramática | 2–3 | `docs/anexo_derivaciones.md` | `scripts/derivaciones.py` | 28 derivaciones sin fallos | Cumplido y verificado | Adjuntar anexo al formato final |
| Parser ANTLR4 y varias entradas | 2–3 | `src/generated/`, `tests/sintactico` | `unittest` sintáctico | Casos válidos e inválidos pasan | Cumplido y verificado | Ninguna técnica |
| Al menos dos errores semánticos | 2–3 | `src/visitor_semantico.py`, `tests/semantico` | `unittest` semántico | 14 códigos cubiertos | Cumplido y verificado | Ninguna técnica |
| Informe Hito 1 máximo 5 páginas más carátula | 2–3 | `docs/hito1/Informe_TrabajoParcial_Kipu.pdf` | Conteo de páginas PDF | 11 páginas: excede el máximo indicado | Parcial | No alterar entrega histórica; equipo consulta cómo tratarlo en la final |
| Fuente, G4 y driver simple | 2–3 | `src/`, `grammar/`, `src/kipu.py` | CLI y pruebas | Presentes y funcionales | Cumplido y verificado | Ninguna técnica |
| Presentación Hito 1 en PDF | 2–3 | `docs/hito1/Presentacion_Kipu.pdf` | Apertura y conteo PDF | 12 páginas | Cumplido y verificado | Confirmar que fue la versión enviada |
| Video Hito 1 de máximo 5 minutos | 2–3 | `docs/hito1/Enlace_Video_Demo.txt` | Lectura del enlace | Existe URL; duración y entrega no verificadas | No verificable | Equipo verifica video y evidencia de entrega |

## Hitos 2 y 3

| Requisito oficial | Página | Evidencia examinada | Prueba ejecutada | Resultado | Estado | Acción pendiente |
|---|---:|---|---|---|---|---|
| Hito 2 integra requisitos anteriores | 3 | Informe Hito 2 PDF | Lectura de secciones | Integra léxico, gramática, semántica, arquitectura y plan | Cumplido y verificado | Confirmar versión entregada |
| Gramática actualizada | 3 | `grammar/Kipu.g4`, informes | Verificador L1–L6 | Aprobado | Cumplido y verificado | Ninguna técnica |
| Seis o más errores semánticos verificados | 3 | `visitor_semantico.py`, pruebas | Casos SEM-01 a SEM-14 | 14 códigos preservados | Cumplido y verificado | Ninguna técnica |
| Arquitectura y plan de validación | 3 | Informe Hito 3 §§3 y 7; Hito 2 §§8–9 | Inspección | Arquitectura vigente y plan presentes | Cumplido y verificado | Equipo revisa lenguaje del informe |
| Avance de implementación Hito 2 | 3 | PDF histórico Hito 2, Git | Inspección del informe y commits | Avance documentado | Cumplido y verificado | Entrega histórica no verificable aquí |
| Informe final acumula Hitos 1 y 2 | 3 | `docs/hito3/informe_hito3.md` y anexos | Cotejo de secciones | Contenido técnico integrado; formato final pendiente | Parcial | Equipo revisa y maqueta versión académica |
| Generación de código final con LLVM | 3 | `src/visitor_llvm.py`, `src/ejecutor.py` | Verificador IR, JIT y pruebas | IR y ejecución correctos en casos probados | Cumplido y verificado | Revisar límite de reglas locales |
| Resultados de validación y conclusiones | 3 | Informe Hito 3 §§7–8 y `resultados_validacion.md` | 29 pruebas, gramática, derivaciones, JIT | Resultados y límites reales registrados | Cumplido y verificado | Equipo confirma conclusiones |
| Repositorio completo, URL y ZIP | 1, 3 | Git, `README.md`, ZIP | `git status`, integridad ZIP | Material local completo; GitHub aún no refleja commits | Parcial | Publicar solo tras autorización y revisión del equipo |
| Presentación final en PDF | 3 | `docs/hito3/presentacion_hito3.md` | Revisión de contenido | Guion preparado, PDF ausente | Pendiente | Equipo produce y revisa PDF final |
| Demo final en video, máximo 5 minutos | 3 | `guia_demostracion.md`, `guion_video_5min.md` | Lectura del guion | Guion preparado; video no grabado | Pendiente | Equipo graba, comprueba duración y entrega |
| Sustentación en semana 15 y vestimenta formal | 3 | Consigna transcrita | No comprobable por código | Requiere presencia del equipo | No verificable | Organizar y realizar sustentación |
| Texto del Hito 3 repite “50 %” | 3 | Transcripción de la consigna | Comparación de cláusulas | Inconsistente con exigencia general de implementación completa | Requiere consulta al docente | Confirmar interpretación; se preparó implementación completa de lo probado |

## Rúbrica de evaluación final

La escala de la rúbrica no se convierte en una nota automática. Las cuatro filas siguientes muestran únicamente preparación y evidencia.

| Categoría de la rúbrica | Página | Evidencia examinada | Prueba ejecutada | Resultado | Estado | Acción pendiente |
|---|---:|---|---|---|---|---|
| Documentos requeridos del Hito 2, 0–5 puntos | 4–5 | PDF y PPTX históricos Hito 2 | Presencia de archivos | Archivos presentes; envío no verificable | Parcial | Equipo comprueba acuse de entrega |
| Código desarrollado, 0–5 puntos | 4–5 | Gramática, Visitors, LLVM, plan | 29 pruebas, L1–L6, derivaciones, JIT | Evidencia técnica positiva | Parcial | Docente juzga conceptos de clase y límite de reglas locales |
| Exposición e informe, 0–5 puntos | 4–5 | Informe y guion | Revisión de contenido | Borradores preparados; exposición no realizada | Pendiente | Equipo adapta PDF y ensaya exposición |
| Preguntas, 0–5 puntos | 4–5 | Guía de sustentación | Revisión de preguntas | Material disponible; dominio personal no verificable | No verificable | Cada integrante estudia y responde por sí mismo |

## Recomendaciones del proyecto, separadas de la consigna

La conexión directa `KipuVisitor` → `IRBuilder`, el uso de Windows, los 14 errores y la prueba nativa con Clang proceden de decisiones del proyecto y de la retroalimentación comunicada por el estudiante. La consigna exige LLVM como vía elegida para Kipu, pero no un EXE ni Clang. La restricción de reglas al ámbito global se propone en `propuesta_reglas_locales.md` y **no se ha aplicado**.
