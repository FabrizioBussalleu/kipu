# Teoría de Compiladores — Pautas de entrega final 2026-2

Fuente: `Teoria_de_Compiladores_Trabajo_Parcial_y_Final (2).pdf`, páginas 1–5. Transcripción organizada y lista de verificación para Kipu. No sustituye la consigna original.

## 1. Instrucciones generales (p. 1)

- [ ] Grupo de 3 a 4 integrantes.
- [ ] Uso de herramientas de gestión de proyectos y código fuente.
- [ ] Repositorio GitHub: entregar su URL y el repositorio completo en formato ZIP en los hitos correspondientes.
- [ ] Todos los artefactos de análisis, diseño y desarrollo deben estar en el repositorio.
- [ ] El lenguaje elegido debe contar con los componentes mínimos necesarios o la interoperabilidad correspondiente.
- [ ] La idea del proyecto debe contar con el visto bueno del profesor.
- [ ] El trabajo debe ser original y realizado por el equipo. La consigna establece que cualquier sospecha de que no fue realizado en su totalidad por el equipo implica anulación y nota 0. Confirmar con el docente qué asistencia externa está permitida; no inventar contribuciones ni evidencias.

## 2. Requisitos acumulados del Hito 1 (semana 7, pp. 2–3)

El informe del Hito 1 tiene un máximo de 5 páginas más carátula.

### Informe y diseño del lenguaje
- [ ] Problemática y motivación.
- [ ] Objetivos.
- [ ] Descripción de las construcciones del lenguaje.
- [ ] Cinco ejemplos por cada construcción.

### Analizador léxico
- [ ] Descripción del léxico: tipos, variables, palabras clave, etc.
- [ ] Especificación en formato token: lista de lexemas, incluida en el informe.
- [ ] Implementación mediante expresiones regulares en ANTLR.
- [ ] Pruebas con varias entradas.

### Analizador sintáctico
- [ ] Gramáticas libres de contexto para cada construcción, con la convención de notación enseñada en clase, incluidas en el informe.
- [ ] Cuatro ejemplos representativos por cada gramática, con sus derivaciones más a la izquierda.
- [ ] Implementación en ANTLR4.
- [ ] Pruebas con varias entradas.

### Analizador semántico
- [ ] Descripción de al menos dos errores semánticos en el informe (el Hito 2 eleva este mínimo a seis).
- [ ] Implementación y pruebas con varias entradas.

### Entregables del Hito 1
- [ ] Repositorio con código fuente, archivos G4 y driver simple.
- [ ] Presentación en PDF.
- [ ] Demo en video de máximo cinco minutos.

## 3. Requisitos acumulados del Hito 2 (semana 12, p. 3)

La consigna indica un avance del 50 % de la implementación final.

- [ ] Informe con todo lo anterior.
- [ ] Gramática actualizada.
- [ ] Analizador semántico completo con al menos seis errores semánticos verificados.
- [ ] Arquitectura del compilador.
- [ ] Plan de validación del compilador.
- [ ] Repositorio con avance de la implementación.

## 4. Hito 3 — Trabajo final (semana 15, p. 3)

### Informe final
- [ ] Todo lo anterior (requisitos acumulados de Hitos 1 y 2).
- [ ] Generación de código final con LLVM o generación de código intermedio sin LLVM, según la naturaleza del proyecto y previa consulta con el docente.
- [ ] Resultados de la validación del compilador.
- [ ] Conclusiones.

### Entregables
- [ ] Repositorio de código fuente completo.
- [ ] URL de GitHub y ZIP completo, conforme a las instrucciones generales.
- [ ] Presentación en PDF.
- [ ] Demo en video del funcionamiento del compilador, máximo 5 minutos.

### Sustentación
- Última sesión de la semana 15.
- Vestimenta formal profesional (business professional attire).

### Precisiones de la fuente
- El enunciado general exige front end y back end completos, usando ANTLR y LLVM cuando corresponda (p. 2).
- El texto del Hito 3 repite literalmente que se presentará un 50 % de la implementación final, igual que el Hito 2. Existe una inconsistencia con la exigencia general de implementación completa y repositorio completo. No asumir que basta entregar la mitad: consultar al docente.
- El límite de cinco páginas más carátula se indica expresamente para Hito 1; no se especifica un límite independiente para Hito 3.
- No se especifica Clang, archivo EXE, sistema operativo, número de diapositivas ni formato de archivo del informe final. La presentación sí debe ser PDF. Confirmar detalles no especificados con el docente.

## 5. Rúbrica oficial del trabajo final (pp. 4–5)

| Categoría | Bueno | Regular | Por mejorar |
|---|---|---|---|
| Hito 2 | Envía documentos requeridos: 5 puntos | No envía todos: 1–4 puntos | No envía ninguno: 0 puntos |
| Código desarrollado (gramáticas, arquitectura, plan de validación, LLVM) | Cumple indicaciones y usa correctamente conceptos vistos en clase: 4–5 puntos | Cumple indicaciones y usa parcialmente conceptos vistos en clase: 3 puntos | No cumple indicaciones y/o usa conceptos no vistos en clase: 0–2 puntos |
| Exposición e informe | Exposición adecuada en lenguaje formal, dominio del tema: 4–5 puntos | Exposición inadecuada y/o falta de dominio: 3 puntos | No demuestra dominio y evidencia falta de conocimientos del curso: 0–2 puntos |
| Preguntas | Responde correctamente: 4–5 puntos | Responde parcialmente: 3 puntos | No responde y/o no demuestra conocimientos del curso: 0–2 puntos |

Total máximo: 20 puntos. No asignar una nota automática a partir de pruebas de software: la evaluación corresponde al docente.

## 6. Indicaciones específicas para revisar Kipu (no son requisitos textuales del PDF)

Estas indicaciones proceden de la retroalimentación comunicada por el estudiante y las decisiones del proyecto:

- Revisar la conexión directa entre `KipuVisitor` e `ir.IRBuilder`, siguiendo los ejemplos del profesor.
- Mantener clases y métodos explícitos, comprensibles y acordes con los conceptos vistos en clase.
- Revisar que `VisitorSemantico` y `LLVMVisitor` recorran el árbol ANTLR directamente, según la arquitectura elegida por el equipo.
- Comprobar las siete construcciones documentadas, sus ejemplos y derivaciones; no asumir que el número de archivos equivale al número de casos correctos.
- Verificar los 14 códigos semánticos reportados, sin confundir el mínimo oficial de seis con el objetivo interno de conservar los catorce.
- Comprobar que toda construcción aceptada por el front end pueda compilarse o que sus restricciones estén justificadas y aprobadas. Revisar especialmente las reglas locales y GEN-01.
- Ejecutar pruebas reales de LLVM IR y JIT en Windows. La prueba nativa con Clang es una comprobación adicional; consultar si el docente exige código nativo aparte del IR y JIT.
- Conservar los informes históricos; actualizar el informe final para reflejar la arquitectura vigente.
- Trabajar exclusivamente en `cambios-Luciano`; no publicar commits adicionales ni realizar merges sin autorización.

## 7. Instrucciones de auditoría para Codex

1. Contrastar cada casilla de las secciones 1–4 con el repositorio real y la consigna original.
2. Crear una matriz con columnas: requisito, página de la consigna, archivo o sección de evidencia, prueba ejecutada, resultado, estado y acción pendiente.
3. Usar estados: cumplido y verificado, parcial, pendiente, no verificable o requiere consulta al docente.
4. No marcar como cumplido un requisito basándose solamente en un informe previo. Inspeccionar el código y ejecutar pruebas cuando corresponda.
5. Distinguir los requisitos oficiales de las recomendaciones de la sección 6.
6. Identificar entregables que aún sean borradores y tareas que requieren participación directa del equipo, como revisión de autoría, sustentación, grabación del video y entrega académica.
7. Registrar discrepancias y limitaciones en `INFORME_FINAL.md` y `PROGRESO.md`. No inventar resultados ni atribuciones.
8. Presentar los pendientes priorizados antes de considerar la entrega completa. No alterar la especificación del lenguaje ni publicar cambios sin la autorización correspondiente.
